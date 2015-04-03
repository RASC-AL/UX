'''
Created on Feb 6, 2015

@author: akash
'''
import sys
import socket
import server
from PyQt4 import QtGui
from cam import camThread
from xbox import xbox
from xbox import send_data

class Rover(QtGui.QMainWindow):
    
    def __init__(self):

        super(Rover, self).__init__()
        self.editText = MyTextEdit(self)
        self.setCentralWidget(self.editText)
        self.initUI()
	self.xbox = None
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
	
	
	        
        #Start Edit Camera
            #Labels for Camera

        self.cameraLabel0=QtGui.QLabel('Camera 0',self)
        self.cameraLabel1=QtGui.QLabel('Camera 1',self)
        self.cameraLabel2=QtGui.QLabel('Camera 2',self)
        self.cameraLabel3=QtGui.QLabel('Camera 3',self)
        self.cameraLabel4=QtGui.QLabel('Camera 4',self)
        self.cameraLabel0.setGeometry(820, 10, 100, 30)
        self.cameraLabel1.setGeometry(820, 50, 100, 30)
        self.cameraLabel2.setGeometry(820, 90, 100, 30)
        self.cameraLabel3.setGeometry(820, 130, 100, 30)
        self.cameraLabel4.setGeometry(820, 170, 100, 30)

        #TextEdits for Camera definition

        self.cameraText0 = QtGui.QLineEdit(self)
        self.cameraText1 = QtGui.QLineEdit(self)
        self.cameraText2 = QtGui.QLineEdit(self)
        self.cameraText3 = QtGui.QLineEdit(self)
        self.cameraText4 = QtGui.QLineEdit(self)
        self.cameraText0.setGeometry(920, 10, 150, 30)
        self.cameraText1.setGeometry(920, 50, 150, 30)
        self.cameraText2.setGeometry(920, 90, 150, 30)
        self.cameraText3.setGeometry(920, 130, 150, 30)
        self.cameraText4.setGeometry(920, 170, 150, 30)
        self.cameraText0.setStyleSheet("background:white;")
        self.cameraText1.setStyleSheet("background:white;")
        self.cameraText2.setStyleSheet("background:white;")
        self.cameraText3.setStyleSheet("background:white;")
        self.cameraText4.setStyleSheet("background:white;")   
        #End Edit Camera
        
        setCameraButton = QtGui.QPushButton("Set Cam",self)
        setCameraButton.clicked.connect(self.setCam)
        setCameraButton.setGeometry(820,210,90,60)       
        setCameraButton.setStyleSheet("background:white;color:black;")
        
        #Camera Select ComboBox
        comboCameraSelect = QtGui.QComboBox(self)
        comboCameraSelect.setGeometry(820, 280, 150, 50)
        comboCameraSelect.addItem("camera0")
        comboCameraSelect.addItem("camera1")
        comboCameraSelect.addItem("camera2")
        comboCameraSelect.addItem("camera3")
        comboCameraSelect.addItem("camera4")
        comboCameraSelect.setStyleSheet("background:white;color:black;")


        comboCameraSelect.activated[str].connect(self.onComboCamSelected)
        self.comboCameraSelect = comboCameraSelect
        
        #FPS ComboBox
        comboFPSSelect = QtGui.QComboBox(self)
        comboFPSSelect.setGeometry(820, 330, 150, 50)
        comboFPSSelect.addItem("5")
        comboFPSSelect.addItem("10")
        comboFPSSelect.addItem("15")
        comboFPSSelect.addItem("20")
        comboFPSSelect.addItem("25")
        comboFPSSelect.addItem("30")
        comboFPSSelect.setStyleSheet("background:white;color:black;")


        comboFPSSelect.activated[str].connect(self.onComboFPSSelected)
        self.comboFPSSelect = comboFPSSelect

	#The main Video widget	
	pic = QtGui.QWidget(self)
        pic.setGeometry(10, 10, 800, 620)
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
        stopButton.setGeometry(480,650,90,60)
        stopButton.setStyleSheet("background:white;color:black; ")

        resetButton = QtGui.QPushButton("Reset",self)
        resetButton.clicked.connect(self.onResetClicked)
        resetButton.setGeometry(950,210,90,60)
        resetButton.setStyleSheet("background:white;color:black; ")

                 
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
        self.resize(825, 600)
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
	    self.connect( self.xbox,  self.xbox.signal, self.testfunc)    
	    self.xbox.start() 
	 
        else:
            self.xbox.stop() 
	      
    def testfunc(self,sigStr):
	signalArray = sigStr.split(',')
	self.xboxLabelShoulder.setText("Shoulder "+signalArray[0])
	self.xboxLabelElbow.setText("Elbow "+signalArray[1])
	self.xboxLabelBase.setText("Base "+signalArray[2])
    	self.xboxLabelManipulator.setText("Manipulator "+signalArray[3])
	self.xboxLabelClawState.setText("ClawState "+signalArray[4])
	self.xboxLabelRightMotor.setText("RightMotor "+signalArray[5])
	self.xboxLabelLeftMotor.setText("LeftMotor "+signalArray[6])
	
    def stopXbox(self):
        self.xbox.stop()

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
