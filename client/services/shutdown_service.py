class Shutdown_Service():
    def __init__(self, socket_client):
        self.socket_client = socket_client
    
    def shutdown(self):
        try:
            self.socket_client.send("SHUTDOWN")
        except Exception as e:
            print(f"Error sending shutdown command: {e}")
            
    def close(self):
        self.socket_client.send("QUIT")
        self.socket_client.close()