#!/usr/bin/python
'''
Output Peripheral control for the vLabtool - version 0.
'''

from __future__ import print_function
import os
os.environ['QT_API'] = 'pyqt'
import sip
sip.setapi("QString", 2)
sip.setapi("QVariant", 2)

from PyQt4 import QtCore, QtGui
from SEEL.templates import aboutDevice
import sys,os,time



class AppWindow(QtGui.QMainWindow, aboutDevice.Ui_MainWindow):
	def __init__(self, parent=None,**kwargs):
		super(AppWindow, self).__init__(parent)
		self.setupUi(self)
		self.I=kwargs.get('I',None)

		self.setWindowTitle('About Device : '+self.I.hexid)
		self.table.setColumnWidth(0,200)
		if self.I.connected :
			xpos=0;ypos=0
			for a in self.I.aboutArray:
				xpos=0
				for b in a:
					item = QtGui.QTableWidgetItem()
					self.table.setItem(ypos,xpos,item)
					item.setText('%s'%b)
					xpos+=1
				ypos+=1

	def __del__(self):
		print ('bye')
                
if __name__ == "__main__":
    from SEEL import interface
    app = QtGui.QApplication(sys.argv)
    myapp = AppWindow(I=interface.connect())
    myapp.show()
    sys.exit(app.exec_())
