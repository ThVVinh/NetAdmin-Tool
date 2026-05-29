import json


class ProcessHandler:
    def __init__(self, process_service):
        self.process_service = process_service

    def handle(self, session):
        while True:
            signal = session.read_line()

            if signal == "XEM":
                processes = self.process_service.get_processes()

                self.send_processes(
                    session,
                    processes
                )

            elif signal == "KILL":
                pid = session.read_line()
                print("KILL PID:", pid)
                self.process_service.kill_process(pid)
                
            elif signal == "START":
                process_name = session.read_line()
                print("START Process:", process_name)
                self.process_service.start_process(process_name)

            elif signal == "QUIT":
                break
            
    def send_processes(self, session, processes):
        data = json.dumps(processes).encode("utf-8")
        session.send(len(data).to_bytes(4, "big"))
        session.send(data)