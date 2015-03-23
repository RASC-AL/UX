"""
Implemented a basic layout structure using grid layout.

Currently, the program is able to switch images based on the combo box item selected. 
To incorporate the logic for switching camera feeds based on combo box, the program logic should be included in onComboSelected method.

Currently, the program just displays an alert box when reset button is clicked. 
The code for reset needs to be included in handleButton method.


Currently, the program just fills the camera label values with hard-coded identifiers. 
The code for filling camera labels needs to be included in handleCameraFillLabel method

"""
import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        #Labels for Camera

        cameraLabel0=QtGui.QLabel('Camera 0')
        cameraLabel1=QtGui.QLabel('Camera 1')
        cameraLabel2=QtGui.QLabel('Camera 2')
        cameraLabel3=QtGui.QLabel('Camera 3')
        cameraLabel4=QtGui.QLabel('Camera 4')

        #TextEdits for Camera defination

        self.cameraText0 = QtGui.QLineEdit()
        self.cameraText1 = QtGui.QLineEdit()
        self.cameraText2 = QtGui.QLineEdit()
        self.cameraText3 = QtGui.QLineEdit()
        self.cameraText4 = QtGui.QLineEdit()

        #Camera Stream Holder

        #dummyLabel=QtGui.QPixmap("camera0.JPG")
        self.cameraFeed = QtGui.QLabel()
        self.cameraFeed.setPixmap(QtGui.QPixmap("camera0.JPG"))



        #ComboBox for selecting camera

        comboCameraSelect = QtGui.QComboBox(self)
        comboCameraSelect.addItem("camera0")
        comboCameraSelect.addItem("camera1")
        comboCameraSelect.addItem("camera2")
        comboCameraSelect.addItem("camera3")
        comboCameraSelect.addItem("camera4")

        comboCameraSelect.activated[str].connect(self.onComboSelected)




        #Reset Button

        self.resetButton = QtGui.QPushButton('Reset', self)
        self.resetButton.clicked.connect(self.handleButton)



        #Camera TextBoxes Fill Button

        self.cameraFillLabel = QtGui.QPushButton('CameraFillLabel', self)
        self.cameraFillLabel.clicked.connect(self.handleCameraFillLabel)


        #for displaying the status

        displayStatus = QtGui.QLabel('Status')
        grid = QtGui.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.cameraFeed,1,0,5,1)
        grid.addWidget(cameraLabel0,1,6,1,1)
        grid.addWidget(self.cameraText0,1,7,1,1)

        grid.addWidget(cameraLabel1,2,6,1,1)
        grid.addWidget(self.cameraText1,2,7 ,1,1)

        grid.addWidget(cameraLabel2,3,6,1,1)
        grid.addWidget(self.cameraText2,3,7,1,1)

        grid.addWidget(cameraLabel3,4,6,1,1)
        grid.addWidget(self.cameraText3,4,7,1,1)

        grid.addWidget(cameraLabel4,5,6,1,1)
        grid.addWidget(self.cameraText4,5,7,1,1)

        grid.addWidget(self.resetButton,6,1,1,1)
        grid.addWidget(displayStatus,7,2,3,3)
        grid.addWidget(comboCameraSelect,7,0,2,1)
        grid.addWidget(self.cameraFillLabel,6,0,1,1)
        self.setLayout(grid) 
        
        self.setGeometry(100, 100,500,500)
        self.setWindowTitle('UB_Bulls')    
        self.show()



    # Method for switching Camera Feeds
    def onComboSelected(self, text):
        #temp=QtGui.QPixmap(text+".JPG")


        self.cameraFeed.setPixmap(QtGui.QPixmap(text+".JPG"))



    # Method for handling Reset Button Event
    def handleButton(self):
        #print ('Hello World')
        QtGui.QMessageBox.question(self, 'Message',
            "Reset Button Clicked", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)


    #Method for handling filling of text boxes corresponding to Cameras.
    def handleCameraFillLabel(self):
        self.cameraText0.setText("Value_C0")
        self.cameraText1.setText("Value_C1")
        self.cameraText2.setText("Value_C2")
        self.cameraText3.setText("Value_C3")
        self.cameraText4.setText("Value_C4")
         
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()