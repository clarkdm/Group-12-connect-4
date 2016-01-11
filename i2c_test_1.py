import lcddriver
from time import *

lcd = lcddriver.lcd()

lcd.lcd_display_string("Hello world", 1)
lcd.lcd_display_string("My name is", 2)
#from
#https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=34261&p=378524