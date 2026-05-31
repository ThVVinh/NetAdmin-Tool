import json


class AppsRunningService:
    def __init__(self, socket_client):
        self.socket_client = socket_client
        self.socket_client.send("APP")
        
    def get_apps_running(self):
        self.socket_client.send("VIEW")
        
        length = int.from_bytes(
            self.socket_client.recv_exact(4),
            "big"
        )

        data = self.socket_client.recv_exact(length)
        apps = json.loads(
            data.decode("utf-8")
        )

        return apps
            
    def kill_app(self, pid):
        message = f"KILL\n{pid}"
        self.socket_client.send(message)
        

    def start_app(self, app_name):
        message = f"START\n{app_name}"

        self.socket_client.send(message)
        
    def close(self):
        self.socket_client.send("QUIT")
        self.socket_client.close()