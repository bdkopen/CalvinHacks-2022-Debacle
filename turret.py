from stepper import Stepper
import time

class Turret():
    def __init__(self):
        self.camStepper = Stepper(1, 22, 23, 24)
        self.turnStepper = Stepper(2, 5, 6, 12)
        self.tiltStepper = Stepper(3, 4, 13, 26)

    def test(self):
        self.camStepper.move(True, 10000, 0.0002)
        self.camStepper.move(False, 10000, 0.0002)

    def adjust(self, dx, dy):
        self.turnStepper.move(True, dx, 0.0015)
        self.tiltStepper.move(False, dy, 0.0002)

    def fire(self):
        self.camStepper.move(True, 800, 0.0003)

if __name__ == "__main__":
    myTurret = Turret()
    while True:
        myTurret.adjust(100,1000)
        myTurret.fire()
        time.sleep(2)
