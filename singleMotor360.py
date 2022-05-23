import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib
    
#define GPIO pins
GPIO_pins = (-1, -1, -1) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 20       # Direction -> GPIO Pin
step = 21      # Step -> GPIO Pin

# Declare an named instance of class pass GPIO pins numbers
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")


# call the function, pass the arguments
# clockwise=False, steptype="Full", steps=200, stepdelay=.0.1, verbose=True, initdelay=.05
mymotortest.motor_go(False, "Full" , 200, .01, True, .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()