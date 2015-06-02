import pygame
import os
import time
import socket
import globals
from PyQt4 import QtCore
#import gobject
#gobject.threads_init()
#import gst

flag = 0

dropTime = 0
homeTime = 0
clawTime = 0

class xbox(QtCore.QThread):
	
	def __init__(self):
		QtCore.QThread.__init__(self)
		self.signal = QtCore.SIGNAL("signal")
		#print "Am inside xbox init"
		self.elbowPosition = 0.00
		self.shoulderPosition = 0.00
		self.basePosition = 5.001
		self.manipulatorPosition = 5.001
		self.clawState = 0;
		
		self.Command = "";
		
		self.rightMotor = 5.001;
		self.leftMotor = 5.001;
		
		self.instructionsPerSec = 8.0
	        
                self.speedMod = 1.0
 	
		self.clear = lambda: os.system('cls')
		
		pygame.init()
		 
		# Set the width and height of the screen [width,height]
		#size = [500, 700]
		#screen = pygame.display.set_mode(size)
		
		#pygame.display.set_caption("My Game")
		
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
                global dropTime, homeTime, clawTime, flag
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
		    
		    joy1_left = joystick.get_axis( 1 )
		    joy1_right = joystick.get_axis( 4 )
		    joy1_lefttrigger = joystick.get_axis( 2 )
		    joy1_righttrigger = joystick.get_axis( 5 )
		
		    joy2_left = joystick2.get_axis( 1 )
		    joy2_right = joystick2.get_axis( 4 )
                    joy2_righttrigger = joystick2.get_axis( 5 )
		    
		    if (abs(joy1_left) < 0.25):
		        joy1_left = 0            
		    if (abs(joy1_right) < 0.25):
		        joy1_right = 0    
		    if (joy1_lefttrigger < 0):
		        joy1_lefttrigger = 0    
		    if (joy1_righttrigger < 0):
		        joy1_righttrigger = 0
		    
		
		    if (abs(joy2_left) < 0.25):
		        joy2_left = 0            
		    if (abs(joy2_right) < 0.25):
		        joy2_right = 0        
                    
                    senservo = 4 *  (self.instructionsPerSec / 16)
                    senbigact = 30 * (self.instructionsPerSec / 16)
                    sensmallact = 17 * (self.instructionsPerSec / 16)

                    sensmotor = 4 * (self.instructionsPerSec / 16)
	            
                    #print(time.time() - globals.now)	    
                    if(time.time() - globals.now < 1):
		        if(joystick.get_button(0) ==  1 and flag == 0):
		            self.clawState = 1        
		        if(joystick.get_button(1) ==  1 and flag == 0):
		            self.clawState = 0
		
		        if(joystick.get_button( 5 )):
		            self.manipulatorPosition += joy1_right/(-senservo) #X        
		        else:
		            self.elbowPosition += joy1_right/(-sensmallact) #X
		        
		        self.shoulderPosition += joy1_left/(-senbigact) #Y
		    
		        self.basePosition += (joy1_lefttrigger-joy1_righttrigger)/(senservo * 2) 
                        
                        #Drop position (X)
                        if(joystick.get_button(2)):
                            self.elbowPosition = 1.94
                            self.shoulderPosition = 0.0
                            time.sleep(5)
                            self.manipulatorPosition = 8.2
                            flag = 2
                            dropTime = time.time()

                        #Home Position (Y)
                        elif(joystick.get_button(3)):
                            flag = 3
                            self.basePosition = 3.75
                            homeTime = time.time()

                        if(joy2_righttrigger > .15):
			    self.speedMod = 2.0
 		        else:
			    self.speedMod = 1.0

                        #Reset Button (LB)
                        if(joystick.get_button(4)):
                            self.shoulderPosition = 0.0
                            self.clawState = 0
                       
                        #Turn left
                        if(joystick2.get_button(4)):
                            self.leftMotor = -.2
                            self.rightMotor = .2
                        #Turn right  
                        elif(joystick2.get_button(5)):
                            self.leftMotor  = .2
                            self.rightMotor = -.2
 
                        else:
		            self.rightMotor = (-joy2_right * self.speedMod)/(sensmotor)
		            self.leftMotor = (-joy2_left * self.speedMod)/(sensmotor)
		    

		        if (abs(self.elbowPosition) > 10):
		            self.elbowPosition = 10
		                
		        if (abs(self.shoulderPosition) > 10):
		            self.shoulderPosition = 10
		        
		        if (abs(self.basePosition) > 10):
		            self.basePosition = 10
		    
		        if (abs(self.manipulatorPosition) > 10):
		            self.manipulatorPosition = 10
		                
		        if (self.manipulatorPosition < 0):
		            self.manipulatorPosition = 0
		        
		        if (self.elbowPosition < 0):
		            self.elbowPosition = 0
		                
		        if (self.shoulderPosition < 0):
		            self.shoulderPosition = 0
		                
		        if (self.basePosition < 0):
		            self.basePosition = 0
		  
		        elbowSend = ((self.elbowPosition / 10) * 1000) + 1000
		        shoulderSend = ((self.shoulderPosition / 10) * 650) + 1000
		    
		        baseSend = ((self.basePosition/10) * 800) + 1100
		    
		        manipulatorSend = ((self.manipulatorPosition/10) * 1800) + 600
		
		        rightMotorSend = ((self.rightMotor) * 127 + 127)
		        leftMotorSend = ((self.leftMotor) * 127 + 127)
                   
                        #Change cameras using drive controller buttons
                        if(joystick2.get_button(0)):
                            self.Command = "C0"
                        elif(joystick2.get_button(1)):
                            self.Command = "C1"
                        elif(joystick2.get_button(2)):
                            self.Command = "C2"
                        elif(joystick2.get_button(3)):
			    self.Command = "C3"
                        else:
                            self.Command = "l" + str(int(round(elbowSend))) + "," + str(int(round(shoulderSend))) + "," + str(int(round(baseSend))) + "," + str(int(round(manipulatorSend))) + "," + str(int(round(self.clawState))) + "," + str(int(round(rightMotorSend))) + "," + str(int(round(leftMotorSend))) + ",";
		        		  
		        self.emit(self.signal, self.Command)
		        self.Command = ""
                       
                        #Drop position (X)
                        if(flag == 2 and time.time() - dropTime > 12):
                            self.basePosition = 7.80
                            clawTime = time.time()
                            flag = 4
                        
			if(flag == 4 and time.time() - clawTime > 5):
			    self.clawState = 1
			    flag = 0
			
                        #Home Position (Y)
                        if(flag == 3 and (time.time() - homeTime) > 5):
                            self.elbowPosition = 1.94
                            self.shoulderPosition = 3.50
                            self.manipulatorPosition = 5.3
                            flag = 0

		    # Limit to 16 frames per second
		    time.sleep(.25)
                    
		    #clock.tick(16)
		    #self.clear()
		    
		# Close the window and quit.
		# If you forget this line, the program will 'hang'
		# on exit if running from IDLE.


