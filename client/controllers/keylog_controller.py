import tkinter as tk

class KeyLogController:
    def __init__(self, view, service):
        self.view = view
        self.service = service
        self.view.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )
        self.bind_events()
        
    def bind_events(self):
        self.view.hook_btn.config(
            command=self.hook
        )
        
        self.view.unhook_btn.config(
            command=self.unhook
        )
        
        self.view.log_keys_btn.config(
            command=self.log_keys
        )
        
        self.view.clear_btn.config(
            command=self.clear
        )
        
    def hook(self):
        self.view.hook_btn.config(state="disabled")
        self.view.unhook_btn.config(state="normal")
        self.service.hook()
    
    def unhook(self):
        self.view.hook_btn.config(state="normal")
        self.view.unhook_btn.config(state="disabled")
        self.service.unhook()
    
    def log_keys(self):
        data = self.service.log_keys()
        self.view.txtKQ.config(state=tk.NORMAL) 
        self.view.txtKQ.insert(tk.END, data + "\n") 
        self.view.txtKQ.config(state=tk.DISABLED)  
    
    def clear(self):
        self.view.txtKQ.config(state=tk.NORMAL)
        self.view.txtKQ.delete(1.0, tk.END)
        self.view.txtKQ.config(state=tk.DISABLED)
        
        data = self.service.clear()
        
        self.view.txtKQ.config(state=tk.NORMAL)
        self.view.txtKQ.insert(tk.END, data + "\n")
        self.view.txtKQ.config(state=tk.DISABLED)
        
    def on_close(self):
        self.service.close()
        self.view.destroy()