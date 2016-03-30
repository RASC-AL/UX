from PyQt4 import QtCore
import gobject
gobject.threads_init()
import gst
import subprocess as sub

class camThread(QtCore.QThread):
           
    def __init__(self,windowId):
	try:
		QtCore.QThread.__init__(self)    
		self.windowId =windowId                                   

		#self.player = gst.parse_launch('udpsrc port=5632 caps="application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)MP4V-ES, profile-level-id=(string)1, config=(string)000001b001000001b58913000001000000012000c48d88007d0a041e1463000001b24c61766335322e3132332e30, payload=(int)96, ssrc=(uint)298758266, clock-base=(uint)3097828288, seqnum-base=(uint)63478" ! rtpmp4vdepay ! ffdec_mpeg4 ! autovideosink udpsrc port=6112 caps="application/x-rtp,media=(string)audio, clock-rate=(int)22000, width=16, height=16, encoding-name=(string)L16, encoding-params=(string)1, channels=(int)1, channel-positions=(int)1, payload=(int)96" ! rtpL16depay ! audioconvert ! alsasink sync=false') #This is MP4V 2015
                self.cmd = ['udpsrc', 'port=5632', 'caps="application/x-rtp,', 'media=(string)video,', 'clock-rate=(int)90000,', 'encoding-name=(string)MP4V-ES,', 'profile-level-id=(string)1,', 'config=(string)000001b001000001b58913000001000000012000c48d88007d0a041e1463000001b24c61766335322e3132332e30,', 'payload=(int)96,', 'ssrc=(uint)298758266,', 'clock-base=(uint)3097828288,', 'seqnum-base=(uint)63478"', '!', 'rtpmp4vdepay', '!', 'ffdec_mpeg4', '!', 'autovideosink', 'udpsrc', 'port=6112', 'caps="application/x-rtp,media=(string)audio,', 'clock-rate=(int)22000,', 'width=16,', 'height=16,', 'encoding-name=(string)L16,', 'encoding-params=(string)1,', 'channels=(int)1,', 'channel-positions=(int)1,', 'payload=(int)96"', '!', 'rtpL16depay', '!', 'audioconvert', '!', 'alsasink', 'sync=false']

                '''
		bus = self.player.get_bus()
		bus.add_signal_watch()
		bus.enable_sync_message_emission()
		
		bus.connect("sync-message::element", self.on_sync_message)  
		self.bus = bus     '''
	except Exception, e:
		print(e)
        
    '''
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
    '''
            
    def run(self):                
       #self.player.set_state(gst.STATE_PLAYING)
       self.pro = sub.Popen(self.cmd, stdout = sub.PIPE, stderr = sub.PIPE)                                                                                
    def quit(self):
        #self.player.set_state(gst.STATE_NULL)
        self.pro.terminate()
        #self.cap.release()
        
            
            
        
        
