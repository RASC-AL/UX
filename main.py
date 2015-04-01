'''
Created on Feb 6, 2015

@author: akash
'''
import sys
import socket
import server
from PyQt4 import QtGui
from cam import camThread

class Rover(QtGui.QMainWindow):
    
    def __init__(self):
        super(Rover, self).__init__()
        self.editText = MyTextEdit(self)
        self.setCentralWidget(self.editText)
        self.initUI()
        
    def initUI(self):   
           
        pic = QtGui.QWidget(self)
        pic.setGeometry(10, 10, 400, 320)
        
        #Start Edit Camera
            #Labels for Camera

        self.cameraLabel0=QtGui.QLabel('Camera 0',self)
        self.cameraLabel1=QtGui.QLabel('Camera 1',self)
        self.cameraLabel2=QtGui.QLabel('Camera 2',self)
        self.cameraLabel3=QtGui.QLabel('Camera 3',self)
        self.cameraLabel4=QtGui.QLabel('Camera 4',self)
        self.cameraLabel0.setGeometry(450, 10, 100, 30)
        self.cameraLabel1.setGeometry(450, 50, 100, 30)
        self.cameraLabel2.setGeometry(450, 90, 100, 30)
        self.cameraLabel3.setGeometry(450, 130, 100, 30)
        self.cameraLabel4.setGeometry(450, 170, 100, 30)
        #TextEdits for Camera definition

        self.cameraText0 = QtGui.QLineEdit(self)
        self.cameraText1 = QtGui.QLineEdit(self)
        self.cameraText2 = QtGui.QLineEdit(self)
        self.cameraText3 = QtGui.QLineEdit(self)
        self.cameraText4 = QtGui.QLineEdit(self)
        self.cameraText0.setGeometry(550, 10, 150, 30)
        self.cameraText1.setGeometry(550, 50, 150, 30)
        self.cameraText2.setGeometry(550, 90, 150, 30)
        self.cameraText3.setGeometry(550, 130, 150, 30)
        self.cameraText4.setGeometry(550, 170, 150, 30)
        self.cameraText0.setStyleSheet("background:white;")
        self.cameraText1.setStyleSheet("background:white;")
        self.cameraText2.setStyleSheet("background:white;")
        self.cameraText3.setStyleSheet("background:white;")
        self.cameraText4.setStyleSheet("background:white;")   
        #End Edit Camera
        
        setCameraButton = QtGui.QPushButton("Set Cam",self)
        setCameraButton.clicked.connect(self.setCam)
        setCameraButton.setGeometry(450,210,90,60)       
        setCameraButton.setStyleSheet("background:white;color:black;")
        
        
        comboCameraSelect = QtGui.QComboBox(self)
        comboCameraSelect.setGeometry(450, 280, 150, 50)
        comboCameraSelect.addItem("camera0")
        comboCameraSelect.addItem("camera1")
        comboCameraSelect.addItem("camera2")
        comboCameraSelect.addItem("camera3")
        comboCameraSelect.addItem("camera4")
        comboCameraSelect.setStyleSheet("background:white;color:black;")


        comboCameraSelect.activated[str].connect(self.onComboSelected)
        self.comboCameraSelect = comboCameraSelect
        
        pic.setStyleSheet("image:url(/home/sblinux/Pictures/Bulls.jpg);background:white;background-repeat:repat; ")
        pic.setAttribute(0,1);
        pic.setAttribute(3,1);
      
        startButton = QtGui.QPushButton("Start Cam",self)
        startButton.clicked.connect(self.startCam)
        startButton.setGeometry(100,330,90,60)       
        startButton.setStyleSheet("background:white;color:black; ")
        
        stopButton = QtGui.QPushButton("Stop Cam",self)
        stopButton.clicked.connect(self.stopCam)
        stopButton.setGeometry(240,330,90,60)
        stopButton.setStyleSheet("background:white;color:black; ")
                        
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
    def onComboSelected(self):
        camstr = 'C ' + str(self.comboCameraSelect.currentIndex())  
        pass
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
