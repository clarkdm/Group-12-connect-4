import picamera
import numpy as np
import pylab
import cv2
import mahotas as mh
from time import sleep

camera = picamera.PiCamera()



camera.start_preview()
sleep(50)
camera.stop_preview()

camera.capture('image.jpg')






