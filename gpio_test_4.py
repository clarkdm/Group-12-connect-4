#gpio_test_4


import time
import sys
import RPi.GPIO as GPIO
import lcddriver # LCD
import Motor
import Motor_Controller as MC

arm = MC.Motor_Controller(time,sys,GPIO,Motor)


arm.home(GPIO)

arm.go_to_base()

arm.go_to_column_1()

arm.open_grabber()

arm.off(GPIO)





GPIO.cleanup() 
















































