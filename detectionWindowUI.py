# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetectionWindow/detectionwindow.ui'
#
# Created: Wed May 18 13:42:23 2016
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DetectionWindow(object):
    def setupUi(self, DetectionWindow):
        DetectionWindow.setObjectName(_fromUtf8("DetectionWindow"))
        DetectionWindow.resize(781, 596)
        DetectionWindow.setStyleSheet(_fromUtf8("background:blue;\n"
""))
        self.verticalLayout = QtGui.QVBoxLayout(DetectionWindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(DetectionWindow)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget_3 = QtGui.QWidget(self.splitter)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter_2 = QtGui.QSplitter(self.widget_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.VideoWidget = QtGui.QWidget(self.splitter_2)
        self.VideoWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.VideoWidget.setStyleSheet(_fromUtf8("image:url(/home/sblinux/Pictures/Bulls.jpg);\n"
"background:white;\n"
"background-repeat:repat;"))
        self.VideoWidget.setObjectName(_fromUtf8("VideoWidget"))
        self.GPSWidget = QtGui.QWidget(self.splitter_2)
        self.GPSWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.GPSWidget.setStyleSheet(_fromUtf8("background:white;"))
        self.GPSWidget.setObjectName(_fromUtf8("GPSWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.GPSWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.GPSWebView = QtWebKit.QWebView(self.GPSWidget)
        self.GPSWebView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.GPSWebView.setObjectName(_fromUtf8("GPSWebView"))
        self.verticalLayout_3.addWidget(self.GPSWebView)
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.ControlsWidget = QtGui.QWidget(self.splitter)
        self.ControlsWidget.setMinimumSize(QtCore.QSize(0, 200))
        self.ControlsWidget.setObjectName(_fromUtf8("ControlsWidget"))
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(DetectionWindow)
        QtCore.QMetaObject.connectSlotsByName(DetectionWindow)

    def retranslateUi(self, DetectionWindow):
        DetectionWindow.setWindowTitle(QtGui.QApplication.translate("DetectionWindow", "DetectionWindow", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
