from tkinter import messagebox


class ProcessesRunningController:
    def __init__(self, view, service):
        self.view = view
        self.service = service
        self.view.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )
        self.bind_events()
        
    def bind_events(self):
        self.view.btn_view.config(
            command=self.get_processes_running
        )

        self.view.btn_kill.config(
            command=self.kill_process
        )

        self.view.btn_start.config(
            command=self.start_process
        )

        self.view.btn_delete.config(
            command=self.clear_processes_table
        )
        
    def get_processes_running(self):
        try:
            processes = self.service.get_processes_running()
            
            processes = sorted(
                processes,
                key=lambda x: x["pid"]
            )
            
            self.view.show_processes(processes)

        except Exception as ex:
            messagebox.showerror(
                "Error",
                str(ex)
            )
            
    def kill_process(self):
        pid = self.view.get_selected_pid()

        if not pid:
            messagebox.showwarning(
                "Warning",
                "Chưa chọn process"
            )
            return

        self.service.kill_process(pid)

        self.get_processes_running()
        
    def start_process(self):
        process_name = self.view.ask_process_name()

        if not process_name:
            return

        self.service.start_process(process_name)

        self.get_processes_running()

    def clear_processes_table(self):
        self.view.listView.delete(*self.view.listView.get_children())
        
    def on_close(self):
        self.service.close()
        self.view.destroy()