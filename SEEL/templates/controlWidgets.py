# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlWidgets.ui'
#
# Created: Sat Dec 26 16:56:51 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(720, 580)
        MainWindow.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
"\n"
"QFrame.PeripheralCollection{\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border: 1px solid black;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #6af, stop: 0.1 #689);\n"
"}\n"
"QFrame.PeripheralCollection QLabel {\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QFrame.PeripheralCollectionInner {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #abe, stop: 0.7 #aba);\n"
"border: none;\n"
"border-top: 1px solid black;\n"
"}\n"
"\n"
"QFrame.PeripheralCollectionInner QLabel{\n"
"color: black;\n"
"}\n"
"\n"
"QWidget.PeripheralCollectionInner {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #abe, stop: 0.7 #aba);\n"
"border: none;\n"
"border-top: 1px solid black;\n"
"}\n"
"\n"
"\n"
"\n"
"QWidget.PeripheralCollectionInner {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #abe, stop: 0.7 #aba);\n"
"border: none;\n"
"border-top: 1px solid black;\n"
"}\n"
"\n"
"QWidget.PeripheralCollectionInner QLabel{\n"
"color: black;\n"
"}\n"
"\n"
"#SCF2,#SCF1\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #abe, stop: 0.7 #aba);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea_4 = QtGui.QScrollArea(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setMinimumSize(QtCore.QSize(350, 0))
        self.scrollArea_4.setMaximumSize(QtCore.QSize(370, 16777215))
        self.scrollArea_4.setStyleSheet(_fromUtf8(""))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea_4.setObjectName(_fromUtf8("scrollArea_4"))
        self.SCF1 = QtGui.QWidget()
        self.SCF1.setGeometry(QtCore.QRect(0, 0, 353, 574))
        self.SCF1.setStyleSheet(_fromUtf8(""))
        self.SCF1.setObjectName(_fromUtf8("SCF1"))
        self.gridLayout_6 = QtGui.QGridLayout(self.SCF1)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.frame_6 = QtGui.QFrame(self.SCF1)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_8 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setContentsMargins(0, 5, 0, 0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.WidgetLayout = QtGui.QGridLayout()
        self.WidgetLayout.setMargin(5)
        self.WidgetLayout.setSpacing(7)
        self.WidgetLayout.setObjectName(_fromUtf8("WidgetLayout"))
        self.gridLayout_8.addLayout(self.WidgetLayout, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_6, 0, 0, 1, 1)
        self.scrollArea_4.setWidget(self.SCF1)
        self.gridLayout.addWidget(self.scrollArea_4, 0, 0, 3, 1)
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.Frame_2 = QtGui.QFrame(self.frame_3)
        self.Frame_2.setProperty("PeripheralCollectionInner", _fromUtf8(""))
        self.Frame_2.setObjectName(_fromUtf8("Frame_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Frame_2)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_10 = QtGui.QLabel(self.Frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.Frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.Frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.PCS_LABEL = QtGui.QLabel(self.Frame_2)
        self.PCS_LABEL.setObjectName(_fromUtf8("PCS_LABEL"))
        self.gridLayout_2.addWidget(self.PCS_LABEL, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.Frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.PVS3_LABEL = QtGui.QLabel(self.Frame_2)
        self.PVS3_LABEL.setObjectName(_fromUtf8("PVS3_LABEL"))
        self.gridLayout_2.addWidget(self.PVS3_LABEL, 2, 1, 1, 1)
        self.PVS2_LABEL = QtGui.QLabel(self.Frame_2)
        self.PVS2_LABEL.setObjectName(_fromUtf8("PVS2_LABEL"))
        self.gridLayout_2.addWidget(self.PVS2_LABEL, 1, 1, 1, 1)
        self.PVS1_LABEL = QtGui.QLabel(self.Frame_2)
        self.PVS1_LABEL.setObjectName(_fromUtf8("PVS1_LABEL"))
        self.gridLayout_2.addWidget(self.PVS1_LABEL, 0, 1, 1, 1)
        self.PVS1BOX = QtGui.QDoubleSpinBox(self.Frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PVS1BOX.sizePolicy().hasHeightForWidth())
        self.PVS1BOX.setSizePolicy(sizePolicy)
        self.PVS1BOX.setDecimals(3)
        self.PVS1BOX.setMinimum(-5.0)
        self.PVS1BOX.setMaximum(5.0)
        self.PVS1BOX.setSingleStep(0.1)
        self.PVS1BOX.setObjectName(_fromUtf8("PVS1BOX"))
        self.gridLayout_2.addWidget(self.PVS1BOX, 0, 2, 1, 1)
        self.PVS2BOX = QtGui.QDoubleSpinBox(self.Frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PVS2BOX.sizePolicy().hasHeightForWidth())
        self.PVS2BOX.setSizePolicy(sizePolicy)
        self.PVS2BOX.setDecimals(3)
        self.PVS2BOX.setMinimum(-3.3)
        self.PVS2BOX.setMaximum(3.3)
        self.PVS2BOX.setSingleStep(0.1)
        self.PVS2BOX.setObjectName(_fromUtf8("PVS2BOX"))
        self.gridLayout_2.addWidget(self.PVS2BOX, 1, 2, 1, 1)
        self.PVS3BOX = QtGui.QDoubleSpinBox(self.Frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PVS3BOX.sizePolicy().hasHeightForWidth())
        self.PVS3BOX.setSizePolicy(sizePolicy)
        self.PVS3BOX.setDecimals(3)
        self.PVS3BOX.setMaximum(3.3)
        self.PVS3BOX.setSingleStep(0.1)
        self.PVS3BOX.setObjectName(_fromUtf8("PVS3BOX"))
        self.gridLayout_2.addWidget(self.PVS3BOX, 2, 2, 1, 1)
        self.PCSBOX = QtGui.QDoubleSpinBox(self.Frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PCSBOX.sizePolicy().hasHeightForWidth())
        self.PCSBOX.setSizePolicy(sizePolicy)
        self.PCSBOX.setDecimals(3)
        self.PCSBOX.setMaximum(3.3)
        self.PCSBOX.setSingleStep(0.1)
        self.PCSBOX.setObjectName(_fromUtf8("PCSBOX"))
        self.gridLayout_2.addWidget(self.PCSBOX, 3, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.Frame_2)
        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(self.frame_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.Frame_3 = QtGui.QFrame(self.frame_4)
        self.Frame_3.setProperty("PeripheralCollectionInner", _fromUtf8(""))
        self.Frame_3.setObjectName(_fromUtf8("Frame_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.Frame_3)
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_17 = QtGui.QLabel(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)
        self.WAVE1_FREQ = QtGui.QLabel(self.Frame_3)
        self.WAVE1_FREQ.setObjectName(_fromUtf8("WAVE1_FREQ"))
        self.gridLayout_3.addWidget(self.WAVE1_FREQ, 0, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_3.addWidget(self.pushButton_4, 2, 2, 2, 1)
        self.SINE2BOX = QtGui.QDoubleSpinBox(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SINE2BOX.sizePolicy().hasHeightForWidth())
        self.SINE2BOX.setSizePolicy(sizePolicy)
        self.SINE2BOX.setMinimum(5.0)
        self.SINE2BOX.setMaximum(5000.0)
        self.SINE2BOX.setProperty("value", 500.0)
        self.SINE2BOX.setObjectName(_fromUtf8("SINE2BOX"))
        self.gridLayout_3.addWidget(self.SINE2BOX, 1, 2, 1, 1)
        self.WAVE2_FREQ = QtGui.QLabel(self.Frame_3)
        self.WAVE2_FREQ.setObjectName(_fromUtf8("WAVE2_FREQ"))
        self.gridLayout_3.addWidget(self.WAVE2_FREQ, 1, 1, 1, 1)
        self.SINE1BOX = QtGui.QDoubleSpinBox(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SINE1BOX.sizePolicy().hasHeightForWidth())
        self.SINE1BOX.setSizePolicy(sizePolicy)
        self.SINE1BOX.setMinimum(5.0)
        self.SINE1BOX.setMaximum(5000.0)
        self.SINE1BOX.setProperty("value", 500.0)
        self.SINE1BOX.setObjectName(_fromUtf8("SINE1BOX"))
        self.gridLayout_3.addWidget(self.SINE1BOX, 0, 2, 1, 1)
        self.SINEPHASE = QtGui.QDoubleSpinBox(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SINEPHASE.sizePolicy().hasHeightForWidth())
        self.SINEPHASE.setSizePolicy(sizePolicy)
        self.SINEPHASE.setDecimals(1)
        self.SINEPHASE.setMaximum(359.0)
        self.SINEPHASE.setObjectName(_fromUtf8("SINEPHASE"))
        self.gridLayout_3.addWidget(self.SINEPHASE, 3, 1, 1, 1)
        self.label_29 = QtGui.QLabel(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_3.addWidget(self.label_29, 1, 0, 1, 1)
        self.label_30 = QtGui.QLabel(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_3.addWidget(self.label_30, 3, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.Frame_3)
        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.frame_5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.Frame_4 = QtGui.QFrame(self.frame_5)
        self.Frame_4.setProperty("PeripheralCollectionInner", _fromUtf8(""))
        self.Frame_4.setObjectName(_fromUtf8("Frame_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.Frame_4)
        self.gridLayout_4.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.pushButton_6 = QtGui.QPushButton(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_4.addWidget(self.pushButton_6, 6, 2, 1, 1)
        self.label_20 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_4.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_35 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout_4.addWidget(self.label_35, 4, 0, 1, 1)
        self.SQR3P = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR3P.sizePolicy().hasHeightForWidth())
        self.SQR3P.setSizePolicy(sizePolicy)
        self.SQR3P.setDecimals(3)
        self.SQR3P.setMaximum(360.0)
        self.SQR3P.setSingleStep(1.0)
        self.SQR3P.setProperty("value", 0.0)
        self.SQR3P.setObjectName(_fromUtf8("SQR3P"))
        self.gridLayout_4.addWidget(self.SQR3P, 3, 1, 1, 1)
        self.label_34 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_4.addWidget(self.label_34, 3, 0, 1, 1)
        self.SQR4P = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR4P.sizePolicy().hasHeightForWidth())
        self.SQR4P.setSizePolicy(sizePolicy)
        self.SQR4P.setDecimals(3)
        self.SQR4P.setMaximum(360.0)
        self.SQR4P.setSingleStep(1.0)
        self.SQR4P.setProperty("value", 0.0)
        self.SQR4P.setObjectName(_fromUtf8("SQR4P"))
        self.gridLayout_4.addWidget(self.SQR4P, 4, 1, 1, 1)
        self.SQR1DC = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR1DC.sizePolicy().hasHeightForWidth())
        self.SQR1DC.setSizePolicy(sizePolicy)
        self.SQR1DC.setDecimals(3)
        self.SQR1DC.setMaximum(1.0)
        self.SQR1DC.setSingleStep(0.1)
        self.SQR1DC.setProperty("value", 0.5)
        self.SQR1DC.setObjectName(_fromUtf8("SQR1DC"))
        self.gridLayout_4.addWidget(self.SQR1DC, 1, 2, 1, 1)
        self.label_33 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_4.addWidget(self.label_33, 2, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_4.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_4.addWidget(self.label_21, 0, 2, 1, 1)
        self.label_19 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)
        self.SQR2P = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR2P.sizePolicy().hasHeightForWidth())
        self.SQR2P.setSizePolicy(sizePolicy)
        self.SQR2P.setDecimals(3)
        self.SQR2P.setMaximum(360.0)
        self.SQR2P.setSingleStep(1.0)
        self.SQR2P.setProperty("value", 0.0)
        self.SQR2P.setObjectName(_fromUtf8("SQR2P"))
        self.gridLayout_4.addWidget(self.SQR2P, 2, 1, 1, 1)
        self.SQR2DC = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR2DC.sizePolicy().hasHeightForWidth())
        self.SQR2DC.setSizePolicy(sizePolicy)
        self.SQR2DC.setDecimals(3)
        self.SQR2DC.setMaximum(1.0)
        self.SQR2DC.setSingleStep(0.1)
        self.SQR2DC.setProperty("value", 0.5)
        self.SQR2DC.setObjectName(_fromUtf8("SQR2DC"))
        self.gridLayout_4.addWidget(self.SQR2DC, 2, 2, 1, 1)
        self.SQR4DC = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR4DC.sizePolicy().hasHeightForWidth())
        self.SQR4DC.setSizePolicy(sizePolicy)
        self.SQR4DC.setDecimals(3)
        self.SQR4DC.setMaximum(1.0)
        self.SQR4DC.setSingleStep(0.1)
        self.SQR4DC.setProperty("value", 0.5)
        self.SQR4DC.setObjectName(_fromUtf8("SQR4DC"))
        self.gridLayout_4.addWidget(self.SQR4DC, 4, 2, 1, 1)
        self.SQR3DC = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR3DC.sizePolicy().hasHeightForWidth())
        self.SQR3DC.setSizePolicy(sizePolicy)
        self.SQR3DC.setDecimals(3)
        self.SQR3DC.setMaximum(1.0)
        self.SQR3DC.setSingleStep(0.1)
        self.SQR3DC.setProperty("value", 0.5)
        self.SQR3DC.setObjectName(_fromUtf8("SQR3DC"))
        self.gridLayout_4.addWidget(self.SQR3DC, 3, 2, 1, 1)
        self.line = QtGui.QFrame(self.Frame_4)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_4.addWidget(self.line, 5, 0, 1, 3)
        self.label = QtGui.QLabel(self.Frame_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 6, 0, 1, 1)
        self.SQRSF = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQRSF.sizePolicy().hasHeightForWidth())
        self.SQRSF.setSizePolicy(sizePolicy)
        self.SQRSF.setDecimals(3)
        self.SQRSF.setMinimum(100.0)
        self.SQRSF.setMaximum(1000000.0)
        self.SQRSF.setSingleStep(10.0)
        self.SQRSF.setProperty("value", 1000.0)
        self.SQRSF.setObjectName(_fromUtf8("SQRSF"))
        self.gridLayout_4.addWidget(self.SQRSF, 6, 1, 1, 1)
        self.label_22 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_4.addWidget(self.label_22, 1, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.Frame_4)
        self.gridLayout.addWidget(self.frame_5, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.PVS1BOX, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), MainWindow.setPVS1)
        QtCore.QObject.connect(self.PVS2BOX, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), MainWindow.setPVS2)
        QtCore.QObject.connect(self.PVS3BOX, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), MainWindow.setPVS3)
        QtCore.QObject.connect(self.PCSBOX, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), MainWindow.setPCS)
        QtCore.QObject.connect(self.SINE1BOX, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), MainWindow.setSINE1)
        QtCore.QObject.connect(self.SINE2BOX, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), MainWindow.setSINE2)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.setSinePhase)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.setSQRS)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.SCF1.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.frame_3.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.label_2.setText(_translate("MainWindow", " IV Sources", None))
        self.Frame_2.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.label_10.setText(_translate("MainWindow", "PVS3", None))
        self.label_12.setText(_translate("MainWindow", "PVS2 ", None))
        self.label_11.setText(_translate("MainWindow", "PVS1 ", None))
        self.PCS_LABEL.setText(_translate("MainWindow", "0-3.3mA", None))
        self.label_9.setText(_translate("MainWindow", "PCS", None))
        self.PVS3_LABEL.setText(_translate("MainWindow", "0 - 3.3V", None))
        self.PVS2_LABEL.setText(_translate("MainWindow", "-3.3 to 3.3V", None))
        self.PVS1_LABEL.setText(_translate("MainWindow", "-5 to 5V", None))
        self.frame_4.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.label_3.setText(_translate("MainWindow", " Waveform Generators", None))
        self.Frame_3.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.label_17.setText(_translate("MainWindow", "Wave 1", None))
        self.WAVE1_FREQ.setText(_translate("MainWindow", "10Hz to 5KHz", None))
        self.pushButton_4.setText(_translate("MainWindow", "SET PHASE", None))
        self.WAVE2_FREQ.setText(_translate("MainWindow", "10Hz to 5KHz", None))
        self.label_29.setText(_translate("MainWindow", "Wave 2", None))
        self.label_30.setText(_translate("MainWindow", "phase", None))
        self.frame_5.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.label_4.setText(_translate("MainWindow", " PWM Output ( sine waves will be disabled )", None))
        self.Frame_4.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.pushButton_6.setText(_translate("MainWindow", "SET", None))
        self.label_20.setText(_translate("MainWindow", "Phase", None))
        self.label_35.setText(_translate("MainWindow", "SQR4", None))
        self.label_34.setText(_translate("MainWindow", "SQR3", None))
        self.label_33.setText(_translate("MainWindow", "SQR2", None))
        self.label_18.setText(_translate("MainWindow", "SQR1", None))
        self.label_21.setText(_translate("MainWindow", "Duty Cycle", None))
        self.label_19.setText(_translate("MainWindow", "Output", None))
        self.label.setText(_translate("MainWindow", "Frequency", None))
        self.label_22.setText(_translate("MainWindow", "0", None))

