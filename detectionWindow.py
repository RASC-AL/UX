import sys
from PyQt4 import QtGui, QtCore
from detectionWindowUI import Ui_DetectionWindow as UI

class detectionWindow(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = UI()
        self.ui.setupUi(self)
        self.parent = parent
        
        self.signal = QtCore.SIGNAL("signal")       

        self.GPSWebView = self.ui.GPSWebView
        self.GPSWebView.load(QtCore.QUrl("file:////home/ieee/UX/geo.html"))
        self.GPSWebView.loadFinished.connect(self.webAppReady)

        for i in range(1, 7):
            self.ui.FPSComboBox.addItem(str(i * 5))
        self.ui.FPSComboBox.setCurrentIndex(1)
        self.ui.FPSComboBox.activated[str].connect(self.selectFPS)

        self.ui.camComboBox.addItem("Left Camera")
        self.ui.camComboBox.addItem("Right Camera")

        self.ui.markerComboBox.addItem("Purple Rock")
        self.ui.markerComboBox.addItem("Green Rock")
        self.ui.markerComboBox.addItem("Blue Rock")
        self.ui.markerComboBox.addItem("Red Rock")
        self.ui.markerComboBox.addItem("Orange Rock")
        self.ui.markerComboBox.addItem("Yellow Rock")
        self.ui.markerComboBox.activated[str].connect(self.changeMarker)

        self.ui.clearComboBox.addItem("Clear Route")
        self.ui.clearComboBox.addItem("Clear Markers")
        self.ui.clearComboBox.addItem("Clear All")

        self.ui.clearButton.clicked.connect(self.handleClear)

        self.ui.openButton.clicked.connect(self.handleOpen)

        self.ui.saveButton.clicked.connect(self.handleSave)

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

    def selectFPS(self):
        camstr = 'D' + self.ui.FPSComboBox.currentText()
        self.emit(self.signal, camstr)

    def switchCam(self):
        self.ui.camComboBox.setCurrentIndex(self.ui.camComboBox.currentIndex() ^ 1)

    def setDropCam(self):
        self.ui.camComboBox.setCurrentIndex(1)

    def changeMarker(self):
        color = self.ui.markerComboBox.currentText().split(' ')[0]
        print color
        scriptString = "setMarkerColor(\"" + color + "\");"
        self.evaluateJS(scriptString)

    def handleClear(self):
        clearType = self.ui.clearComboBox.currentText().split(' ')[1]
        scriptString = "clearScreen(\"" + clearType + "\");"  
        self.evaluateJS(scriptString)

    def handleOpen(self):
        pass

    def handleSave(save):
        pass

    def showMax(self):
        self.setVisible(True)
        height = self.ui.GPSWidget.frameGeometry().height() - 25
        width = self.ui.GPSWidget.frameGeometry().width() - 25
        scriptString = "resetSize({0}, {1});".format(width, height)
        self.evaluateJS(scriptString)
        self.GPSWebView.show()

    def evaluateJS(self, scriptString):
        self.GPSWebView.page().mainFrame().evaluateJavaScript(scriptString)


