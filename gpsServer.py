import socket
import select
import os
import sys
import client
import json

from PyQt4 import QtCore
from server import customServer

class gpsServer(QtCore.QThread):

    def __init__(self, port, detectionWindow):
        QtCore.QThread.__init__(self)
        self.port = port
        self.bufferLength = 128
        self.server = None
        self.detectionWindow = detectionWindow

    def run(self):
        if(self.server is None):
            self.server = customServer(self.port, self.bufferLength) 
            self.connect(self.server, self.server.signal, self.gpsCallback)  
            self.server.start()

    def gpsCallback(self, sigStr):
        print "Callback"
        print sigStr
        strArr = sigStr.split('\n')[1].split(',')
        if(strArr[0] == '$GPGGA'):
            lat, lng = self.getLatLongFromNMEA(strArr)
            self.detectionWindow.handleCallback(lat, lng)
            print lat
            print lng

    def getLatLongFromNMEA(self, nmeaSen):
        lat = nmeaSen[2]
        latDir = 1.0 if nmeaSen[3] == 'N' else -1.0

        #Parse latitude to google maps coordinate
        hours = float(lat[0:2])
        mins = float(lat[2:])
        lat = latDir * (hours + mins / 60.0)

        lng = nmeaSen[4]
        lngDir = 1.0 if nmeaSen[5] == 'E' else -1.0

        #Parse longitude to google maps coordinates
        hours = float(lng[0:3])
        mins = float(lng[3:])
        lng = lngDir * (hours + mins / 60.0)

        return [lat, lng]

