import psutil


class ProcessService:
    def get_processes(self):
        result = []

        for proc in psutil.process_iter(
            attrs=['pid', 'name', 'num_threads']
        ):

            try:
                result.append({
                    "name": proc.info["name"],
                    "pid": proc.info["pid"],
                    "threads": proc.info["num_threads"]
                })

            except:
                pass

        return result
    

    def kill_process(self, pid):
        process = psutil.Process(int(pid))

        process.terminate()

    def start_process(self, name):
        psutil.Popen(name)