import RPi.GPIO as GPIO
import time
GPIO.cleanup()  
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(14)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)


