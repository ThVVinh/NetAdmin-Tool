class BaseService:
    def __init__(self, socket_client):
        self.socket_client = socket_client
        
    def connect_to_server(self, ip):
        try:
            self.socket_client.connect(ip, 5656)
            message = "CONNECTED"
            self.socket_client.send(message)
            return True
        except Exception as ex:
            print(f"Error connecting to server: {ex}")
            return False

    def disconnect_from_server(self):
        message = "DISCONNECTED"
        self.socket_client.send(message)
        self.socket_client.close()