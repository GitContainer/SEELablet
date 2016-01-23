#!/usr/bin/python

"""

::

    This experiment is used to study Full wave rectifiers


"""

from __future__ import print_function
from SEEL.utilitiesClass import utilitiesClass
from SEEL.analyticsClass import analyticsClass

from SEEL.templates import template_graph

import numpy as np
from PyQt4 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools

params = {
'image' : 'fullwave.png',
'helpfile': 'http://hyperphysics.phy-astr.gsu.edu/hbase/electronic/rectifiers.html',
'name':'Full Wave\nRectifier'
}

class AppWindow(QtGui.QMainWindow, template_graph.Ui_MainWindow,utilitiesClass):
    def __init__(self, parent=None,**kwargs):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.I=kwargs.get('I',None)
        
        self.setWindowTitle(self.I.generic_name + ' : '+self.I.H.version_string.decode("utf-8"))
        self.plot1=self.add2DPlot(self.plot_area)
        labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
        self.plot1.setLabel('left','Voltage -->', units='V',**labelStyle)
        self.plot1.setLabel('bottom','Time -->', units='S',**labelStyle)
        self.plot1.setYRange(-3.3,3.3)
        self.plot1.setLimits(yMax=3.3,yMin=-3.3,xMin=0)
        self.I.set_gain('CH1',2)
        self.I.set_gain('CH2',2)
        self.I.configure_trigger(0,'CH1',0)
        self.tg=2
        self.timer = QtCore.QTimer()

        self.curveCH1 = self.addCurve(self.plot1,'INPUT 1(CH1)',(255,255,255))
        self.curveCH2 = self.addCurve(self.plot1,'INPUT 2(CH2)',(0,255,255))
        self.curveCH3 = self.addCurve(self.plot1,'OUTPUT(CH3)',(0,255,0))

        self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)        

        a1={'TITLE':'Wave 1','MIN':10,'MAX':5000,'FUNC':self.setSineWaves,'TYPE':'dial','UNITS':'Hz','TOOLTIP':'Frequency of waveform generator #1','LINK':self.updateLabels}
        self.WidgetLayout.addWidget(self.dialIcon(**a1))

        self.sineSection = self.sineWidget(self.I)
        self.WidgetLayout.addWidget(self.sineSection)
        
        self.timer.singleShot(100,self.run)
        
        
    def run(self):
        self.I.capture_traces(3,2000,self.tg)
        self.timer.singleShot(5000*self.I.timebase*1e-3+10,self.plotData)

    def plotData(self): 
        while(not self.I.oscilloscope_progress()[0]):
            time.sleep(0.1)
            print (self.timebase,'correction required',n)
            n+=1
            if n>10:
                self.timer.singleShot(100,self.run)
                return
        self.I.__fetch_channel__(1)
        self.I.__fetch_channel__(2)
        self.I.__fetch_channel__(3)
        self.curveCH1.setData(self.I.achans[0].get_xaxis()*1e-6,self.I.achans[0].get_yaxis(),connect='finite')
        self.curveCH2.setData(self.I.achans[1].get_xaxis()*1e-6,self.I.achans[1].get_yaxis(),connect='finite')
        self.curveCH3.setData(self.I.achans[2].get_xaxis()*1e-6,self.I.achans[2].get_yaxis(),connect='finite')
        self.timer.singleShot(100,self.run)

    def setSineWaves(self,freq):
        return self.I.set_sine_phase(freq,180)

    def updateLabels(self,value,units=''):
        self.sineSection.WAVE1_FREQ.setText('%.3f %s '%(value,units))
        self.sineSection.WAVE2_FREQ.setText('%.3f %s '%(value,units))
        self.sineSection.SINEPHASE.setValue(180)


    def setTimebase(self,T):
        self.tgs = [0.5,1,2,4,6,8,10,25,50,100]
        self.tg = self.tgs[T]
        self.tgLabel.setText(str(5000*self.tg*1e-3)+'mS')
        
    def closeEvent(self, event):
        self.timer.stop()
        self.finished=True
        

    def __del__(self):
        self.timer.stop()
        print ('bye')

if __name__ == "__main__":
    from SEEL import interface
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=interface.connect())
    myapp.show()
    sys.exit(app.exec_())

