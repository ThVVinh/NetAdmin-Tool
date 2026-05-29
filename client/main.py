import tkinter as tk
from controllers.base_controller import BaseController
from core.socket_client import SocketClient
from services.base_service import BaseService
from views.main_view import MainView


root = tk.Tk()
root.withdraw()

socket_client = SocketClient()
view = MainView()
service = BaseService(socket_client)
controller = BaseController(view, service)

view.mainloop()