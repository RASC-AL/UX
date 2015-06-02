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
#from camGTK3 import camThread
from xbox import xbox
from server import customServer
import os


from common import *


roverSocket = None
port = 9999 
#roverip = '128.205.55.125'
roverip = '166.143.225.234'

#communication: mothod for sending data across to rover. This socket is only meant for sending data to the rover 
#roverSocket is None when connections isn't present and it is set to the socket when connection is established
#The socket used for receiving data is in server.py. The sockets are kept separate because the rover has 2 different nodes for
#receiving and sending data.
def send_data(msg):
    msg = pad(msg)
    global roverSocket
    try:
        if roverSocket is None:
            roverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            roverSocket.settimeout(1)
            roverSocket.connect((roverip, port))
        totalsent = 0
        while totalsent < len(msg):
            sent = roverSocket.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
	#print 'sent message ' + msg
    except Exception, e:
        if roverSocket is None:
            return
        roverSocket.close()
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

class Rover(QtGui.QMainWindow):

    def __init__(self):

        super(Rover, self).__init__()
        globals.init()
        globals.now = time.time()
        self.editText = MyTextEdit(self)
        self.setCentralWidget(self.editText)
        self.initUI()
	self.xbox = None
	self.server = None
        self.startServer()
        self.startXbox()
        self.camValue = 0
        self.FPS = 15
        
    def initUI(self):   

	#Labels for the xbox values# shoulderSend,elbowSend,baseSend,manipulatorSend,clawState,rightMotorSend,leftMotorSend
        titleFont = QtGui.QFont('Times', 16, QtGui.QFont.Bold)        

        self.controlLabel=QtGui.QLabel('Xbox Control Values',self)
        self.controlLabel.setGeometry(10, 650, 300, 30)
        self.controlLabel.setStyleSheet("background:#0079E4; color:white")
        self.controlLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
	self.controlLabel.setFont(titleFont)
        self.xboxLabelShoulder=QtGui.QLabel('',self)
	self.xboxLabelShoulder.setGeometry(10, 690, 300, 30)
	self.xboxLabelShoulder.setStyleSheet("background:white;color:black;")
        self.xboxLabelShoulder.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
	self.xboxLabelElbow=QtGui.QLabel('',self)
	self.xboxLabelElbow.setGeometry(10, 730, 300, 30)
	self.xboxLabelElbow.setStyleSheet("background:white;color:black;")
        self.xboxLabelElbow.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
	self.xboxLabelBase=QtGui.QLabel('',self)
	self.xboxLabelBase.setGeometry(10, 770, 300, 30)
	self.xboxLabelBase.setStyleSheet("background:white;color:black;")
        self.xboxLabelBase.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
	self.xboxLabelManipulator=QtGui.QLabel('',self)
	self.xboxLabelManipulator.setGeometry(10, 810, 300, 30)
	self.xboxLabelManipulator.setStyleSheet("background:white;color:black;")
        self.xboxLabelManipulator.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
	self.xboxLabelClawState=QtGui.QLabel('',self)
	self.xboxLabelClawState.setGeometry(10, 850, 300, 30)
	self.xboxLabelClawState.setStyleSheet("background:white;color:black;")
        self.xboxLabelClawState.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
	self.xboxLabelRightMotor=QtGui.QLabel('',self)
	self.xboxLabelRightMotor.setGeometry(10, 890, 300, 30)
	self.xboxLabelRightMotor.setStyleSheet("background:white;color:black;")
        self.xboxLabelRightMotor.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
	self.xboxLabelLeftMotor=QtGui.QLabel('',self)
	self.xboxLabelLeftMotor.setGeometry(10, 930, 300, 30)
	self.xboxLabelLeftMotor.setStyleSheet("background:white;color:black;")
        self.xboxLabelLeftMotor.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.sensorLabel=QtGui.QLabel('Rover Sensor Values',self)
        self.sensorLabel.setGeometry(910, 650, 300, 30)
        self.sensorLabel.setStyleSheet("background:#0079E4; color:white")
        self.sensorLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.sensorLabel.setFont(titleFont)

	#Label for the temperature
	self.metaInformation=QtGui.QLabel('Meta Information',self)
	self.metaInformation.setGeometry(910, 690, 300, 30)
	self.metaInformation.setStyleSheet("background:white;color:black;")
        self.metaInformation.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
	
        self.motorcurrent1=QtGui.QLabel('Motor Current 1',self)
        self.motorcurrent1.setGeometry(910, 730, 300, 30)
        self.motorcurrent1.setStyleSheet("background:white;color:black;")
        self.motorcurrent1.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.motorcurrent2=QtGui.QLabel('Motor Current 2',self)
        self.motorcurrent2.setGeometry(910, 770, 300, 30)
        self.motorcurrent2.setStyleSheet("background:white;color:black;")
        self.motorcurrent2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.motorcurrent3=QtGui.QLabel('Motor Current 3',self)
        self.motorcurrent3.setGeometry(910, 810, 300, 30)
        self.motorcurrent3.setStyleSheet("background:white;color:black;")
        self.motorcurrent3.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.motorcurrent4=QtGui.QLabel('Motor Current 4',self)
        self.motorcurrent4.setGeometry(910, 850, 300, 30)
        self.motorcurrent4.setStyleSheet("background:white;color:black;")
        self.motorcurrent4.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.pitch=QtGui.QLabel('Pitch',self)
        self.pitch.setGeometry(910, 890, 300, 30)
        self.pitch.setStyleSheet("background:white;color:black;")
        self.pitch.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.roll=QtGui.QLabel('Roll',self)
        self.roll.setGeometry(910, 930, 300, 30)
        self.roll.setStyleSheet("background:white;color:black;")
        self.roll.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

