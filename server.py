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
		hostname = "128.205.55.128"    #"128.205.54.9"
		self.serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		#self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.serv.bind((hostname, int(port)))
		#self.serv.listen(10)
		self.connections.append(self.serv)
		
	def run(self):
		try:
			while True:
				#print "inside the server---------------------"
				readsock, writesock, errsock = select.select(self.connections, [], [])
				for sock in readsock:
					if sock == self.serv:
						#(clientsocket, address) = self.serv.accept()
						#self.connections.append(clientsocket)
						#self.client = client.client(clientsocket)
						#self.addr = address
						#print 'receiving data'
						self.receive()				
					else:
						#print 'receiving data here'
						self.receive()
		except Exception, e:
			#rospy.logerr(e)
			#self.connections.remove(self.client.sock)
			#self.client = None
			print e

	#method moved to main code
	def send(self, data, host, port):
		self.client = client.client()
		self.client.connect(host, port)
		self.client.send(data)

	def receive(self):
		#if self.client is None:
			#rospy.logerr('client connection not present')
			#return
		#chunks = []
		#bytes_recd = 0
		#while bytes_recd < 4096:
		chunk, addr = self.serv.recvfrom(64)
			#print 'received message : ' + str(chunk) + ' from ' + str(addr)
		#if chunk == '':
		#	break
		#chunks.append(chunk)
		#bytes_recd = bytes_recd + len(chunk)
		#if "\n" in chunk:
	        #        break
	        someString = str(chunk)
		#print 'Message received : ' + someString
		self.emit(self.signal, someString)
		sys.stdout.flush()


