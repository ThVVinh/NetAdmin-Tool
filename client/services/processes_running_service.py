import json


class ProcessesRunningService:
    def __init__(self, socket_client):
        self.socket_client = socket_client
        self.socket_client.send("PROCESS")
        
    def get_processes_running(self):
        self.socket_client.send("XEM")
        
        length = int.from_bytes(
            self.socket_client.recv_exact(4),
            "big"
        )

        data = self.socket_client.recv_exact(length)
        processes = json.loads(
            data.decode("utf-8")
        )
        
        return processes
            
    def kill_process(self, pid):
        message = f"KILL\n{pid}"

        self.socket_client.send(message)
        

    def start_process(self, process_name):
        message = f"START\n{process_name}"

        self.socket_client.send(message)