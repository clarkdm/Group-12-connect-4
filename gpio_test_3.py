#gpio_test_3

import time
import sys
import RPi.GPIO as GPIO
import lcddriver # LCD
import Motor


lcd = lcddriver.lcd()
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)




home_pin = 14



StepPins_1 = [22,27,17,4]    #1 	R3
StepPins_2 = [7,8,25,24]      #2 	G
StepPins_3 = [23,9,11,5]     #3		B
StepPins_4 = [26,19,13,6]    #4		R1
StepPins_5 = [21,20,16,12]   #5		R2

M1 = Motor.Motor(GPIO, sys, time, StepPins_1, "Motor 1", home_pin)
M2 = Motor.Motor(GPIO, sys, time, StepPins_2, "Motor 2", home_pin)
M3 = Motor.Motor(GPIO, sys, time, StepPins_3, "Motor 3", home_pin)
M4 = Motor.Motor(GPIO, sys, time, StepPins_4, "Motor 4", home_pin)
M5 = Motor.Motor(GPIO, sys, time, StepPins_5, "Motor 5", home_pin)


M1.set_base(1250)
#M2.set_base(400)
M3.set_base(3700)
M4.set_base(1000)
M5.set_base(4800)


M1.home()
#M2.home()
M3.home()
M4.home()
M5.home()





M5.go_to_base()
lcd.lcd_display_string("M5  2", 1)
lcd.lcd_display_string(str(M5.position), 2)

M1.go_to_base()
lcd.lcd_display_string("M1  3", 1)
lcd.lcd_display_string(str(M1.position), 2)

M3.go_to_base()
lcd.lcd_display_string("M3  4", 1)
lcd.lcd_display_string(str(M3.position), 2)

M4.go_to_base()
lcd.lcd_display_string("M4  5", 1)
lcd.lcd_display_string(str(M4.position), 2)

M5.go_to_base()
lcd.lcd_display_string("M5   6", 1)
lcd.lcd_display_string(str(M5.position), 2)





M5.go_to(2500)
M3.go_to(4700)
M1.go_to(600)
M4.go_to(2400)
M2.run_m(-1, 1200)



lcd.lcd_display_string(str(M4.position), 1)
lcd.lcd_display_string(str(M5.position), 2)


#lcd.lcd_display_string('Button M5', 1)

#x = True

#while x:

 #   input_state = GPIO.input(home_pin)
 #   M5.run_m(2 , 10)
	

 #   if input_state == False:
  #      print('Button Pressed    ')
  #      x = False


lcd.lcd_display_string(str(M5.position), 2)




GPIO.cleanup() 

 