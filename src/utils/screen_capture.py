from mss import mss
import numpy as np

def capture_screen(monitor={"top": 40, "left": 0, "width": 1280, "height": 720}):
    with mss() as sct:
        screenshot = sct.grab(monitor)
    return np.array(screenshot)