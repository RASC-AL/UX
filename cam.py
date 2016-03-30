#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
import gobject
gobject.threads_init()
import gst

class camThread(QtCore.QThread):
    INSTANCE = None

    def __init__(self,windowId):
        camThread.INSTANCE = self
        try:
            QtCore.QThread.__init__(self)    
            self.windowId = windowId                                   
            self.gstInitialization()
        except Exception, e:
            print(e)
        
    def on_sync_message(self, bus, message):        
        if message.structure is None:
            return None
        message_name = message.structure.get_name()
        if message_name == "prepare-xwindow-id":
            win_id = self.windowId
            assert win_id
            imagesink = message.src
            imagesink.set_property("force-aspect-ratio", True)
            imagesink.set_xwindow_id(win_id) 
            return message               
             
    def handle_segfault(self, bus, message):
        try:
            self.mainloop.quit()
        except:
            pass
        print("SEGMENTATION FAULT")
        self = camThread.INSTANCE
        self.gstInitialization()
        
    def run(self):
        self.player.set_state(gst.STATE_PLAYING)
                                                                                
    def quit(self):
        self.player.set_state(gst.STATE_NULL)
        if self.player:
            del self.player
        if self.bus:
            del self.bus
        self.gstInitialization()
        
        #self.cap.release()
        
    def gstInitialization(self):         
        #self.player = gst.parse_launch('udpsrc port=5632 caps="application/x-rtp,payload=26,encoding-name=JPEG" ! queue ! rtpjpegdepay ! jpegdec ! xvimagesink sync=false')
        #self.player = gst.parse_launch('udpsrc port=5632 caps="application/x-rtp,payload=26,encoding-name=JPEG" ! queue ! rtpjpegdepay ! jpegdec ! xvimagesink sync=false udpsrc port=6112 caps="application/x-rtp,media=(string)audio, clock-rate=(int)8000, width=16, height=16, encoding-name=(string)L16, encoding-params=(string)1, channels=(int)1, channel-positions=(int)1, payload=(int)96" ! rtpL16depay ! audioconvert ! alsasink sync=false') #current 2015
       # self.player = gst.parse_launch('udpsrc port=5632 caps="application/x-rtp,payload=26,encoding-name=JPEG" ! queue ! rtpjpegdepay ! jpegdec ! xvimagesink  udpsrc port=6112 caps="application/x-rtp, media=(string)audio, clock-rate=(int)8000, encoding-name=(string)AMR, encoding-params=(string)1, octet-align=(string)1, payload=(int)96" ! rtpamrdepay ! amrnbdec ! audioconvert ! alsasink')        
#self.player = gst.parse_launch('udpsrc port=5632 caps="application/x-rtp,payload=26,encoding-name=JPEG" ! queue ! rtpjpegdepay ! jpegdec ! xvimagesink sync=false udpsrc port=6112 caps="application/x-rtp,media=(string)audio, clock-rate=(int)22000, width=16, height=16, encoding-name=(string)L16, encoding-params=(string)1, channels=(int)1, channel-positions=(int)1, payload=(int)96" ! rtpL16depay ! audioconvert ! alsasink sync=false')
        self.player = gst.parse_launch('udpsrc port=1234 caps="application/x-rtp, payload=127" ! rtph264depay ! ffdec_h264 ! xvimagesink sync=false')
        self.bus = self.player.get_bus()
        self.bus.add_signal_watch()
        self.bus.enable_sync_message_emission()
        self.bus.connect("sync-message::element", self.on_sync_message)
        self.bus.connect("sync-message::error", self.handle_segfault)

