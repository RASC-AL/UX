# -*- coding: utf-8 -*-
'''
Created on Feb 6, 2015

@author: akash
'''
import sys
import socket
import server
import time
import re
import globals
import cv2
import urllib
import numpy as np
from PyQt4 import QtGui, QtCore
from cam import camThread
from detectionWindow import detectionWindow
from mainWindowUI import Ui_MainWindow as mainUI
#from camGTK3 import camThread
from xboxCombo import xbox
from server import customServer
from gpsServer import gpsServer
import os

roverSocket = None
port = 9999
gpsPort = 22336
#roverip = '128.205.55.154' #LocalBackup
#roverip = '128.205.55.189' #MainRover
roverip = '166.166.193.135' #GX440
#roverip = '166.161.234.059' #GX450
MSGLEN = 64

#communication: method for sending data across to rover. This socket is only meant for sending data to the rover 
#roverSocket is None when connections isn't present and it is set to the socket when connection is established
#The socket used for receiving data is in server.py. The sockets are kept separate because the rover has 2 different nodes for
#receiving and sending data.
def send_data(msg):
    print msg + "End"
    msg = pad(msg)
    global roverSocket
    try:
        if roverSocket is None:
            print "Initializing socket"
            roverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            roverSocket.settimeout(1)
            roverSocket.connect((roverip, port))
        totalsent = 0
        '''
        while totalsent < len(msg):
            sent = roverSocket.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
        '''
        roverSocket.sendto(msg, (roverip, port))
    #print 'sent message ' + msg
    except Exception, e:
        if roverSocket is None:
            return
        #roverSocket.close()
        roverSocket = None

def ping(self, hostname):
    if self.client is None or self.addr is None:
        print "No client registered"
        return
    response = os.system("ping -c 1 " + addr)
    if response == 0:
        return True
    else:
        return False

def pad(message, length=MSGLEN):
        assert len(message) <= length, 'Message is longer than the provided length! %d > %d' % (len(message), length)

        pad_len = length - len(message)
        tokens = [' ' for x in range(pad_len)]

        return message + ''.join(tokens)


