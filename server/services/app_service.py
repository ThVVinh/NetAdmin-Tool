import re
import subprocess

import psutil


class AppService:
    def get_apps(self):
        processes = subprocess.Popen(
            [
                "powershell",
                "gps",
                "| ? { $_.MainWindowTitle }",
                "| select ProcessName, Id, @{Name='ThreadCount';Expression ={$_.Threads.Count}}, CPU"
            ],
            shell=True,
            stdout=subprocess.PIPE
        ).stdout.readlines()[3:-2]

        processes = [
            process.decode().rstrip()
            for process in processes
        ]

        apps = []

        for process in processes:

            m = re.match(
                r"(.+?) +(\d+) +(\d+) *(\d*,?\d*)",
                process
            )

            if not m:
                continue

            apps.append({
                "name": m.group(1),
                "pid": int(m.group(2)),
                "threads": int(m.group(3))
            })

        return apps

    def kill_app(self, pid):
        try:
            process = psutil.Process(int(pid))
            process.terminate()
                        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return

    def start_app(self, name):
        try:
            process = psutil.Popen(name)
        except Exception as e: 
            return