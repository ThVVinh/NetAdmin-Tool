from tkinter import messagebox

from services.processes_running_service import ProcessesRunningService
from controllers.processes_running_controller import ProcessesRunningController, ProcessesRunningController
from views.processes_running_view import ProcessesRunningView


class BaseController:
    def __init__(self, view, service):
        self.view = view
        self.service = service
        self.bind_events()
        
    def bind_events(self):
        self.view.btnApp.config(
            command=self.butApp_Click
        )
        
        self.view.btnConnect.config(
            command=self.butConnect_Click
        )
        
        self.view.btnTat.config(
            command=self.butShutdown_Click
        )
        
        self.view.btnReg.config(
            command=self.butReg_Click
        )
        
        self.view.btnExit.config(
            command=self.butExit_Click
        )
        
        self.view.btnScreenshot.config(
            command=self.butScreenshot_Click
        )
        
        self.view.btnKeyLock.config(
            command=self.butKeyLock_Click
        )
        
        self.view.btnProcess.config(
            command=self.butProcess_Click
        )
        
    def butConnect_Click(self):
        try:
            ip_address = self.view.txtIP.get()
            self.service.connect_to_server(ip_address)
            messagebox.showinfo("Success", "Connected to server successfully")

        except Exception as e:
            messagebox.showerror("Error", "Failed to connect to server")

    def butApp_Click(self):
        # if Program.client:
        #     Program.nw.write("APPLICATION\n")
        #     Program.nw.flush()
        #     viewApp = ListAppProcess(Program.nw, Program.client)
        #     viewApp.mainloop()
        pass
    
    def butProcess_Click(self):
        # if Program.client:
        #     Program.nw.write("PROCESS\n")
        #     Program.nw.flush()
        viewApp = ProcessesRunningView()
        service = ProcessesRunningService(self.service.socket_client)
        process_controller = ProcessesRunningController(viewApp, service)
        

    
    def butReg_Click(self):
        pass
    
    def butExit_Click(self):
        self.service.socket_client.close()
        self.view.destroy()
    
    def butScreenshot_Click(self):
        pass
    
    def butKeyLock_Click(self):
        pass
    
    def butShutdown_Click(self):
        pass