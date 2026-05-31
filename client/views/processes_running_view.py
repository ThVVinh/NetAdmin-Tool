import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

class ProcessesRunningView(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("List Process")
        self.geometry("302x261")
        
        self.btn_kill = ttk.Button(self, text="Kill")
        self.btn_kill.place(x=24, y=12, width=66, height=47)
        
        self.btn_view = ttk.Button(self, text="View")
        self.btn_view.place(x=96, y=12, width=59, height=47)
        
        self.btn_start = ttk.Button(self, text="Start")
        self.btn_start.place(x=231, y=12, width=59, height=47)
        
        self.btn_delete = ttk.Button(self, text="Delete")
        self.btn_delete.place(x=161, y=12, width=64, height=47)
        
        self.listView = ttk.Treeview(self, columns=("Name Process", "ID Process", "Count Thread"), show="headings")
        self.listView.heading("Name Process", text="Name Process")
        self.listView.column("Name Process", width=100)
        self.listView.heading("ID Process", text="ID Process")
        self.listView.column("ID Process", width=65)
        self.listView.heading("Count Thread", text="Count Thread")
        self.listView.column("Count Thread", width=75)
        self.listView.place(x=24, y=74, width=266, height=162)
    
            
    def show_processes(self, process_list):
        self.listView.delete(*self.listView.get_children())
        
        for process in process_list:
            self.listView.insert(
                "",
                "end",
                values=(
                    process["name"],
                    process["pid"],
                    process["threads"]
                )
            )
            
    def get_selected_pid(self):
        selected_item = self.listView.focus()

        if not selected_item:
            return None

        item_data = self.listView.item(selected_item, "values")

        return item_data[1]
    
    def ask_process_name(self):
        return simpledialog.askstring(
            "Start Process",
            "Nhập tên process:"
        )