from PyQt4 import QtCore
import gobject
gobject.threads_init()
import gst

class audioThread(QtCore.QThread):
           
    def __init__(self):
        QtCore.QThread.__init__(self)
	self.player = gst.parse_launch('udpsrc port=5000 caps="application/x-rtp,media=(string)audio, clock-rate=(int)22000, width=16, height=16, encoding-name=(string)L16, encoding-params=(string)1, channels=(int)1, channel-positions=(int)1, payload=(int)96" ! rtpL16depay ! audioconvert ! alsasink sync=false')
        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()        
        bus.connect("sync-message::element", self.on_sync_message)  
        self.bus = bus          

    def on_sync_message(self, bus, message):        
        if message.structure is None:
            return None
        message_name = message.structure.get_name()
        if message_name == "prepare-xwindow-id":
            imagesink = message.src
            return message               
            
    def run(self):                
        self.player.set_state(gst.STATE_PLAYING)
                                                                                       
    def quit(self):
        self.player.set_state(gst.STATE_NULL)
        
            
            
        
        
