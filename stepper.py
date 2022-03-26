import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

# direction= 22 # Direction (DIR) GPIO Pin
# step = 23 # Step GPIO Pin
# EN_pin = 24 # enable pin (LOW to enable)

class Stepper():
    def __init__(self, id, direction_pin, step_pin, EN_pin):
        self.id = int(id)
        self.direction_pin = direction_pin
        self.step_pin = step_pin
        self.EN_pin = EN_pin
        self.myMotor = RpiMotorLib.A4988Nema(self.direction_pin, self.step_pin, (21,21,21), "A4988")
        GPIO.setup(EN_pin, GPIO.OUT)   
        print("Stepper ", str(id), " initialized.")     

    def move(self, clockwise, num_steps, step_delay):
        GPIO.output(self.EN_pin, GPIO.LOW)
        print("Stepper ", str(id), " moving ", str(num_steps), " steps. CW = ", str(clockwise))     
        self.myMotor.motor_go(clockwise, "1/4", num_steps, step_delay, False, 0.05)

    def __del__(self):
        GPIO.cleanup()