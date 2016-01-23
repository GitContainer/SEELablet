#!/usr/bin/python

"""

::

    This experiment is used to study Half wave rectifiers


"""

from __future__ import print_function
from SEEL.utilitiesClass import utilitiesClass
from SEEL.analyticsClass import analyticsClass

from SEEL.templates import template_xc

import numpy as np
from PyQt4 import QtGui,QtCore
import pyqtgraph as pg
import sys,functools,time

params = {
'image' : 'halfwave.png',
'helpfile': 'http://www.electronics-tutorials.ws/capacitor/cap_8.html',
'name':'Capacitive\nReactance'
}

class AppWindow(QtGui.QMainWindow, template_xc.Ui_MainWindow,utilitiesClass):
    def __init__(self, parent=None,**kwargs):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.I=kwargs.get('I',None)
        
        self.setWindowTitle(self.I.generic_name + ' : '+self.I.H.version_string.decode("utf-8"))
        self.plot1=self.add2DPlot(self.plot_area)
        labelStyle = {'color': 'rgb(255,255,255)', 'font-size': '11pt'}
        self.plot1.setLabel('bottom','Time -->', units='S',**labelStyle)

        self.p2=self.enableRightAxis(self.plot1)

        self.plot1.getAxis('left').setLabel('Vc -->>', color='#ffffff')
        self.plot1.getAxis('right').setLabel('I -->>', units='A', color='#00ffff')

        self.I.set_gain('CH1',1)
        self.I.set_gain('CH2',1)
        self.plot1.setYRange(-8.5,8.5)

        self.p2.setYRange(-8.5/self.resistance.value(),8.5/self.resistance.value())


        self.CC = analyticsClass()
        self.I.configure_trigger(0,'CH1',0)
        self.tg=20
        self.samples = 2000
        self.setTimeGap(20)
        self.timer = QtCore.QTimer()

        self.curveCH1 = self.addCurve(self.plot1,'VC(CH1-CH2)',(255,255,255))
        self.curveCH2 = self.addCurve(self.p2,'Current',(0,255,255))
        self.WidgetLayout.setAlignment(QtCore.Qt.AlignLeft)

        a1={'TITLE':'Wave 1','MIN':10,'MAX':5000,'FUNC':self.I.set_sine1,'TYPE':'dial','UNITS':'Hz','TOOLTIP':'Frequency of waveform generator #1'}
        self.fdial = self.dialIcon(**a1)
        self.WidgetLayout.addWidget(self.fdial)
        self.timer.singleShot(100,self.run)
        self.resultsTable.setRowCount(50)
        self.resultsTable.setColumnCount(4)
        self.resultsTable.setHorizontalHeaderLabels(['F','Vc','I (mA)','Xc = Vc/I'])
        self.acquireParams = False
        self.currentRow=0
        
        self.plotAButton.setText('F vs Xc')
        self.plotBButton.setText('F vs 1/Xc')

    def setTimeGap(self,tg):
        self.tg = tg
        self.plot1.setLimits(yMax=8,yMin=-8,xMin=0,xMax=self.samples*self.tg*1e-6)
        self.p2.setLimits(yMax=8/self.resistance.value(),yMin=-8/self.resistance.value(),xMin=0,xMax=self.samples*self.tg*1e-6)


    def launchOutputs(self):
        if self.I:
            from SEEL.controls import outputs
            inst = outputs.AppWindow(self,I=self.I)
            inst.show()
            size = inst.geometry()
            inst.setGeometry(300, 50,size.width(), size.height())
        else:
            print (self.setWindowTitle('Device Not Connected!'))


    def fit(self):
        print ("Adding...")
        self.acquireParams = True
        
    def run(self):
        self.I.configure_trigger(0,'CH1',0,resolution=10,prescaler=3)
        self.I.capture_traces(2,self.samples,self.tg)
        self.timer.singleShot(self.samples*self.I.timebase*1e-3+50,self.plotData)

    def plotData(self): 
        while(not self.I.oscilloscope_progress()[0]):
            time.sleep(0.1);n=0
            print (self.I.timebase,'correction required',n)
            n+=1
            if n>10:
                self.timer.singleShot(100,self.run)
                return
        self.I.__fetch_channel__(1)
        self.I.__fetch_channel__(2)
        T = self.I.achans[0].get_xaxis()*1e-6
        VCH1 = self.I.achans[0].get_yaxis()
        VCH2 = self.I.achans[1].get_yaxis()
        I = VCH2/self.resistance.value()
        VC = VCH1-VCH2
        self.curveCH1.setData(T,VC,connect='finite')
        self.curveCH2.setData(T,I,connect='finite')
        if self.acquireParams:
            pars1 = self.CC.sineFit(T,VC)
            pars2 = self.CC.sineFit(T,I)#,freq=self.frq)
            if pars1 and pars2:
                a1,f1,o1,p1 = pars1
                a2,f2,o2,p2 = pars2
                f1=f1*1e-6
                f2=f2*1e-6
                if (a2 and a1) and (abs(f2-self.I.sine1freq)<10) and (abs(f1-self.I.sine1freq)<10):
                    #self.msg.setText("Set F:%.1f\tFitted F:%.1f"%(frq,f1))
                    p2=(p2)
                    p1=(p1)
                    dp=(p2-p1)-360
                    if dp<-360:dp+=360
                    item = QtGui.QTableWidgetItem();item.setText('%.3f'%(self.I.sine1freq));self.resultsTable.setItem(self.currentRow, 0, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                    item = QtGui.QTableWidgetItem();item.setText('%.3f'%(a1));self.resultsTable.setItem(self.currentRow, 1, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                    item = QtGui.QTableWidgetItem();item.setText('%.3f'%(a2*1e3));self.resultsTable.setItem(self.currentRow, 2, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                    item = QtGui.QTableWidgetItem();item.setText('%.3f'%(a1/a2));self.resultsTable.setItem(self.currentRow, 3, item);item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
                    self.currentRow+=1
                    print ('F: %.2f,%.2f\tA: %.2f,%.2f\tP: %.1f,%.1f'%(f1,f2,a1,a2,p1,p2))
                    print ('Xc*F %.3f'%(f2*a1/a2))
                else:
                    self.displayDialog("Fit Failed. Please check parameters\nor change timescale")
            else:
                self.displayDialog("Fit Failed. Please check parameters\nor change timescale")
            self.acquireParams = False
        self.timer.singleShot(100,self.run)

       
    def plotA(self):
        F,XC = self.fetchColumns(self.resultsTable,0,3)
        self.newPlot(F,XC,title = "F vs XC: ",xLabel = 'F',yLabel='XC')

    def plotB(self):
        F,XC = self.fetchColumns(self.resultsTable,0,3)
        self.newPlot(F,1./np.array(XC),title = "F vs 1/XC: ",xLabel = 'F',yLabel='1/XC')        



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