#        self.angle=QtGui.QLabel('Angle',self)
#        self.angle.setGeometry(910, 970, 300, 30)
#        self.angle.setStyleSheet("background:white;color:black;")
#        self.angle.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        #self.roverTemp=QtGui.QLabel('Rover Temp: ',self)
        #self.roverTemp.setGeometry(910, 1010, 300, 30)
        #self.roverTemp.setStyleSheet("background:white;color:black;")
        #self.roverTemp.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
      
        #Camera Select Label 
        self.cameraLabel=QtGui.QLabel('Cam',self)
        self.cameraLabel.setGeometry(505, 830, 90, 30)
        self.cameraLabel.setStyleSheet("background:#0079E4; color:white")
        self.cameraLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.cameraLabel.setFont(titleFont)


        #Camera Select ComboBox
        comboCameraSelect = QtGui.QComboBox(self)
        comboCameraSelect.setGeometry(505, 870, 90, 60)
        comboCameraSelect.addItem("camera0")
        comboCameraSelect.addItem("camera1")
        comboCameraSelect.addItem("camera2")
        comboCameraSelect.addItem("camera3")
        comboCameraSelect.setStyleSheet("background:white;color:black;")


        comboCameraSelect.activated[str].connect(self.onComboCamSelected)
        self.comboCameraSelect = comboCameraSelect
        
        #FPS Label       
        self.FPSLabel=QtGui.QLabel('FPS',self)
        self.FPSLabel.setGeometry(625, 830, 90, 30)
        self.FPSLabel.setStyleSheet("background:#0079E4; color:white")
        self.FPSLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.FPSLabel.setFont(titleFont)

        #FPS ComboBox
        comboFPSSelect = QtGui.QComboBox(self)
        comboFPSSelect.setGeometry(625, 870, 90, 60)
        comboFPSSelect.addItem("5")
        comboFPSSelect.addItem("10")
        comboFPSSelect.addItem("15")
        comboFPSSelect.addItem("20")
        comboFPSSelect.addItem("25")
        comboFPSSelect.addItem("30")
        comboFPSSelect.setStyleSheet("background:white;color:black;")
        comboFPSSelect.setCurrentIndex(2)

        comboFPSSelect.activated[str].connect(self.onComboFPSSelected)
        self.comboFPSSelect = comboFPSSelect

	#The main Video widget	
	pic = QtGui.QWidget(self)
        pic.setGeometry(10, 10, 1200, 620)
        pic.setStyleSheet("image:url(/home/sblinux/Pictures/Bulls.jpg);background:white;background-repeat:repat; ")
        pic.setAttribute(0,1);
        pic.setAttribute(3,1);

	#Start button for the camera feed      
        startButton = QtGui.QPushButton("Start Cam",self)
        startButton.clicked.connect(self.startCam)
        startButton.setGeometry(505,690,90,60)       
        startButton.setStyleSheet("background:white;color:black; ")
        
        stopButton = QtGui.QPushButton("Stop Cam",self)
        stopButton.clicked.connect(self.stopCam)
        stopButton.setGeometry(625,690,90,60)
        stopButton.setStyleSheet("background:white;color:black; ")

        resetButton = QtGui.QPushButton("Reset",self)
        resetButton.clicked.connect(self.onResetClicked)
        resetButton.setGeometry(505,760,90,60)
        resetButton.setStyleSheet("background:white;color:black; ")
 
        blobButton = QtGui.QPushButton("Blob", self)
        blobButton.clicked.connect(self.onBlobClicked)
        blobButton.setGeometry(625, 760, 90, 60)
        blobButton.setStyleSheet("background:white;color:black; ")
        self.bButton = blobButton
         
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)                        
         
        self.setStyleSheet("margin:5px; background:#0079E4; ")
        self.pic = pic
        self.center()
        self.showMaximized()
	#self.resize(825, 600)
        self.setWindowIcon(QtGui.QIcon('/home/akash/Downloads/bulls1.jpg')) 
        self.setWindowTitle('Ub - Rasc-Al')
        self.show()
        self.cam = None
	self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.resetStream)
        self.timer.start(20000)

                               
    def resetStream(self):
        if(self.cam != None): # and self.cam.isRunning()):
            print("DFGvsdfCS")
            self.cam.quit()
            self.cam.start()
 
    def onComboCamSelected(self):
        self.camValue = self.comboCameraSelect.currentIndex()     
        camstr = 'C' + str(self.camValue) + ',' + str(self.FPS) + ',480,640'
	print camstr
	send_data(camstr) 

    def onComboFPSSelected(self):
        self.FPS = int(self.comboFPSSelect.currentText())
	camstr = 'C' + str(self.camValue) + ',' + str(self.FPS) + ',480,640'
        print camstr
        send_data(camstr) 

    def onResetClicked(self):
        send_data('R')

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
          
    def stopCam(self):
        if(self.cam!=None):                             
            self.cam.quit()
            self.cam = None
                
    def startCam(self): 
	try:      
	        if(self.cam==None):   
                    self.cam = camThread(int(self.pic.winId())) 
                    self.cam.start()                
	        elif(self.cam.isRunning()):            
        	    pass
	except Exception, e:
		print e
        
    def startXbox(self):
	         
	if(self.xbox==None):  
            self.xbox = xbox() 	
	    self.connect( self.xbox,  self.xbox.signal, self.xboxCallBackfunc)    
	    self.xbox.start() 
	 
        else:
            self.xbox.stop() 
	      
    def xboxCallBackfunc(self,sigStr):
        if sigStr[0] is 'C':
            self.camValue = int(sigStr[1])
            self.comboCameraSelect.setCurrentIndex(self.camValue)
            sigStr = 'C' + str(self.camValue) + ',' + str(self.FPS) + ',480,640'
        elif sigStr[0] is 'l':
	    signalArray = sigStr.split(',')
	    self.xboxLabelShoulder.setText("Shoulder: "+signalArray[1])
	    self.xboxLabelElbow.setText("Elbow: "+signalArray[0][1:])
	    self.xboxLabelBase.setText("Base: "+signalArray[2])
    	    self.xboxLabelManipulator.setText("Manipulator: "+signalArray[3])
	    self.xboxLabelClawState.setText("ClawState: "+signalArray[4])
	    self.xboxLabelRightMotor.setText("RightMotor: "+signalArray[5])
	    self.xboxLabelLeftMotor.setText("LeftMotor: "+signalArray[6])	
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
        if(sigStr[0] == 'b'):
	    if(sigStr[1] == '1'):
                self.bButton.setStyleSheet("background:green;color:black;")
            else:
                self.bButton.setStyleSheet("background:white;color:black;")
        elif(sigStr[0] == 'T'):
            
            globals.now = time.time()
            tokens = re.split('\s+', sigStr)
            sigStr = "Temperature: 55.8 C " + tokens[2]
            self.metaInformation.setText(sigStr)
	elif(sigStr[0] == 'd'):
            print(sigStr)
            dataValues = sigStr[1:].split(',')
	    self.motorcurrent1.setText('Right Motor 1: ' + dataValues[0] + ' A')
            self.motorcurrent2.setText('Right Motor 2: ' + dataValues[1] + ' A')
            self.motorcurrent3.setText('Left Motor 1: ' + dataValues[2] + ' A')
            self.motorcurrent4.setText('Left Motor 2: ' + dataValues[3] + ' A')
            self.pitch.setText('Pitch: ' + dataValues[4] + ' Degrees')
            self.roll.setText('ROll: ' + dataValues[5] + ' Degrees')
            



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
