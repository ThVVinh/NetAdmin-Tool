import socket

class SocketClient:
    def __init__(self):
        self.socket = None
        self.reader = None
        self.writer = None

    def connect(self, ip, port=5656):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))
        
        self.reader = self.socket.makefile("r")
        self.writer = self.socket.makefile("w")

    def send(self, msg):
        self.writer.write(msg + "\n")
        self.writer.flush()
        
    def recv_line(self):
        return self.reader.readline().strip()

    def recv_exact(self, size):
        data = b''

        while len(data) < size:
            chunk = self.socket.recv(
                size - len(data)
            )

            if not chunk:
                raise ConnectionError()

            data += chunk

        return data
    
    def convert_bytes_to_int(self, byte_data):
        return int.from_bytes(byte_data, byteorder='big')

    def close(self):
        if self.socket:
            self.socket.close()