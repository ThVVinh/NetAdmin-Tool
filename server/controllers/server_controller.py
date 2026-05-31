from core.socket_server import SocketServer
from handlers.process_handler import ProcessHandler
from handlers.app_handler import AppHandler
from handlers.keylog_handler import KeyLogHandler
from handlers.screenshot_handler import Screenshot_Handler
from handlers.shutdown_handler import Shutdown_Handler
from services.shutdown_service import Shutdown_Service
from services.screenshot_service import Screenshot_Service
from services.keylog_service import KeyLogService
from services.app_service import AppService
from services.process_service import ProcessService


class ServerController:

    def __init__(self):
        self.server = SocketServer()
        self.process_handler = ProcessHandler(ProcessService())
        self.app_handler = AppHandler(AppService())
        self.keylogger_handler = KeyLogHandler(KeyLogService())
        self.screenshot_handler = Screenshot_Handler(Screenshot_Service())
        self.shutdown_handler = Shutdown_Handler(Shutdown_Service())
        
        self.server.set_client_handler(
            self.handle_client
        )

    def start(self):
        self.server.start()
        
    def handle_client(self, session):
        while True:
            command = session.read_line()
            print(f"Received command: {command}")

            if command == "PROCESS":
                self.process_handler.handle(
                    session
                )
                
            elif command == "APP":
                self.app_handler.handle(
                    session
                )
                
            elif command == "KEYLOGGER":
                self.keylogger_handler.handle(
                    session
                )
            
            elif command == "SCREENSHOT":
                self.screenshot_handler.handle(
                    session
                )
            
            elif command == "SHUTDOWN":
                self.shutdown_handler.handle()

            elif command == "QUIT":
                session.close()

    