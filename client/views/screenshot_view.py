import io
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk, ImageTk

class Screenshot_View(tk.Toplevel):
    def __init__(self):
        # pic
        super().__init__()
        self.title("Screenshot")
        self.geometry("500x400")
        
        self.picture = tk.Label(self)
        self.picture.place(x=12, y=12, width=400, height=400)
        
        self.butTake = ttk.Button(self, text="Capture")
        self.butTake.place(x=420, y=12, width=75, height=175)
        
        self.save_btn = ttk.Button(self, text="Save", state=tk.DISABLED)
        self.save_btn.place(x=420, y=209, width=75, height=175)
        
        self.saveFileDialog = filedialog.SaveAs(self)
    
        
    def display_screenshot(self, screenshot_bytes):
        img = Image.open(io.BytesIO(screenshot_bytes))
        img = img.resize((400, 350), Image.LANCZOS)
        self.img_tk = ImageTk.PhotoImage(img)
        self.picture.config(image=self.img_tk)
    
    