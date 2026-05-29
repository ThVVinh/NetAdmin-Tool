class ClientSession:
    def __init__(self, socket, address):
        self.socket = socket
        self.address = address
        self.reader = socket.makefile("r")
        self.writer = socket.makefile("w")

    def read_line(self):
        return self.reader.readline().strip()

    def write_line(self, message):
        self.writer.write(message + "\n")
        self.writer.flush()

    def send(self, data):
        self.socket.sendall(data)

    def recv_bytes(self, size):
        return self.socket.recv(size)

    def close(self):
        self.socket.close()