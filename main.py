'''
Created on Feb 6, 2015

@author: akash
'''
import sys
import socket
import server
import time
import globals
from PyQt4 import QtGui
from cam import camThread
from xbox import xbox
from server import customServer

port = 9999
def send_data(msg):
	msg = msg + "\n"
	#print msg
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ipAdd = socket.gethostbyname('sbrover2.eng.buffalo.edu')
        sock.connect((ipAdd, 9999))  
	totalsent = 0
	#print "Am inside send Data"
	while totalsent < len(msg):
		sent = sock.send(msg[totalsent:])
		if sent == 0:
			raise RuntimeError("socket connection broken")
		totalsent = totalsent + sent
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
	self.xboxLabelShoulder=QtGui.QLabel('',self)
	self.xboxLabelShoulder.setGeometry(10, 650, 300, 30)
	self.xboxLabelShoulder.setStyleSheet("background:white;color:black;")
	self.xboxLabelElbow=QtGui.QLabel('',self)
	self.xboxLabelElbow.setGeometry(10, 690, 300, 30)
	self.xboxLabelElbow.setStyleSheet("background:white;color:black;")
	self.xboxLabelBase=QtGui.QLabel('',self)
	self.xboxLabelBase.setGeometry(10, 730, 300, 30)
	self.xboxLabelBase.setStyleSheet("background:white;color:black;")
	self.xboxLabelManipulator=QtGui.QLabel('',self)
	self.xboxLabelManipulator.setGeometry(10, 770, 300, 30)
	self.xboxLabelManipulator.setStyleSheet("background:white;color:black;")
	self.xboxLabelClawState=QtGui.QLabel('',self)
	self.xboxLabelClawState.setGeometry(10, 810, 300, 30)
	self.xboxLabelClawState.setStyleSheet("background:white;color:black;")
	self.xboxLabelRightMotor=QtGui.QLabel('',self)
	self.xboxLabelRightMotor.setGeometry(10, 850, 300, 30)
	self.xboxLabelRightMotor.setStyleSheet("background:white;color:black;")
	self.xboxLabelLeftMotor=QtGui.QLabel('',self)
	self.xboxLabelLeftMotor.setGeometry(10, 890, 300, 30)
	self.xboxLabelLeftMotor.setStyleSheet("background:white;color:black;")

	#Label for the temperature
	self.metaInformation=QtGui.QLabel('Meta Information',self)
	self.metaInformation.setGeometry(620, 650, 400, 50)
	self.metaInformation.setStyleSheet("background:white;color:black;")
	#self.metaInformation.setTextFormat(0)  #Check
        
	#Camera Select ComboBox
        comboCameraSelect = QtGui.QComboBox(self)
        comboCameraSelect.setGeometry(350, 800, 90, 60)
        comboCameraSelect.addItem("camera0")
        comboCameraSelect.addItem("camera1")
        comboCameraSelect.addItem("camera2")
        comboCameraSelect.addItem("camera3")
        comboCameraSelect.setStyleSheet("background:white;color:black;")


        comboCameraSelect.activated[str].connect(self.onComboCamSelected)
        self.comboCameraSelect = comboCameraSelect
        
        #FPS ComboBox
        comboFPSSelect = QtGui.QComboBox(self)
        comboFPSSelect.setGeometry(470, 800, 90, 60)
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
        startButton.setGeometry(350,650,90,60)       
        startButton.setStyleSheet("background:white;color:black; ")
        
        stopButton = QtGui.QPushButton("Stop Cam",self)
        stopButton.clicked.connect(self.stopCam)
        stopButton.setGeometry(470,650,90,60)
        stopButton.setStyleSheet("background:white;color:black; ")

        resetButton = QtGui.QPushButton("Reset",self)
        resetButton.clicked.connect(self.onResetClicked)
        resetButton.setGeometry(350,720,90,60)
        resetButton.setStyleSheet("background:white;color:black; ")
 
        blobButton = QtGui.QPushButton("Blob", self)
        blobButton.clicked.connect(self.onBlobClicked)
        blobButton.setGeometry(470, 720, 90, 60)
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
        self.cam =None
                            
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
        #Put web browser display code
	self.bButton.setStyleSheet("background:green;color:black;")

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
        if(self.cam==None):                       
            self.cam = camThread(int(self.pic.winId()))                                 
            self.cam.start()
                        
        elif(self.cam.isRunning()):            
            pass
        
    def startXbox(self):
	         
	if(self.xbox==None):  
            self.xbox = xbox() 	
	    self.connect( self.xbox,  self.xbox.signal, self.xboxCallBackfunc)    
	    self.xbox.start() 
	 
        else:
            self.xbox.stop() 
	      
    def xboxCallBackfunc(self,sigStr):
	send_data(sigStr)
	#print sigStr	
	signalArray = sigStr.split(',')
	self.xboxLabelShoulder.setText("Shoulder "+signalArray[1])
	self.xboxLabelElbow.setText("Elbow "+signalArray[0][1:])
	self.xboxLabelBase.setText("Base "+signalArray[2])
    	self.xboxLabelManipulator.setText("Manipulator "+signalArray[3])
	self.xboxLabelClawState.setText("ClawState "+signalArray[4])
	self.xboxLabelRightMotor.setText("RightMotor "+signalArray[5])
	self.xboxLabelLeftMotor.setText("LeftMotor "+signalArray[6])	
	
    def stopXbox(self):
        self.xbox.stop()

    def startServer(self):	         
	if(self.server==None):  
            self.server = customServer(port) 	
	    self.connect( self.server,  self.server.signal, self.serverCallBackfunc)    
	    self.server.start() 

    def serverCallBackfunc(self,sigStr):
	send_data(sigStr)
        #print(sigStr)
        if(sigStr[0] == 'b'):
            #print(sigStr)
	    if(sigStr[1] == '1'):
                self.bButton.setStyleSheet("background:green;color:black;")
            else:
                self.bButton.setStyleSheet("background:white;color:black;")
        elif(sigStr[0] == 'T'):
            globals.now = time.time()
            index = sigStr.find('+')
            sigStr = "Temperature: " + sigStr[index+1:]
            self.metaInformation.setText(sigStr)
		
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
