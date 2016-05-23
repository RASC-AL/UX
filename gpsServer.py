import socket
import select
import os
import sys
import client
import json

from PyQt4 import QtCore
from server import customServer

class gpsServer(QtCore.QThread):

    def __init__(self, port):
        QtCore.QThread.__init__(self)
        self.port = port
        self.server = None

    def run(self):
        if(self.server is None):
            self.server = customServer(self.port) 
            self.connect(self.server, self.server.signal, self.gpsCallback)  
            self.server.start()

    def gpsCallback(self, sigStr):
        #print " ".join(hex(ord(n)) for n in sigStr)
        strArr = sigStr.split(',')
        #if(strArr[0] == '$GPGGA'):
        #    lat, lon = self.getLatLongFromNMEA(strArr)
        #    print lat
        #    print lon
        print sigStr

    def getLatLongFromNMEA(self, nmeaSen):
        lat = nmeaSen[2]
        latDir = 1.0 if nmeaSen[3] == 'N' else -1.0

        #Parse latitude to google maps coordinate
        hours = float(lat[0:2])
        mins = float(lat[2:])
        lat = latDir * (hours + mins / 60.0)

        lon = nmeaSen[4]
        lonDir = 1.0 if nmeaSen[5] == 'E' else -1.0

        #Parse longitude to google maps coordinates
        hours = float(lon[0:3])
        mins = float(lon[3:])
        lon = lonDir * (hours + mins / 60.0)

        return [lat, lon]

