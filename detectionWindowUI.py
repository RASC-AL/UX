# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetectionWindow/detectionwindow.ui'
#
# Created: Wed May 18 23:54:11 2016
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
        self.VideoWidget.setStyleSheet(_fromUtf8("image:url(/home/ieee-2/Pictures/Bulls.jpg);\n"
"background:white;\n"
""))
        self.VideoWidget.setObjectName(_fromUtf8("VideoWidget"))
        self.GPSWidget = QtGui.QWidget(self.splitter_2)
        self.GPSWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.GPSWidget.setStyleSheet(_fromUtf8("background:white;"))
        self.GPSWidget.setObjectName(_fromUtf8("GPSWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.GPSWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.GPSWebView = QtWebKit.QWebView(self.GPSWidget)
        self.GPSWebView.setProperty("url", QtCore.QUrl(_fromUtf8("about:blank")))
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
        DetectionWindow.setWindowTitle(_translate("DetectionWindow", "DetectionWindow", None))

from PyQt4 import QtWebKit
