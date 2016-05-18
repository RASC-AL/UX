import socket
import select
import os
import sys
import client

from PyQt4 import QtCore
import gobject
gobject.threads_init()
import gst

#communication: server code. This class holds a client object which is set to None, when we have a connection established to the rover 
#the client holds the socket. This socket is only used for recieving data from the server. The socket meant for sending data is present 
#in main.py
class customServer(QtCore.QThread):

	def __init__(self, port):
	    QtCore.QThread.__init__(self)
	    self.signal = QtCore.SIGNAL("server")
	    self.messageNum = 0
	    self.client = client.client()
	    self.connections = []
	    self.port = port
	    #TODO check ip
	    hostname = "0.0.0.0"
	    self.serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	    self.serv.bind((hostname, int(port)))
	    self.connections.append(self.serv)
		
	def run(self):
	    try:
		while True:
		    #print "inside the server---------------------"
		    readsock, writesock, errsock = select.select(self.connections, [], [])
		    for sock in readsock:
			self.receive()				
	    except Exception, e:
		print e

	#method moved to main code
	def send(self, data, host, port):
	    self.client = client.client()
	    self.client.connect(host, port)
	    self.client.send(data)

	def receive(self):
            chunk, addr = self.serv.recvfrom(64)
	    someString = str(chunk)
	    #print 'Message received : ' + someString
	    self.emit(self.signal, someString)
	    sys.stdout.flush()


