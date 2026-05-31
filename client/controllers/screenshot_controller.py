import io
from tkinter import filedialog, filedialog, messagebox
import tkinter as tk
from PIL import Image, ImageTk


class Screenshot_Controller:
    def __init__(self, view, service):
        self.view = view
        self.service = service
        
        self.view.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )
        
        self.bind_events()
    
    def bind_events(self):
        self.view.butTake.config(
            command=self.take_picture
        )
        
        self.view.save_btn.config(
            command=lambda: self.save_picture(self.screenshot_data)
        )
        
    def take_picture(self):
        try:
            self.screenshot_data = self.service.capture()
            self.view.display_screenshot(self.screenshot_data)
            
            self.view.save_btn.config(state=tk.NORMAL)
        except Exception as ex:
            messagebox.showerror(
                "Error",
                str(ex)
            )
            
    def save_picture(self, screenshot_data):
        if screenshot_data:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                with open(file_path, "wb") as f:
                    f.write(screenshot_data)
                    
    def on_close(self):
        self.service.close()
        self.view.destroy()