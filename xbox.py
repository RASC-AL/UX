import pygame
import os
import time
import socket

from PyQt4 import QtCore
import gobject
gobject.threads_init()
import gst

def send_data(msg):
		msg = msg + "\n"
		print msg
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(("166.143.225.234", 9999))
		totalsent = 0
		print "Am inside send Data"
		while totalsent < len(msg):
			sent = sock.send(msg[totalsent:])
			if sent == 0:
				raise RuntimeError("socket connection broken")
			totalsent = totalsent + sent

class xbox(QtCore.QThread):
	

	def __init__(self):
		QtCore.QThread.__init__(self)
		print "Am inside xbox init"
		self.elbowPosition = 1.001
		self.shoulderPosition = 1.001
		self.basePosition = 5.001
		self.manipulatorPosition = 5.001
		self.clawState = 0;
		
		self.Command = "";
		
		self.rightMotor = 5.001;
		self.leftMotor = 5.001;
		
		self.instructionsPerSec = 8.0
		
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
		# -------- Main Program Loop -----------
		
		while self.done==False:
		    print "Am inside xbox main loop"
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
		    
		    if (abs(joy1_left) < 0.15):
		        joy1_left = 0            
		    if (abs(joy1_right) < 0.15):
		        joy1_right = 0    
		    if (joy1_lefttrigger < 0):
		        joy1_lefttrigger = 0    
		    if (joy1_righttrigger < 0):
		        joy1_righttrigger = 0
		    
		
		    if (abs(joy2_left) < 0.15):
		        joy2_left = 0            
		    if (abs(joy2_right) < 0.15):
		        joy2_right = 0        
		    
		    if(joystick.get_button(0) ==  1):
		        self.clawState = 1        
		    if(joystick.get_button(1) ==  1):
		        self.clawState = 0
		
		    senservo = 4 *  (self.instructionsPerSec / 16)
		    senbigact = 16 * (self.instructionsPerSec / 16)
		    sensmallact = 17 * (self.instructionsPerSec / 16)
		    
		    sensmotor = 4 * (self.instructionsPerSec / 16)
		    
		    if(joystick.get_button( 5 )):
		        self.manipulatorPosition += joy1_right/(-senservo) #X        
		    else:
		        self.elbowPosition += joy1_right/(-sensmallact) #X
		        
		    self.shoulderPosition += joy1_left/(-senbigact) #Y
		    
		    self.basePosition += (joy1_lefttrigger-joy1_righttrigger)/(senservo) #
		    
		    self.rightMotor = joy2_right/(sensmotor)
		    self.leftMotor = -joy2_left/(sensmotor)
		    
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
		    shoulderSend = ((self.shoulderPosition / 10) * 1000) + 1000
		    
		    baseSend = ((self.basePosition/10) * 800) + 1100
		    
		    manipulatorSend = ((self.manipulatorPosition/10) * 1800) + 600
		
		    rightMotorSend = ((self.rightMotor) * 500) + 1500
		    leftMotorSend = ((self.leftMotor) * 500) + 1500
		        
		    self.Command = "l" + str(int(round(shoulderSend))) + "," + str(int(round(elbowSend))) + "," + str(int(round(baseSend))) + "," + str(int(round(manipulatorSend))) + "," + str(int(round(self.clawState))) + "," + str(int(round(rightMotorSend))) + "," + str(int(round(leftMotorSend))) + ",";
		    print "awra"
		    print self.Command
		    #self.send_data(self.Command)	
		
		    print self.Command
		    self.Command = ""
		    # Limit to 16 frames per second
		    time.sleep(125)
		    #clock.tick(16)
		    #self.clear()
		    
		# Close the window and quit.
		# If you forget this line, the program will 'hang'
		# on exit if running from IDLE.


