import tkinter as tk

class KeyLogController:
    def __init__(self, view, service):
        self.view = view
        self.service = service
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
        self.service.hook()
    
    def unhook(self):
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
        
        