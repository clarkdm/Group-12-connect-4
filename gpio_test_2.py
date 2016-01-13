#gpio_test_2

import time
import sys
import RPi.GPIO as GPIO
import lcddriver # LCD
import Motor


lcd = lcddriver.lcd()
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)




home_pin = 14



StepPins_1 = [22,27,17,4]    #1
StepPins_2 = [24,25,8,7]      #2
StepPins_3 = [23,9,11,5]     #3
StepPins_4 = [26,19,13,6]    #4
StepPins_5 = [21,20,16,12]   #5

M1 = Motor.Motor(GPIO, sys, time, StepPins_1, "Motor 1", home_pin)
M2 = Motor.Motor(GPIO, sys, time, StepPins_2, "Motor 2", home_pin)
M3 = Motor.Motor(GPIO, sys, time, StepPins_3, "Motor 3", home_pin)
M4 = Motor.Motor(GPIO, sys, time, StepPins_4, "Motor 4", home_pin)
M5 = Motor.Motor(GPIO, sys, time, StepPins_5, "Motor 5", home_pin)


M1.set_base(1250)
#M2.set_base(400)
M3.set_base(3700)
M4.set_base(1000)
M5.set_base(1500)


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

#M4.home()

#M5.home()


#M4.home()
#M5.home()
#print M5.position
#M5.go_to_fast(3000)
#print M5.position


#lcd.lcd_display_string("M5", 1)
#lcd.lcd_display_string(str(M5.position), 2)











#M1.run_m(-1, 400)       ## R3 1


#M2.run_m(1, 400)        ## G 1




#M3.run_m(1, 400)        ## B 1



#M4.run_m(-1, 400)        ## R1 -1



#M5.run_m(1, 400)       ## R2 -1



#M5.run_m(1, 1000)


GPIO.cleanup() 

 