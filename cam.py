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
            self.windowId =windowId                                   

		#self.player = gst.parse_launch('udpsrc port=1234 caps="application/x-rtp,payload=96,encoding-name=JPEG" ! rtpjpegdepay ! jpegdec ! autovideosink') #this is MJPEG 2015

		#self.player = gst.parse_launch('udpsrc port=1234 caps="application/x-rtp,payload=96,encoding-name=H264" ! rtph264depay ! h264parse ! ffdec_h264 ! xvimagesink sync=false') #This is H264 2015

		#self.player = gst.parse_launch('udpsrc port=5632 caps="application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)MP4V-ES, profile-level-id=(string)1, config=(string)000001b001000001b58913000001000000012000c48d88007d0a041e1463000001b24c61766335322e3132332e30, payload=(int)96, ssrc=(uint)298758266, clock-base=(uint)3097828288, seqnum-base=(uint)63478" ! rtpmp4vdepay ! ffdec_mpeg4 ! autovideosink udpsrc port=6112 caps="application/x-rtp,media=(string)audio, clock-rate=(int)22000, width=16, height=16, encoding-name=(string)L16, encoding-params=(string)1, channels=(int)1, channel-positions=(int)1, payload=(int)96" ! rtpL16depay ! audioconvert ! alsasink sync=false') #This is MP4V 2015

                #self.player = gst.parse_launch('udpsrc port=5632 caps="application/x-rtp,payload=26,encoding-name=JPEG" ! queue ! rtpjpegdepay ! jpegdec ! xvimagesink sync=false')#This is jpeg with sync n queue 2015

                #self.player = gst.parse_launch('udpsrc port=5632 caps="application/x-rtp,payload=26,encoding-name=THEORA" ! queue ! rtptheorapay ! theoradec ! xvimagesink sync=false')#This is jpeg with sync n queue 2015

	    #	self.player = gst.parse_launch('''udpsrc port=5632 ! "application/x-rtp, payload=96, media=video, clock-rate=90000, encoding-name=MP4V-ES" ! rtpmp4vdepay ! ffdec_mpeg4 ! ffmpegcolorspace ! videoscale ! video/x-raw-rgb, width=1030, height=768 ! autovideosink sync=false''')
                
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
        
    def run(self):                
        self.player.set_state(gst.STATE_PLAYING)
                                                                                
    def quit(self):
        self.player.set_state(gst.STATE_NULL)
        
        #self.cap.release()
        
    def gstInitialization(self):         
        self.player = gst.parse_launch('udpsrc port=5632 caps="application/x-rtp,payload=26,encoding-name=JPEG" ! queue ! rtpjpegdepay ! jpegdec ! xvimagesink sync=false')
        self.bus = self.player.get_bus()
        self.bus.add_signal_watch()
        self.bus.enable_sync_message_emission()
        self.bus.connect("sync-message::element", self.on_sync_message)
        self.bus.connect("sync-message::error", self.handle_segfault)
	print 'kuch bhi printing'
        
    
        
        