class Rover(QtGui.QWidget):

    def __init__(self):
        super(Rover, self).__init__()
        globals.init()
        globals.now = time.time()
        self.ui = mainUI()
        self.ui.setupUi(self)
        self.initUI()
        self.xbox = None
        self.server = None
        self.gpsServer = None
        self.startServer()
        self.startXbox()
        self.startGPS()
        self.detectionWindow = detectionWindow(self)
        self.camValue = 4
        self.FPS = 15
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.panMin = 0
        self.panMax = 180
        self.panRate = 1
        self.tiltMin = 0
        self.tiltMax = 75
        self.tiltRate = 1
        #Pan, Tilt, Zoom, Current Cam
        self.ptzTracker = [[90, 0, 0], [90, 0, 0]] 
        self.currentCam = 0
    def initUI(self):   
        self.ui.comboCameraSelect.addItem("Drive Camera")
        self.ui.comboCameraSelect.addItem("Rock Camera")

        self.ui.comboCameraSelect.activated[str].connect(self.onComboCamSelected)
        self.ui.comboCameraSelect

        #FPS ComboBox
        self.ui.comboFPSSelect.addItem("5")
        self.ui.comboFPSSelect.addItem("10")
        self.ui.comboFPSSelect.addItem("15")
        self.ui.comboFPSSelect.addItem("20")
        self.ui.comboFPSSelect.addItem("25")
        self.ui.comboFPSSelect.addItem("30")
        self.ui.comboFPSSelect.setCurrentIndex(2)

        self.ui.comboFPSSelect.activated[str].connect(self.onComboFPSSelected)

        #Start button for the camera feed      
        self.ui.startButton.clicked.connect(self.startCam)
                
        self.ui.mastButton.clicked.connect(self.releaseMast)

        self.ui.resetButton.clicked.connect(self.onResetClicked)
 
        self.ui.detectionButton.clicked.connect(self.onDetectionClicked)
         
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
         
        self.setStyleSheet("margin:5px; background:#0079E4; ")
        self.center()
        #self.resize(825, 600)
        self.setWindowIcon(QtGui.QIcon('/home/akash/Downloads/bulls1.jpg')) 
        self.setWindowTitle('Ub - Rasc-Al')
        self.showMaximized()
        self.cam = None
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.resetStream)
        self.timer.start(20000)

    #Key controls for moving PTZ mounts
    
    def keyPressEvent(self, event):
        eventOccurred = True
        if(event.key() == QtCore.Qt.Key_D):
	    self.ptzTracker[self.currentCam][0] -= self.panRate
	    if(self.ptzTracker[self.currentCam][0] < self.panMin):
	        self.ptzTracker[self.currentCam][0] = self.panMin
        elif(event.key() == QtCore.Qt.Key_A):
            self.ptzTracker[self.currentCam][0] += self.panRate
            if(self.ptzTracker[self.currentCam][0] > self.panMax):
                self.ptzTracker[self.currentCam][0] = self.panMax
        elif(event.key() == QtCore.Qt.Key_W):
            self.ptzTracker[self.currentCam][1] -= self.tiltRate
            if(self.ptzTracker[self.currentCam][1] < self.tiltMin):
                self.ptzTracker[self.currentCam][1] = self.tiltMin
        elif(event.key() == QtCore.Qt.Key_S):
            self.ptzTracker[self.currentCam][1] += self.tiltRate
            if(self.ptzTracker[self.currentCam][1] > self.tiltMax):
                self.ptzTracker[self.currentCam][1] = self.tiltMax
        elif(event.key() == QtCore.Qt.Key_Shift and not event.isAutoRepeat()):
            self.ptzTracker[self.currentCam][2] = 0
            self.currentCam = self.currentCam ^ 1 
            self.detectionWindow.switchCam()
        else:
            eventOccurred = False
        
        if(self.ptzTracker[self.currentCam][2] == 1 and eventOccurred):
            self.handleDigitalZoom()
        elif(eventOccurred):
            ptzStr = self.getPTZString()
            print ptzStr
            send_data(ptzStr)

    def keyReleaseEvent(self, event):
        if(event.isAutoRepeat()):
            return
        eventOccurred = True
        '''
        if(event.key() == QtCore.Qt.Key_Shift):
            self.ptzTracker[self.currentCam][2] = 0
            self.handleDigitalZoom()
        else:
            eventOccurred = False
        '''

    def setPTZForDrop(self):
        self.ptzTracker[0][0:2] = [180, 0]
        self.ptzTracker[1][0:2] = [180, 0]
        send_data(self.getPTZString())

    def getPTZString(self):
        return "P" + ','.join(str(x) for x in self.ptzTracker[0][0:2]) + \
        ',' + ','.join(str(x) for x in self.ptzTracker[1][0:2]) + \
        ',' + str(self.currentCam)

    #TODO
    def handleDigitalZoom(self):
        pass

    def resetStream(self):
        if(self.cam != None): # and self.cam.isRunning()):
            self.cam.quit()
            self.cam.start()
 
    def onComboCamSelected(self):
        self.camValue = 4 + self.ui.comboCameraSelect.currentIndex()     
        camstr = 'C' + str(self.camValue) + ',' + str(self.FPS) + ',480,640'
        print camstr
        send_data(camstr)

    def onComboFPSSelected(self):
        self.FPS = int(self.ui.comboFPSSelect.currentText())
        camstr = 'C' + str(self.camValue) + ',' + str(self.FPS) + ',480,640'
        print camstr
        send_data(camstr) 

    def onResetClicked(self):
        send_data('R')

    def onDetectionClicked(self):
        self.connect(self.detectionWindow, self.detectionWindow.signal,  send_data) 
        self.detectionWindow.showMax()

    #Not currently being used
    def onBlobClicked(self):
        if(self.camValue is 0 or self.camValue is 1):
            stream=urllib.urlopen('http://' + roverip + ':8080/stream?topic=/blob')
            bytes=''
            i = np.zeros((120,320,3), np.uint8)
            while True:
                bytes+=stream.read(10000)
                a = bytes.find('\xff\xd8')
                b = bytes.find('\xff\xd9')
                if a!=-1 and b!=-1:
                    jpg = bytes[a:b+2]
                    bytes= bytes[b+2:]
                    i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
                cv2.namedWindow('blobs', cv2.WINDOW_AUTOSIZE)
                cv2.imshow('blobs',i)
                key = cv2.waitKey(30)
                if key == 27:
                    print("kill")
                    cv2.destroyWindow('blobs')
                    return
                elif key == 49:
                    print("pressed 1")
                    stream=urllib.urlopen('http://'  + roverip + ':8080/stream?topic=/blob?width=3840?height=1080')
                    bytes=''
                    i = np.zeros((1080,3840,3), np.uint8)
                elif key == 50:
                    print("pressed 2")
                    stream=urllib.urlopen('http://' + roverip + ':8080/stream?topic=/blob?width=1280?height=480')
                    bytes=''
                    i = np.zeros((480,1280,3), np.uint8)
                elif key == 51:
                    print("pressed 3")
                    stream=urllib.urlopen('http://' + roverip + ':8080/stream?topic=/blob?width=640?height=240')
                    bytes=''
                    i = np.zeros((240,640,3), np.uint8)


    def setCam(self):
        #Set camera logic comes here    
        pass
        
    def changeText(self):
        self.edit.setText("Some")
        
    def center(self):        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft()) 
    
    def releaseMast(self):
        send_data('M')  

    def stopCam(self):
        if(self.cam!=None):                             
            self.cam.quit()
            self.cam = None
                
    def startCam(self): 
        try:
            if(self.cam==None):   
                print "initialized"
                self.cam = camThread(int(self.ui.pic.winId()), 
                    int(self.detectionWindow.getWinId())) 
                self.cam.start()                
            elif(self.cam.isRunning()):
                print "running"
                pass
        except Exception, e:
            print e
        
    def startXbox(self):
        if(self.xbox==None):  
            self.xbox = xbox(self)     
            self.connect(self.xbox,  self.xbox.signal, self.xboxCallBackfunc)    
            self.xbox.start() 
        else:
            self.xbox.stop() 
          
    def xboxCallBackfunc(self,sigStr):
        if sigStr[0] is 'C':
            self.camValue = int(sigStr[1])
            self.ui.comboCameraSelect.setCurrentIndex(self.camValue - 4)
            sigStr = 'C' + str(self.camValue) + ',' + str(self.FPS) + ',480,640'
        elif sigStr[0] is 'F':
            modifier = -1 + int(sigStr[1]) 
            length = self.ui.comboFPSSelect.count()
            index = (self.ui.comboFPSSelect.currentIndex() + modifier) % length
            index = length - 1 if index == -1 else index
            self.ui.comboFPSSelect.setCurrentIndex(index)
            self.FPS = int(self.ui.comboFPSSelect.currentText())
            sigStr = 'C' + str(self.camValue) + ',' + str(self.FPS) + ',480,640'
        elif sigStr[0] is 's' or sigStr[0] is 'l':
            signalArray = sigStr.split(',')
            self.ui.xboxLabelShoulder.setText(signalArray[1])
            self.ui.xboxLabelElbow.setText(signalArray[0][1:])
            self.ui.xboxLabelBase.setText(signalArray[2])
            self.ui.xboxLabelManipulator.setText(signalArray[3])
            self.ui.xboxLabelClawState.setText(signalArray[4])
            self.ui.xboxLabelRightMotor.setText(signalArray[5])
            self.ui.xboxLabelLeftMotor.setText(signalArray[6])    
        send_data(sigStr)    

    def stopXbox(self):
        self.xbox.stop()

    def startServer(self):             
        if(self.server==None):  
            self.server = customServer(port)     
            self.connect( self.server,  self.server.signal, self.serverCallBackfunc)    
            self.server.start() 

    def serverCallBackfunc(self,sigStr):
        if(sigStr == "" or sigStr is None):
            return
        elif(sigStr[0] == 'T'):
            #print sigStr
            globals.now = time.time()
            tokens = re.split('\s+', sigStr)
            sigStr = "Temperature: 35 C " + tokens[2]
            self.ui.metaInformation.setText(sigStr)
        elif(sigStr[0] == 'd'):
            #print(sigStr)
            dataValues = sigStr[1:].split(',')
            self.ui.pitch.setText(dataValues[0] + ' Degrees')
            self.ui.roll.setText(dataValues[1] + ' Degrees')
    
    def startGPS(self):
        if(self.gpsServer is None):
            self.gpsServer = gpsServer(gpsPort)
            self.gpsServer.start() 

class MyTextEdit(QtGui.QWidget):
    def __init__(self,parent):
        super(MyTextEdit, self).__init__(parent)                   
        #self.show()
        
def main():    
    app = QtGui.QApplication(sys.argv)
    ex = Rover()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
