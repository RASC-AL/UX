import pygame
import os
import time
import socket
import globals
from PyQt4 import QtCore
import math
#import gobject
#gobject.threads_init()
#import gst

#TODO: Fix spacing
#TODO: Fix naming

class xbox(QtCore.QThread):
	
	def __init__(self):
		QtCore.QThread.__init__(self)
		self.signal = QtCore.SIGNAL("signal")
		
		self.basePosition = 1500.0
                self.baseMod = 4
                self.baseMin = 1100.0
                self.baseMax = 1900.0

		self.manipulatorPosition = 1500.0
		self.manipulatorMod = 4
		self.manipulatorMin = 600.0
		self.manipulatorMax = 2100.0

                self.clawState = 1

		self.Command = "";
		
		self.rightMotor = 127;
		self.leftMotor = 127;
		
                self.actuatorTracker = [0, 0, 0, 0, 0]

		self.instructionsPerSecond = 8.0
	        
                self.speedMod = 2.0
 	
		self.clear = lambda: os.system('cls')
		
		pygame.init()
		 
		#Loop until the user clicks the close button.
		self.done = False
		
		# Used to manage how fast the screen updates
		clock = pygame.time.Clock()

		# Initialize the joysticks
		pygame.joystick.init()
	def stop(self):
		self.done = true
		pygame.quit ()
	def run(self):
		# -------- Main Program Loop -----------
		while self.done==False:
		    #print "Am inside xbox main loop"
		    # EVENT PROCESSING STEP
		    for event in pygame.event.get(): # User did something
		        if event.type == pygame.QUIT: # If user clicked close
		            done=True # Flag that we are done so we exit this loop
		        
		    joystick = pygame.joystick.Joystick(0)
		    joystick.init()
		        
		    joystick2 = pygame.joystick.Joystick(1)
		    joystick2.init()
		    
                    pos = False

                    #print(time.time() - globals.now)	    
                    if time.time() - globals.now < 2:
                        #Wrist Movement
                        if joystick.get_button(5) and math.fabs(joystick.get_axis(4)) > .2:
		            elbowPosition = 0
                            self.manipulatorPosition += joystick.get_axis(4) / self.manipulatorMod * 180
                            if self.manipulatorPosition > self.manipulatorMax:
                                self.manipulatorPosition = self.manipulatorMax   
                            if self.manipulatorPosition < self.manipulatorMin:
                                self.manipulatorPosition = self.manipulatorMin
		        #Elbow Movement
                        elif math.fabs(joystick.get_axis(4)) > .2:
		            elbowPosition = joystick.get_axis(4) * 254
		        else:
                            elbowPosition = 0
 
                        #Shoulder Movement
                        if math.fabs(joystick.get_axis(1)) > .2:
		            shoulderPosition = -joystick.get_axis(1) * 254
		        else:
                            shoulderPosition = 0

                        #Base Movement
                        if joystick.get_axis(2) > 0:
                            self.basePosition += joystick.get_axis(2) / self.baseMod * 80
                            self.basePosition = self.baseMax if self.basePosition > self.baseMax else self.basePosition
                        elif joystick.get_axis(5) > 0:
                            self.basePosition -= joystick.get_axis(5) / self.baseMod * 80
                            self.basePosition = self.baseMin if self.basePosition < self.baseMin else self.basePosition                          
                        
                        if joystick2.get_axis(5) > .5:
			    self.speedMod = 1.0
 		        else:
			    self.speedMod = 2.0

                        #Reset Button (LB) #TODO
                        if(joystick.get_button(4)):
                            pass
                       
                        #Start of Drive Control
                        #Default values (Not Moving)
                        self.leftMotor = 127
                        self.rightMotor = 127 

                        #Manual control
                        actuatorType = self.actuatorTracker[-1]
                        if(joystick2.get_button(6)):
                            self.actuatorTracker[-1] = actuatorType ^ 1
                        count = 0
                        if(self.actuatorTracker[-1] == 1):
                            self.actuatorTracker[0] = joystick2.get_button(11)
                            self.actuatorTracker[1] = joystick2.get_button(14)
                            self.actuatorTracker[2] = joystick2.get_button(13)
                            self.actuatorTracker[3] = joystick2.get_button(12)
                            for i in range(0, 4):
                                count += self.actuatorTracker[i]

                        #Turn left
                        if joystick2.get_button(4):
                            self.leftMotor = 127 - .2 * 127
                            self.rightMotor = 127 + .2 * 127
                        #Turn right  
                        elif joystick2.get_button(5):
                            self.leftMotor  = 127 + .2 * 127
                            self.rightMotor = 127 - .2 * 127
                        else:
		            if math.fabs(joystick2.get_axis(1)) > .2:
                                self.leftMotor = -joystick2.get_axis(1) / self.speedMod * 127 + 127
                            if math.fabs(joystick2.get_axis(4)) > .2:
		                self.rightMotor = -joystick2.get_axis(4) / self.speedMod * 127 + 127
                        #End of drive control


		        if(joystick.get_button(0) ==  1):
		            self.clawState = 1        
		        elif(joystick.get_button(1) ==  1):
		            self.clawState = 0
                        #Drop position (X)
                        elif(joystick.get_button(2)):
                            elbowPosition = 1194.0
                            shoulderPosition = 1000.0
                            self.manipulatorPosition = 1830.0
                            self.basePosition = 1800.0
                            pos = True
                        #Home Position (Y)
                        elif(joystick.get_button(3)):
                            elbowPosition = 1100.0
                            shoulderPosition = 1000.0
                            self.basePosition = 1500.0
                            pos = True
                   
                        #Change cameras or suspension using drive controller buttons
                        if(count > 0 or actuatorType != self.actuatorTracker[-1]):         
                            actStr = ','.join(str(x) for x in self.actuatorTracker)
                            rightStickStr = str((self.rightMotor - 127) * -2)
                            self.Command = "A" + actStr + ',' + rightStickStr
                        elif(joystick2.get_button(0)):
                            self.Command = "C4"
                        elif(joystick2.get_button(1)):
                            self.Command = "C5"
                        elif(joystick2.get_button(2)):
                            self.Command = "F0"
                        elif(joystick2.get_button(3)):
                            self.Command = "F2"
                        else:
                            leadChar = 'l' if pos else 's'
                            self.Command = leadChar + str(int(round(elbowPosition))) + "," + str(int(round(shoulderPosition))) + "," + str(int(round(self.basePosition))) + "," + str(int(round(self.manipulatorPosition))) + "," + str(int(round(self.clawState))) + "," + str(int(round(self.rightMotor))) + "," + str(int(round(self.leftMotor)));
		        print self.Command		  
		        self.emit(self.signal, self.Command)
		        self.Command = ""

		    # Limit to 16 frames per second
		    time.sleep(1 / self.instructionsPerSecond)
                    
		    #clock.tick(16)
		    #self.clear()
		    
		# Close the window and quit.
		# If you forget this line, the program will 'hang'
		# on exit if running from IDLE.           
