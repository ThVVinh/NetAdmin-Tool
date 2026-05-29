import tkinter as tk

class ServerView(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Server")
        self.geometry("250x88")

        self.button1 = tk.Button(self, text="Mở server", command=self.button_Click)
        self.button1.place(x=21, y=12, width=75, height=64)

    def button_Click(self):
        pass  # Your code here
