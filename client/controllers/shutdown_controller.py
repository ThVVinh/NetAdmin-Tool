class Shutdown_Controller():
    def __init__(self, view, service):
        self.view = view
        self.service = service
        self.view.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )
        self.bind_events()
    
    def bind_events(self):
        self.view.turnOff_btn.config(command=self.butShutdown_Click)
        
    def butShutdown_Click(self):
        self.service.shutdown()
    
    def on_close(self):
        self.service.close()
        self.view.destroy()