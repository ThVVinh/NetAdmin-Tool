import socket
import threading

from core.client_session import ClientSession


class SocketServer:
    def __init__(
        self,
        host="0.0.0.0",
        port=5656
    ):

        self.host = host
        self.port = port

        self.server_socket = None
        self.is_running = False
        self.client_handler = None

    def start(self):
        if self.is_running:
            return

        self.server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.server_socket.bind(
            (self.host, self.port)
        )

        self.server_socket.listen(100)

        self.is_running = True

        print(
            f"Server running on {self.host}:{self.port}"
        )

        threading.Thread(
            target=self.accept_clients,
            daemon=True
        ).start()

    def accept_clients(self):
        print("Waiting for clients...")
        
        while self.is_running:
            try:
                client_socket, address = (
                    self.server_socket.accept()
                )

                print(
                    f"Client connected: {address}"
                )

                session = ClientSession(
                    client_socket,
                    address
                )

                threading.Thread(
                    target=self.handle_client,
                    args=(session,),
                    daemon=True
                ).start()
            except Exception as ex:
                print(
                    "Accept error:",
                    ex
                )

    def handle_client(self, session):
        try:
            if self.client_handler:
                self.client_handler(session)
        except Exception as ex:
            print(
                "Client error:",
                ex
            )
        finally:
            session.close()

            print(
                f"Client disconnected: {session.address}"
            )

    def stop(self):
        self.is_running = False

        try:
            self.server_socket.close()
        except:
            pass

        print("Server stopped")

    def set_client_handler(
        self,
        handler
    ):

        self.client_handler = handler