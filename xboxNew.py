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

flag = 0

dropTime = 0
homeTime = 0
clawTime = 0

#TODO Fix naming convention inconsistencies
class xbox(QtCore.QThread):
	
	def __init__(self):
       		#TODO QtCore.QThread.__init__(self)
		#TODO self.signal = QtCore.SIGNAL("signal")
		
                self.x = 0.00
                self.y = 0.00
                self.z = 0.00

		self.elbowPosition = 0.00
		self.shoulderPosition = 0.00
		self.basePosition = 5.001
		self.manipulatorPosition = 5.001
		self.clawState = 0;
		
		self.Command = "";
		
		self.rightMotor = 5.001;
		self.leftMotor = 5.001;
		
		self.instructionsPerSec = 8.0
	        
	        #Controls how fast the rover is capable of moving
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

                #Moved out of loop
                joystick_arm = pygame.joystick.Joystick(0)
                joystick_arm.init()

                joystick_drive = pygame.joystick.Joystick(1)
                joystick_drive.init()
                                                                                                
		# -------- Main Program Loop -----------
		while self.done==False:
		    #print "Am inside xbox main loop"
		    # EVENT PROCESSING STEP
		    for event in pygame.event.get(): # User did something
		        if event.type == pygame.QUIT: # If user clicked close
		            done=True # Flag that we are done so we exit this loop
		    
		    #Might need modifying for new joystick
		    joy_arm_x = joystick_arm.get_axis( 0 )
		    joy_arm_y = -joystick_arm.get_axis( 1 )
		    joy_arm_z = -joystick_arm.get_axis( 4 )
		    		
		    joy_drive_left = joystick_drive.get_axis( 1 )
		    joy_drive_right = joystick_drive.get_axis( 4 )
                    joy_drive_right_trigger = joystick_drive.get_axis( 5 )
		    
                    #Sets mimimums for user input
		    if (abs(joy_arm_x) < 0.25):
		        joy_arm_x = 0            
		    if (abs(joy_arm_y) < 0.25):
		        joy_arm_y = 0    
		    if (abs(joy_arm_z) < 0.25):
		        joy_arm_z = 0    
		    		
		    if (abs(joy_drive_left) < 0.25):
		        joy_drive_left = 0            
		    if (abs(joy_drive_right) < 0.25):
		        joy_drive_right = 0        
                    
                    #Sets 'Sensitivities' for actuators, servos, and 
                    #motors
                    senscoord = self.instructionsPerSec * .125
                    sensmotor = self.instructionsPerSec * .25
	            
	            #ARM:
                    #Checks for lost connection                   
                    #TODO if(time.time() - globals.now < 2):
                    if(True):
		        if(joystick_arm.get_button(0) ==  1 and flag == 0):
		            self.clawState = 1        
		        if(joystick_arm.get_button(1) ==  1 and flag == 0):
		            self.clawState = 0
		    
		        x = self.x + joy_arm_x / senscoord #X
		        
		        y = self.y + joy_arm_y / senscoord #Y
		    
		        z = self.z + joy_arm_z / senscoord #Z 
                        
                        #TODO Figure out preset positions
                        #Drop position (X)
                        if(joystick_arm.get_button(2)):
                            self.x = 0.0
                            self.y = 0.0
                            self.z= 0.0
                            flag = 2
                            dropTime = time.time()

                        #Home Position (Y)
                        elif(joystick_arm.get_button(3)):
                            flag = 3
                            self.x = 0.0
                            self.y = 0.0
                            self.z = 0.0
                            homeTime = time.time()

                        #Reset Button (LB)
                        if(joystick_arm.get_button(4)):
                            self.x = 0.0
                            self.y = 0.0
                            self.z = 0.0
                            self.clawState = 0
                       
                        #DRIVE: 

                        if(joy_drive_right_trigger > .15):
                            self.speedMod = 2.0
                        else:
                            self.speedMod = 1.0

                        #Turn left
                        if(joystick_drive.get_button(4)):
                            self.leftMotor = -.2
                            self.rightMotor = .2
                        #Turn right  
                        elif(joystick_drive.get_button(5)):
                            self.leftMotor  = .2
                            self.rightMotor = -.2
                        #Normal drive control 
                        else:
		            self.rightMotor = (-joy_drive_right * self.speedMod)/(sensmotor)
		            self.leftMotor = (-joy_drive_left * self.speedMod)/(sensmotor)
		    
                        jointValues = self.getJoints(x, y, z);
		       
		        #TODO 
		        if(jointValues):
		            elbowSend = ((self.elbowPosition / 10) * 1000) + 1000
		            shoulderSend = ((self.shoulderPosition / 10) * 650) + 1000
		            baseSend = ((self.basePosition/10) * 800) + 1100
		            manipulatorSend = ((self.manipulatorPosition/10) * 1800) + 600
		
		            rightMotorSend = ((self.rightMotor) * 127 + 127)
		            leftMotorSend = ((self.leftMotor) * 127 + 127)
                   
                        #Change cameras using drive controller buttons
                        if(joystick_drive.get_button(0)):
                            self.Command = "C0"
                        elif(joystick_drive.get_button(1)):
                            self.Command = "C1"
                        elif(joystick_drive.get_button(2)):
                            self.Command = "C2"
                        elif(joystick_drive.get_button(3)):
			    self.Command = "C3"
                        else:
                            self.Command = "l" + str(int(round(elbowSend))) + "," + str(int(round(shoulderSend))) + "," + str(int(round(baseSend))) + "," + str(int(round(manipulatorSend))) + "," + str(int(round(self.clawState))) + "," + str(int(round(rightMotorSend))) + "," + str(int(round(leftMotorSend))) + ",";
		        		  
		        #TODO self.emit(self.signal, self.Command)
		        self.Command = ""
                       
                        #Ignore for now 
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

		    # Enforces instructions per second
		    time.sleep(1/self.instructionsPerSec)
                    
		    #clock.tick(16)
		    #self.clear()
		    
		# Close the window and quit.
		# If you forget this line, the program will 'hang'
		# on exit if running from IDLE.

        def getJoints(self, x, y, z):
            link1 = 5 # First link length
            link2 = 5 # Second link length
            
            #Try block will prevent arm taking on any unreachable values
            try:
                #To find the angle Theta0 (t0)
                t0 = math.atan2(y, x)
    
                #To find the angle Theta2

                #Parameters
                k = 2 * z * link2
                l = 2 * x * link2 / math.cos(t0)
                m = link1 * link1 - z * z - link2 * link2 - x * x / (math.cos(t0) * math.cos(t0));

                t2 = 2 * math.atan2(-k + math.sqrt(k * k - m * m + l * l), m - l);
                            
                #To find the angle Theta1
                t1 = math.atan2(z - link2 * math.sin(t2), x / math.cos(t0) - link2 * math.cos(t2));

                #Convert the angles from radians to degree

                t0 = t0*180/math.pi;
                t1 = t1*180/math.pi;
                t2 = 360-t2*180/math.pi;

                #TODO Need to know bounds of angles
                #if(abs(t0 > 180) or abs(t1 > 180) or abs(t2 > 180)):       
                #    raise ValueError

                self.x = x
                self.y = y 
                self.z = z
                
                print "Base angle: %f" % t0
                print "Shoulder angle: %f" % t1
                print "Elbow Angle: %f" % t2

                #Need to convert angles to values of what is written to servos and actuators

            except ValueError:
                pass

            print "X: %f" % self.x
            print "Y: %f" % self.y
            print "Z: %f" % self.z
            

if __name__ == '__main__':
    globals.init()
    xb = xbox()
    xb.run() 


