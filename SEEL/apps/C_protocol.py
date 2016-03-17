#!/usr/bin/python
'''
oscilloscope for the vLabtool - version 0. \n

Also Includes XY plotting mode, and fitting against standard Sine/Square functions\n
'''

from __future__ import print_function
import os
os.environ['QT_API'] = 'pyqt'
import sip
sip.setapi("QString", 2)
sip.setapi("QVariant", 2)


from PyQt4 import QtCore, QtGui
import time,sys
from SEEL.templates import digitalScope

import sys,os,string
import time
import sys

import pyqtgraph as pg

import numpy as np


err_count=0
trial = 0
start_time = time.time()
fps = None
dacval=0
from SEEL.commands_proto import *

params = {
'image' : 'logic.png',
'name':'Logic\nAnalyzer',
'hint':'4-Channel Logic analyzer that uses inputs ID1 through ID4. Capable of detecting various level changes in the input signal, and recording timestamps'
}



class AppWindow(QtGui.QMainWindow, digitalScope.Ui_MainWindow):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)
		from SEEL.analyticsClass import analyticsClass
		self.math = analyticsClass()

		self.setWindowTitle(self.I.H.version_string+' : '+params.get('name','').replace('\n',' ') )

		self.plot=pg.PlotWidget(enableMenu=False)
		self.plot.setTitle('Logic Analyzer' )

		#cross hair
		self.vLine = pg.InfiniteLine(angle=90, movable=True)
		#self.vLine.setPen(color=(135,44,64,150), width=3)
		self.plot.addItem(self.vLine, ignoreBounds=False)


		self.proxy = pg.SignalProxy(self.vLine.scene().sigMouseMoved, rateLimit=60, slot=self.readCursor)
		
		self.fps=0
		self.active_dchannels=1
		self.channel_states=np.array([1,0,0,0])
		self.channels_in_buffer=1
		self.dtrig=0
		self.dchan_modes=[1,1,1,1]
		self.dtime=0.001
		self.maxT=0


		self.max_samples_per_channel=[0,self.I.MAX_SAMPLES/4,self.I.MAX_SAMPLES/4,self.I.MAX_SAMPLES/4,self.I.MAX_SAMPLES/4]
		self.samples=self.I.MAX_SAMPLES/4#self.sample_slider.value()
		self.lastTime=time.time()
		self.trace_colors=[(0,255,20),(255,255,0),(255,10,100),(10,255,255)]
		self.plot.setLabel('bottom', 'Time -->>', units='uS')
		self.LlabelStyle = {'color': 'rgb%s'%(str(self.trace_colors[0])), 'font-size': '11pt'}
		self.plot.setLabel('left','CH1', units='V',**self.LlabelStyle)
		#self.plot.addLegend(offset=(-10,30))
		self.plot.getPlotItem().setMouseEnabled(True,False)
		self.plot.setLimits(yMax=12,yMin=0)

		self.curve1 = self.plot.plot(name='1'); self.curve1.setPen(color=self.trace_colors[0], width=1)
		self.curve2 = self.plot.plot(name='2'); self.curve2.setPen(color=self.trace_colors[1], width=1)
		self.curve3 = self.plot.plot(name='3'); self.curve3.setPen(color=self.trace_colors[2], width=1)
		self.curve4 = self.plot.plot(name='4'); self.curve4.setPen(color=self.trace_colors[3], width=1)
		#self.I.sqr4_continuous(1000,.5,0.1,.5,0.3,.3,0.5,.1)

		self.plot.showGrid(True,False,0.4)
		self.plot_area.addWidget(self.plot)
		self.showgrid()
		self.setActiveDigitalChannels(1)
		self.set_digital_scope_time(0)
		self.timer = QtCore.QTimer()
		self.finished=False
		self.timer.timeout.connect(self.update)
		self.timer.start(100)
		
	def updateViews(self):
			self.plot2.setGeometry(self.plot.getViewBox().sceneBoundingRect())
			self.plot2.linkedViewChanged(self.plot.plotItem.vb, self.plot2.XAxis)
		
	def showgrid(self):
		return

	def capture(self):
		self.curve1.clear()
		self.curve2.clear()
		self.curve3.clear()
		self.curve4.clear()
		
		if self.active_dchannels==4:self.I.start_four_channel_LA(1,self.dtime,self.dchan_modes,edge='rising',trigger_ID1=True)
		elif self.active_dchannels==1:#self.start_one_channel_LA_backup(self.dtrig,'ID1',edge='falling')
			aqchan = self.LA1_chan.currentText()
			aqmode = self.LA1_chanmode.currentIndex()
			trchan = self.LA1_trig.currentText()
			trmode = self.LA1_trigmode.currentIndex()
			if(trmode):trmode+=1
			#print(aqchan,aqmode,trchan,trmode)
			if trmode: self.I.start_one_channel_LA(channel=aqchan,channel_mode=aqmode,trigger_channel=trchan,trigger_mode=trmode)
			else : self.I.start_one_channel_LA(channel=aqchan,channel_mode=aqmode,trigger_mode=0)
		elif self.active_dchannels==3:
			trchan = self.LA1_trig.currentText()
			trmode = self.LA1_trigmode.currentIndex()
			if(trmode):trmode+=1
			if trmode: self.I.start_three_channel_LA(modes=self.dchan_modes,trigger_channel=trchan,trigger_mode=trmode)
			else : self.I.start_three_channel_LA(modes=self.dchan_modes,trigger_channel=trchan,trigger_mode=0)
		elif self.active_dchannels==2: self.I.start_two_channel_LA(1)

	def display(self):
		n=0
		self.I.fetch_LA_channels()
		#print(len(self.I.dchans[0].timestamps))
		if len(self.I.dchans[0].timestamps)>2:
			offset = self.I.dchans[0].timestamps[0]
			txt = 'CH1: Offset:\t%.3euS\ttimestamps(uS):\t'%(offset/64.)
			txt += string.join(['%.2e'%(a/64.) for a in (self.I.dchans[0].timestamps[1:4]-offset)],'\t')
			self.message_label.setText(txt+'...')
		else:
			self.message_label.setText('CH1: too few points to display')

		self.curve1.clear()
		self.curve2.clear()
		self.curve3.clear()
		self.curve4.clear()
		self.maxT=0
		self.curve1.setData(self.I.dchans[0].get_xaxis(),self.I.dchans[0].get_yaxis() )
		if self.maxT < self.I.dchans[0].maxT: self.maxT = self.I.dchans[0].maxT 
		if self.I.dchans[0].plot_length==1: #No level changes were detected
			x=self.I.dchans[0].xaxis[0];y=self.I.dchans[0].yaxis[0]
			self.curve1.setData([x,x+self.maxT],[y,y])
		if(self.active_dchannels>1):
			self.curve2.setData(self.I.dchans[1].get_xaxis(),self.I.dchans[1].get_yaxis() )
			if self.maxT < self.I.dchans[1].maxT: self.maxT = self.I.dchans[1].maxT 
			if self.I.dchans[1].plot_length==1: #No level changes were detected
				x=self.I.dchans[1].xaxis[0];y=self.I.dchans[1].yaxis[0]
				self.curve2.setData([x,x+self.maxT],[y,y])
		else:	self.curve2.clear()		
		if(self.active_dchannels>2):
			self.curve3.setData(self.I.dchans[2].get_xaxis(),self.I.dchans[2].get_yaxis())
			if self.maxT < self.I.dchans[2].maxT: self.maxT = self.I.dchans[2].maxT 
			if self.I.dchans[2].plot_length==1: #No level changes were detected
				x=self.I.dchans[2].xaxis[0];y=self.I.dchans[2].yaxis[0]
				self.curve3.setData([x,x+self.dtime*1e6],[y,y])
		else:	self.curve3.clear()
		
		if(self.active_dchannels>3):
			self.curve4.setData(self.I.dchans[3].get_xaxis(),self.I.dchans[3].get_yaxis() )
			if self.maxT < self.I.dchans[3].maxT: self.maxT = self.I.dchans[3].maxT 
			if self.I.dchans[3].plot_length==1: #No level changes were detected
				x=self.I.dchans[3].xaxis[0];y=self.I.dchans[3].yaxis[0]
				self.curve4.setData([x,x+self.maxT],[y,y])
		else:	self.curve4.clear()

		self.plot.setRange(QtCore.QRectF(0, -2, self.maxT, 16)) 
		self.readCursor()		
		data = np.diff(self.I.dchans[0].timestamps)	
		print(np.column_stack([range(len(data)),data]))
		from SEEL.utilityApps import spreadsheet
		info = spreadsheet.AppWindow(self,data=np.column_stack([data]))
		info.show()


	def update(self):
		if self.finished:
			self.timer.stop()
		states = self.I.get_LA_initial_states()
		a,b,c,d,e=states
		self.progressBar.setValue(a)

	def setActiveDigitalChannels(self,val):
		self.active_dchannels = int(val)
		self.samples=800
		self.autodRange()

	def readCursor(self):
		pos=self.vLine.getPos()
		index = int(pos[0]*1e6)/self.I.timebase
		if index > 0 and index < self.I.samples:
			coords="<span style='color: white'>%0.1f uS</span>: "%(self.I.achans[0].xaxis[index])
			for a in range(4):
				if self.channel_states[a]:
					c=self.trace_colors[a]
					coords+="<span style='color: rgb%s'>%0.3fV</span>," %(c, self.I.achans[a].yaxis[index])
			self.coord_label.setText(coords)
		else:
			self.coord_label.setText("")


	def autodRange(self):
		self.plot.setRange(QtCore.QRectF(0, -2, self.maxT, 16)) 

	def set_digital_trigger(self,a):
		self.dtrig = 1 if a else 0

	def set_digital_scope_time(self,val):
		self.autodRange()

	def set_dchan_mode_ch1(self,val):
		self.dchan_modes[0] = val
	def set_dchan_mode_ch2(self,val):
		self.dchan_modes[1] = val
	def set_dchan_mode_ch3(self,val):
		self.dchan_modes[2] = val
	def set_dchan_mode_ch4(self,val):
		self.dchan_modes[3] = val


	def autoSetSamples(self):
		self.samples = self.max_samples_per_channel[self.active_channels]

	def measure_dcycle(self):
		inp = self.timing_input.currentText()
		v=self.I.DutyCycle(inp)
		if(v[0]!=-1):p=100*v[1]
		else: p=0
		self.timing_results.setText('Duty Cycle: %f %%'%(p))

	def measure_interval(self):
		t = self.I.MeasureInterval(self.edge1chan.currentText(),self.edge2chan.currentText(),self.edge1edge.currentText(),self.edge2edge.currentText())
		self.time_interval_label.setText('time: %.2e S'%(t))
		

	def closeEvent(self, event):
		self.timer.stop()
		self.finished=True
		

	def __del__(self):
		self.timer.stop()
		print('bye')

		
if __name__ == "__main__":
	from SEEL import interface
	app = QtGui.QApplication(sys.argv)
	myapp = AppWindow(I=interface.connect())
	myapp.show()
	sys.exit(app.exec_())

