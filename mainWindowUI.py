# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow/mainwindow.ui'
#
# Created: Wed May 18 13:44:17 2016
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.resize(979, 600)
        MainWindow.setStyleSheet(_fromUtf8("background:blue;"))
        self.gridLayout = QtGui.QGridLayout(MainWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(MainWindow)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.pic = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic.sizePolicy().hasHeightForWidth())
        self.pic.setSizePolicy(sizePolicy)
        self.pic.setStyleSheet(_fromUtf8("image:url(/home/sblinux/Pictures/Bulls.jpg);\n"
"background:white;\n"
"background-repeat:repat;\n"
""))
        self.pic.setObjectName(_fromUtf8("pic"))
        self.widget_2 = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.widget_3 = QtGui.QWidget(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.widget_3)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_4 = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.xboxLabelShoulder = QtGui.QLineEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.xboxLabelShoulder.sizePolicy().hasHeightForWidth())
        self.xboxLabelShoulder.setSizePolicy(sizePolicy)
        self.xboxLabelShoulder.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.xboxLabelShoulder.setObjectName(_fromUtf8("xboxLabelShoulder"))
        self.gridLayout_4.addWidget(self.xboxLabelShoulder, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_4.addWidget(self.label_5, 5, 0, 1, 1)
        self.xboxLabelElbow = QtGui.QLineEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.xboxLabelElbow.sizePolicy().hasHeightForWidth())
        self.xboxLabelElbow.setSizePolicy(sizePolicy)
        self.xboxLabelElbow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.xboxLabelElbow.setObjectName(_fromUtf8("xboxLabelElbow"))
        self.gridLayout_4.addWidget(self.xboxLabelElbow, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_4.addWidget(self.label_9, 3, 2, 1, 1)
        self.xboxLabelLeftMotor = QtGui.QLineEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.xboxLabelLeftMotor.sizePolicy().hasHeightForWidth())
        self.xboxLabelLeftMotor.setSizePolicy(sizePolicy)
        self.xboxLabelLeftMotor.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.xboxLabelLeftMotor.setObjectName(_fromUtf8("xboxLabelLeftMotor"))
        self.gridLayout_4.addWidget(self.xboxLabelLeftMotor, 2, 3, 1, 1)
        self.xboxLabelBase = QtGui.QLineEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.xboxLabelBase.sizePolicy().hasHeightForWidth())
        self.xboxLabelBase.setSizePolicy(sizePolicy)
        self.xboxLabelBase.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.xboxLabelBase.setObjectName(_fromUtf8("xboxLabelBase"))
        self.gridLayout_4.addWidget(self.xboxLabelBase, 4, 1, 1, 1)
        self.xboxLabelClawState = QtGui.QLineEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.xboxLabelClawState.sizePolicy().hasHeightForWidth())
        self.xboxLabelClawState.setSizePolicy(sizePolicy)
        self.xboxLabelClawState.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.xboxLabelClawState.setObjectName(_fromUtf8("xboxLabelClawState"))
        self.gridLayout_4.addWidget(self.xboxLabelClawState, 1, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.roll = QtGui.QLineEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.roll.sizePolicy().hasHeightForWidth())
        self.roll.setSizePolicy(sizePolicy)
        self.roll.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.roll.setObjectName(_fromUtf8("roll"))
        self.gridLayout_4.addWidget(self.roll, 5, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 2, 2, 1, 1)
        self.xboxLabelRightMotor = QtGui.QLineEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.xboxLabelRightMotor.sizePolicy().hasHeightForWidth())
        self.xboxLabelRightMotor.setSizePolicy(sizePolicy)
        self.xboxLabelRightMotor.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.xboxLabelRightMotor.setObjectName(_fromUtf8("xboxLabelRightMotor"))
        self.gridLayout_4.addWidget(self.xboxLabelRightMotor, 3, 3, 1, 1)
        self.xboxLabelManipulator = QtGui.QLineEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.xboxLabelManipulator.sizePolicy().hasHeightForWidth())
        self.xboxLabelManipulator.setSizePolicy(sizePolicy)
        self.xboxLabelManipulator.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.xboxLabelManipulator.setObjectName(_fromUtf8("xboxLabelManipulator"))
        self.gridLayout_4.addWidget(self.xboxLabelManipulator, 5, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 4)
        self.metaInformation = QtGui.QLineEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.metaInformation.sizePolicy().hasHeightForWidth())
        self.metaInformation.setSizePolicy(sizePolicy)
        self.metaInformation.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.metaInformation.setObjectName(_fromUtf8("metaInformation"))
        self.gridLayout_4.addWidget(self.metaInformation, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_4.addWidget(self.label_10, 4, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_4.addWidget(self.label_11, 5, 2, 1, 1)
        self.pitch = QtGui.QLineEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pitch.sizePolicy().hasHeightForWidth())
        self.pitch.setSizePolicy(sizePolicy)
        self.pitch.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pitch.setObjectName(_fromUtf8("pitch"))
        self.gridLayout_4.addWidget(self.pitch, 4, 3, 1, 1)
        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 1)
        self.widget = QtGui.QWidget(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.startButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.gridLayout_3.addWidget(self.startButton, 0, 0, 1, 1)
        self.stopButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.gridLayout_3.addWidget(self.stopButton, 0, 1, 1, 1)
        self.resetButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.gridLayout_3.addWidget(self.resetButton, 1, 0, 1, 1)
        self.cameraLabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.cameraLabel.setFont(font)
        self.cameraLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.cameraLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraLabel.setObjectName(_fromUtf8("cameraLabel"))
        self.gridLayout_3.addWidget(self.cameraLabel, 2, 0, 1, 1)
        self.comboCameraSelect = QtGui.QComboBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboCameraSelect.sizePolicy().hasHeightForWidth())
        self.comboCameraSelect.setSizePolicy(sizePolicy)
        self.comboCameraSelect.setObjectName(_fromUtf8("comboCameraSelect"))
        self.gridLayout_3.addWidget(self.comboCameraSelect, 3, 0, 1, 1)
        self.FPSLabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.FPSLabel.setFont(font)
        self.FPSLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.FPSLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FPSLabel.setObjectName(_fromUtf8("FPSLabel"))
        self.gridLayout_3.addWidget(self.FPSLabel, 2, 1, 1, 1)
        self.comboFPSSelect = QtGui.QComboBox(self.widget)
        self.comboFPSSelect.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboFPSSelect.sizePolicy().hasHeightForWidth())
        self.comboFPSSelect.setSizePolicy(sizePolicy)
        self.comboFPSSelect.setObjectName(_fromUtf8("comboFPSSelect"))
        self.gridLayout_3.addWidget(self.comboFPSSelect, 3, 1, 1, 1)
        self.detectionButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detectionButton.sizePolicy().hasHeightForWidth())
        self.detectionButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.detectionButton.setFont(font)
        self.detectionButton.setObjectName(_fromUtf8("detectionButton"))
        self.gridLayout_3.addWidget(self.detectionButton, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "Base", None))
        self.label.setText(_translate("MainWindow", "Temperature", None))
        self.label_5.setText(_translate("MainWindow", "Manipulator", None))
        self.label_9.setText(_translate("MainWindow", "Right Motor", None))
        self.label_7.setText(_translate("MainWindow", "Claw State", None))
        self.label_2.setText(_translate("MainWindow", "Shoulder", None))
        self.label_8.setText(_translate("MainWindow", "Left Motor", None))
        self.label_3.setText(_translate("MainWindow", "Elbow", None))
        self.label_6.setText(_translate("MainWindow", "Rover Data", None))
        self.label_10.setText(_translate("MainWindow", "Pitch", None))
        self.label_11.setText(_translate("MainWindow", "Roll", None))
        self.startButton.setText(_translate("MainWindow", "Start Cam", None))
        self.stopButton.setText(_translate("MainWindow", "Stop Cam", None))
        self.resetButton.setText(_translate("MainWindow", "Reset", None))
        self.cameraLabel.setText(_translate("MainWindow", "Camera", None))
        self.FPSLabel.setText(_translate("MainWindow", "FPS", None))
        self.detectionButton.setText(_translate("MainWindow", "Detection", None))

