class Shutdown_Handler():
    def __init__(self, service):
        self.service = service
    
    def handle(self):
        self.service.shutdown()
        