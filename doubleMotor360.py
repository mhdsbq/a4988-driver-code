import Rpi.GPIO as GPIO
import dualMotorLib 

step_left = 26
step_right = 21
dir_left = 19
dir_right = 20

motors = dualMotorLib.DualMotor(step_left, step_right, dir_left, dir_right)
motors.motors_go(clockwise=False, steps=200, stepdelay=.05, verbose=False, initdelay=0)

GPIO.cleanup()

