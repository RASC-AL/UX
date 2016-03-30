import socket

from common import *

roverSocket = None

ROVER_IP = '166.143.225.234'
ROVER_PORT = 9999

def send_data(msg):
    msg = pad(msg)
    global roverSocket
    try:
        if roverSocket is None:
            roverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            roverSocket.settimeout(1)
            roverSocket.connect((ROVER_IP, ROVER_PORT))
        totalsent = 0
        while totalsent < len(msg):
            sent = roverSocket.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
    #print 'sent message ' + msg
    except Exception, e:
    	print e
        if roverSocket is None:
            return
        roverSocket.close()
        roverSocket = None


if __name__ == '__main__':
    while 1:
        camera_num = str(raw_input('>'))
        camstr = 'C' + str(camera_num) + ',' + str(15) + ',480,640,' + str(1)
        send_data(camstr)
 
