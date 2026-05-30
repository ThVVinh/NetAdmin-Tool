from tkinter import messagebox


class AppsRunningController:
    def __init__(self, view, service):
        self.view = view
        self.service = service
        
        self.bind_events()
        
    def bind_events(self):
        self.view.kill_btn.config(
            command=self.kill_app_running
        )

        self.view.view_btn.config(
            command=self.get_apps_running
        )

        self.view.start_btn.config(
            command=self.start_app
        )

        self.view.delete_btn.config(
            command=self.delete_apps_table
        )

    def get_apps_running(self):
        try:
            apps = self.service.get_apps_running()
            
            apps = sorted(
                apps,
                key=lambda x: x["pid"]
            )
            
            self.view.show_apps(apps)

        except Exception as ex:
            messagebox.showerror(
                "Error",
                str(ex)
            )
            
    def kill_app_running(self):
        pid = self.view.get_selected_pid()

        if not pid:
            messagebox.showwarning(
                "Warning",
                "Chưa chọn app"
            )
            return

        self.service.kill_app(pid)

        self.get_apps_running()
        
    def start_app(self):
        app_name = self.view.ask_app_name()

        if not app_name:
            return

        self.service.start_app(app_name)

        self.get_apps_running()

    def delete_apps_table(self):
        self.view.listView.delete(*self.view.listView.get_children())