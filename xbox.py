import pygame
import os
import time
import socket
from PyQt4 import QtCore
import gobject
gobject.threads_init()
import gst


class xbox(QtCore.QThread):
	def send_data(self,msg):
		msg = msg + "\n"
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(("166.143.225.234", 9999))
		totalsent = 0
		print "Am inside send Data"
		while totalsent < len(msg):
			sent = sock.send(msg[totalsent:])
			if sent == 0:
				raise RuntimeError("socket connection broken")
			totalsent = totalsent + sent

	def init(self):
		print "Am inside xbox init"
		elbowPosition = 1.001
		shoulderPosition = 1.001
		basePosition = 5.001
		manipulatorPosition = 5.001
		clawState = 0;
		
		Command = "";
		
		rightMotor = 5.001;
		leftMotor = 5.001;
		
		instructionsPerSec = 8.0
		
		clear = lambda: os.system('cls')
		
		pygame.init()
		 
		# Set the width and height of the screen [width,height]
		#size = [500, 700]
		#screen = pygame.display.set_mode(size)
		
		#pygame.display.set_caption("My Game")
		
		#Loop until the user clicks the close button.
		done = False
		
		# Used to manage how fast the screen updates
		clock = pygame.time.Clock()

		# Initialize the joysticks
		pygame.joystick.init()
	def stop(self):
		done = true
	def start(self):
		# -------- Main Program Loop -----------
		print "Am inside xbox main loop"
		while done==False:
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
		        clawState = 1        
		    if(joystick.get_button(1) ==  1):
		        clawState = 0
		
		    senservo = 4 *  (instructionsPerSec / 16)
		    senbigact = 16 * (instructionsPerSec / 16)
		    sensmallact = 17 * (instructionsPerSec / 16)
		    
		    sensmotor = 4 * (instructionsPerSec / 16)
		    
		    if(joystick.get_button( 5 )):
		        manipulatorPosition += joy1_right/(-senservo) #X        
		    else:
		        elbowPosition += joy1_right/(-sensmallact) #X
		        
		    shoulderPosition += joy1_left/(-senbigact) #Y
		    
		    basePosition += (joy1_lefttrigger-joy1_righttrigger)/(senservo) #
		    
		    rightMotor = joy2_right/(sensmotor)
		    leftMotor = -joy2_left/(sensmotor)
		    
		    if (abs(elbowPosition) > 10):
		        elbowPosition = 10
		                
		    if (abs(shoulderPosition) > 10):
		        shoulderPosition = 10
		        
		    if (abs(basePosition) > 10):
		        basePosition = 10
		    
		    if (abs(manipulatorPosition) > 10):
		        manipulatorPosition = 10
		                
		    if (manipulatorPosition < 0):
		        manipulatorPosition = 0
		        
		    if (elbowPosition < 0):
		        elbowPosition = 0
		                
		    if (shoulderPosition < 0):
		        shoulderPosition = 0
		                
		    if (basePosition < 0):
		        basePosition = 0
		  
		    elbowSend = ((elbowPosition / 10) * 1000) + 1000
		    shoulderSend = ((shoulderPosition / 10) * 1000) + 1000
		    
		    baseSend = ((basePosition/10) * 800) + 1100
		    
		    manipulatorSend = ((manipulatorPosition/10) * 1800) + 600
		
		    rightMotorSend = ((rightMotor) * 500) + 1500
		    leftMotorSend = ((leftMotor) * 500) + 1500
		        
		    command = "l" + str(int(round(shoulderSend))) + "," + str(int(round(elbowSend))) + "," + str(int(round(baseSend))) + "," + str(int(round(manipulatorSend))) + "," + str(int(round(clawState))) + "," + str(int(round(rightMotorSend))) + "," + str(int(round(leftMotorSend))) + ",";
		   
		    self.send_data(command)	
		
		    print command
		    command = ""
		    # Limit to 16 frames per second
		    time.sleep(.125)
		    #clock.tick(16)
		    #clear()
		    
		# Close the window and quit.
		# If you forget this line, the program will 'hang'
		# on exit if running from IDLE.
		pygame.quit ()

