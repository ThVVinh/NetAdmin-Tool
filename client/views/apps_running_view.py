import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

class AppsRunningView(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("List App")
        self.geometry("330x300")

        self.kill_btn = tk.Button(self, text="Kill")
        self.kill_btn.place(x=22, y=12, width=64, height=52)
        
        self.view_btn = tk.Button(self, text="View")
        self.view_btn.place(x=92, y=12, width=65, height=52)
  
        self.delete_btn = tk.Button(self, text="Delete")
        self.delete_btn.place(x=163, y=12, width=75, height=52)

        self.start_btn = tk.Button(self, text="Start")
        self.start_btn.place(x=244, y=12, width=64, height=52)

        self.columns = ("Name Application", "ID Application", "Count Thread")
        self.listView = ttk.Treeview(self, columns=self.columns, show="headings")
        
        self.listView.heading("Name Application", text="Name Application") 
        self.listView.column("Name Application", width=96) 
        
        self.listView.heading("ID Application", text="ID Application") 
        self.listView.column("ID Application", width=100) 
        
        self.listView.heading("Count Thread", text="Count Thread") 
        self.listView.column("Count Thread", width=82) 
        
        self.listView.place(x=22, y=83, width=286, height=182)


    def show_apps(self, app_list):
        self.listView.delete(*self.listView.get_children())
        
        for app in app_list:
            self.listView.insert(
                "",
                "end",
                values=(
                    app["name"],
                    app["pid"],
                    app["threads"]
                )
            )
            
    def get_selected_pid(self):
        selected_item = self.listView.focus()
        
        if not selected_item:
            return None

        item_data = self.listView.item(selected_item, "values")

        return item_data[1]
    
    def ask_app_name(self):
        return simpledialog.askstring(
            "Start Application",
            "Nhập tên application:"
        )