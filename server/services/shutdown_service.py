import subprocess


class Shutdown_Service():
    def shutdown(self):
        try:
            subprocess.run(["shutdown", "/s", "/f", "/t", "15"])
        except Exception as e:
            print(f"Error sending shutdown command: {e}")