import io

from PIL import Image
import mss

class Screenshot_Service:
    def capture(self):
        with mss.mss() as s:
            monitor = s.monitors[1]

            screenshot = s.grab(monitor)

            img = Image.frombytes(
                "RGB",
                screenshot.size,
                screenshot.rgb
            )

            buffer = io.BytesIO()

            img.save(
                buffer,
                format="PNG"
            )

            return buffer.getvalue()
               
    