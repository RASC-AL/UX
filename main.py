'''
Created on Feb 6, 2015

@author: akash
'''
import sys
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
        pic.setGeometry(10, 10, 400, 240)
        
        
        pic.setStyleSheet("image:url(/home/akash/Downloads/bulls.jpg);background-repeat:repat; ")
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
