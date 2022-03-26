from stepper import Stepper

class Turret():
    def __init__(self):
        self.camStepper = Stepper(1, 22, 23, 24)
        self.turnStepper = Stepper(2, 5, 6, 12)
        self.tiltStepper = Stepper(3, 4, 13, 26)

    def test(self):
        self.camStepper.move(True, 10000, 0.0001)
        self.camStepper.move(False, 10000, 0.0001)

    def adjust(self, dx, dy):
        self.turnStepper.move(True, dx, 0.0001)
        self.tiltStepper.move(True, dy, 0.0001)

    def fire(self):
        self.camStepper.move(True, 800, 0.0001)