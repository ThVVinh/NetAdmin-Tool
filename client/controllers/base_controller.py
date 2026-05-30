from tkinter import messagebox

from controllers.keylog_controller import KeyLogController
from views.keylog_view import KeylogView
from controllers.apps_running_controller import AppsRunningController
from services.keylog_service import Keylog_Service
from services.apps_running_service import AppsRunningService
from views.apps_running_view import AppsRunningView
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
        
        self.view.btnExit.config(
            command=self.butExit_Click
        )
        
        self.view.btnScreenshot.config(
            command=self.butScreenshot_Click
        )
        
        self.view.btnKeyLog.config(
            command=self.butKeyLog_Click
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
        apps_view = AppsRunningView()
        service = AppsRunningService(self.service.socket_client)
        app_controller = AppsRunningController(apps_view, service)

    
    def butProcess_Click(self):
        processes_view = ProcessesRunningView()
        service = ProcessesRunningService(self.service.socket_client)
        process_controller = ProcessesRunningController(processes_view, service)
    
    def butExit_Click(self):
        self.service.socket_client.close()
        self.view.destroy()
    
    def butScreenshot_Click(self):
        pass
    
    def butKeyLog_Click(self):
        keylog_view = KeylogView()
        service = Keylog_Service(self.service.socket_client)
        keylog_controller = KeyLogController(keylog_view, service)
    
    def butShutdown_Click(self):
        pass