import board
import neopixel
import time

class leds:
    def __init__(self, num_pixels):
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(board.D18, num_pixels, auto_write = False, pixel_order=neopixel.GRB)
    
    def setColor(self, color):
        self.pixels.fill(color)
        self.pixels.show()

    def setOff(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()

    def flash(self, duration, color):
        self.setColor(color)
        time.sleep(duration)
        self.setOff()
        time.sleep(duration)

if __name__ == "__main__":
    l = leds(10)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    while True:
        l.flash(0.5)