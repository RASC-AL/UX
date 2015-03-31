from PyQt4 import QtCore
import gobject
gobject.threads_init()
import gst

class camThread(QtCore.QThread):
           
    def __init__(self,windowId):
        QtCore.QThread.__init__(self)    
        self.windowId =windowId                                   
        self.player = gst.parse_launch("udpsrc port=1234 !  application/x-rtp, encoding-name=H264, payload=96 !  rtph264depay ! h264parse ! ffdec_h264 ! autovideosink")                            
        
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
            win_id = self.windowId
            assert win_id
            imagesink = message.src
            imagesink.set_property("force-aspect-ratio", True)
            imagesink.set_xwindow_id(win_id) 
            return message               
            
    def run(self):                
        self.player.set_state(gst.STATE_PLAYING)
                                                                                       
    def quit(self):
        
        self.player.set_state(gst.STATE_NULL)
        
        #self.cap.release()
        
            
            
        
        
