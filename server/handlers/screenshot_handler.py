class Screenshot_Handler:
    def __init__(self, screenshot_service):
        self.screenshot_service = screenshot_service
    
    def handle(self, session):
        while True:
            signal = session.read_line()

            if signal == "CAPTURE":
                screenshot_data = self.screenshot_service.capture()
                screenshot_size = len(screenshot_data)
                
                session.send(screenshot_size.to_bytes(4, "big"))
                session.send(screenshot_data)

            elif signal == "QUIT":
                session.close()
                break