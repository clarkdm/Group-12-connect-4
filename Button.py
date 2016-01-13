
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin=18
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(pin)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)