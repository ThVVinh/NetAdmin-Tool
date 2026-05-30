import tkinter as tk

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Client")
        self.geometry("375x275")
        
        self.btnApp = tk.Button(self, text="App Running") 
        self.btnApp.place(x=118, y=64, width=145, height=63)
        
        self.btnConnect = tk.Button(self, text="Kết nối")
        self.btnConnect.place(x=244, y=27, width=125, height=23)

        self.txtIP = tk.Entry(self)
        self.txtIP.insert(0, "192.168.1.")
        self.txtIP.place(x=12, y=29, width=226, height=20)
        
        self.btnTat = tk.Button(self, text="Tắt máy")
        self.btnTat.place(x=118, y=133, width=145, height=57)
       
        self.btnExit = tk.Button(self, text="Thoát")
        self.btnExit.place(x=322, y=196, width=47, height=65)
        
        self.btnScreenshot = tk.Button(self, text="Chụp màn hình")
        self.btnScreenshot.place(x=118, y=196, width=198, height=65)
        
        self.btnKeyLog = tk.Button(self, text="Keylog")
        self.btnKeyLog.place(x=269, y=64, width=100, height=126)
        
        self.btnProcess = tk.Button(self, text="Process Running")
        self.btnProcess.place(x=12, y=64, width=100, height=197)
        