import sys
from PyQt4 import QtGui, QtCore
from detectionWindowUI import Ui_DetectionWindow as UI

class detectionWindow(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = UI()
        self.ui.setupUi(self)
        self.parent = parent
        self.GPSWebView = self.ui.GPSWebView
        self.GPSWebView.load(QtCore.QUrl("file:////home/ieee-2/UX/geo.html"))
        self.GPSWebView.loadFinished.connect(self.webAppReady)
        self.showMaximized()
        self.setVisible(False)
        self.ui.splitter.splitterMoved.connect(self.showMax)
        self.ui.splitter_2.splitterMoved.connect(self.showMax)

    def webAppReady(self):
        pass

    def getWinId(self):
        return self.ui.VideoWidget.winId()

    def keyPressEvent(self, event):
        self.parent.keyPressEvent(event) 

    def keyReleaseEvent(self, event):
        self.parent.keyReleaseEvent(event)

    def showMax(self):
        self.setVisible(True)
        height = self.ui.GPSWidget.frameGeometry().height() - 25
        width = self.ui.GPSWidget.frameGeometry().width() - 25
        scriptString = "resetSize({0}, {1});".format(width, height)
        self.GPSWebView.page().mainFrame().evaluateJavaScript(scriptString)
        self.GPSWebView.show()

