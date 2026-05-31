class Screenshot_Service:
    def __init__(self, socket_client):
        self.socket_client = socket_client
        self.socket_client.send("SCREENSHOT")
        
    def capture(self):
        self.socket_client.send("CAPTURE")
        
        data_length = int.from_bytes(self.socket_client.recv_exact(4), "big")
        data = self.socket_client.recv_exact(data_length)
        
        return data
    
    def close(self):
        self.socket_client.send("QUIT")
        self.socket_client.close()