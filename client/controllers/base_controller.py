from tkinter import messagebox

from controllers.shutdown_controller import Shutdown_Controller
from services.shutdown_service import Shutdown_Service
from views.screenshot_view import Screenshot_View
from controllers.screenshot_controller import Screenshot_Controller
from services.screenshot_service import Screenshot_Service
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
        self.view.app_btn.config(
            command=self.butApp_Click
        )
        
        self.view.connect_btn.config(
            command=self.butConnect_Click
        )
        
        self.view.turnOff_btn.config(
            command=self.butShutdown_Click
        )
        
        self.view.exit_btn.config(
            command=self.butExit_Click
        )
        
        self.view.screenshot_btn.config(
            command=self.butScreenshot_Click
        )
        
        self.view.keylog_btn.config(
            command=self.butKeyLog_Click
        )
        
        self.view.process_btn.config(
            command=self.butProcess_Click
        )
        
    def butConnect_Click(self):
        try:
            ip_address = self.view.txtIP.get()
            if self.service.connect_to_server(ip_address):
                messagebox.showinfo("Success", "Connected to server successfully")
                self.view.app_btn.config(state="normal")
                self.view.turnOff_btn.config(state="normal")
                self.view.screenshot_btn.config(state="normal")
                self.view.keylog_btn.config(state="normal")
                self.view.process_btn.config(state="normal")
                self.view.connect_btn.config(state="disabled")
                self.view.txtIP.config(state="disabled")
            else:
                messagebox.showerror("Error", "Failed to connect to server")
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
        screenshot_view = Screenshot_View()
        service = Screenshot_Service(self.service.socket_client)
        screenshot_controller = Screenshot_Controller(screenshot_view, service)
    
    def butKeyLog_Click(self):
        keylog_view = KeylogView()
        service = Keylog_Service(self.service.socket_client)
        keylog_controller = KeyLogController(keylog_view, service)
    
    def butShutdown_Click(self):
        service = Shutdown_Service(self.service.socket_client)
        Shutdown_Controller(self.view, service)
        