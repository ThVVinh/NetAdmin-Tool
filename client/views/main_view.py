import tkinter as tk

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Client")
        self.geometry("375x275")
        
        self.app_btn = tk.Button(self, text="App Running", state=tk.DISABLED) 
        self.app_btn.place(x=118, y=64, width=145, height=63)
        
        self.connect_btn = tk.Button(self, text="Connect")
        self.connect_btn.place(x=244, y=27, width=125, height=23)

        self.txtIP = tk.Entry(self)
        self.txtIP.insert(0, "192.168.1.")
        self.txtIP.place(x=12, y=29, width=226, height=20)
        
        self.turnOff_btn = tk.Button(self, text="Shut down", state=tk.DISABLED)
        self.turnOff_btn.place(x=118, y=133, width=145, height=57)
       
        self.exit_btn = tk.Button(self, text="Exit")
        self.exit_btn.place(x=322, y=196, width=47, height=65)
        
        self.screenshot_btn = tk.Button(self, text="Screenshot", state=tk.DISABLED)
        self.screenshot_btn.place(x=118, y=196, width=198, height=65)
        
        self.keylog_btn = tk.Button(self, text="Keylog", state=tk.DISABLED)
        self.keylog_btn.place(x=269, y=64, width=100, height=126)
        
        self.process_btn = tk.Button(self, text="Process Running", state=tk.DISABLED)
        self.process_btn.place(x=12, y=64, width=100, height=197)
        