import json


class AppHandler:
    def __init__(self, app_service):
        self.app_service = app_service

    def handle(self, session):
        while True:
            signal = session.read_line()

            if signal == "VIEW":
                apps = self.app_service.get_apps()

                self.send_apps(
                    session,
                    apps
                )

            elif signal == "KILL":
                pid = session.read_line()
                print(f"Received kill command for PID: {pid}")
                self.app_service.kill_app(pid)

            elif signal == "START":
                app_name = session.read_line()
                self.app_service.start_app(app_name)

            elif signal == "QUIT":
                break

    def send_apps(self, session, apps):
        data = json.dumps(apps).encode("utf-8")
        session.send(len(data).to_bytes(4, "big"))
        session.send(data)