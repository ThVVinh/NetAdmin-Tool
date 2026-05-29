from core.socket_server import SocketServer
from handlers.process_handler import ProcessHandler
from services.process_service import ProcessService


class ServerController:

    def __init__(self):

        self.server = SocketServer()

        self.process_handler = ProcessHandler(
            ProcessService()
        )
        
        self.server.set_client_handler(
            self.handle_client
        )

    def start(self):
        self.server.start()
        
    def handle_client(self, session):

        while True:

            command = session.read_line()

            print("COMMAND:", command)

            if command == "PROCESS":
                self.process_handler.handle(
                    session
                )

            elif command == "QUIT":

                break

    