import tkinter as tk

class KeylogView(tk.Toplevel):
    def __init__(self):
        super().__init__()
        
        self.title("Keystroke")
        self.geometry("350x350")
        
        self.txtKQ = tk.Text(self, state="disabled")
        self.txtKQ.place(x = 12, y = 77, width = 318, height = 182)

        self.hook_btn = tk.Button(self, text="Hook", state="normal")
        self.hook_btn.place(x = 12, y = 12, width = 75, height = 59)

        self.unhook_btn = tk.Button(self, text="Unhook", state="disabled")
        self.unhook_btn.place(x = 93, y = 13, width = 75, height = 58)

        self.log_keys_btn = tk.Button(self, text="Print Keys")
        self.log_keys_btn.place(x = 174, y = 12, width = 75, height = 59)

        self.clear_btn = tk.Button(self, text="Clear")
        self.clear_btn.place(x = 256, y = 13, width = 74, height = 58)
