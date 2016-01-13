#gpio_test_4


import time
import sys
import RPi.GPIO as GPIO
import lcddriver # LCD
import Motor
import Motor_Controller as MC

arm = MC.Motor_Controller(time,sys,GPIO,Motor)

lcd = lcddriver.lcd()

lcd.lcd_display_string("column_3", 1)
arm.home(GPIO)
#arm.off(GPIO)
#arm.go_to_base()
#arm.off(GPIO)
arm.go_to_column_2()
#arm.off(GPIO)
arm.open_grabber()

arm.off(GPIO)
arm.go_to_base()




GPIO.cleanup() 
















































