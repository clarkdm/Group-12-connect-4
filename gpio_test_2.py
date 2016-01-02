#gpio_test_2

import time
import sys
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)


class Motor:
    
    

    def __init__(self, GPIO, StepPins, temp):
        print temp
        self.StepPins = StepPins
        for pin in self.StepPins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, False)
            print "Setup pins %i" %(pin)
        # Define advanced sequence
        # as shown in manufacturers datasheet
        self.Seq = [[1,0,0,1],
               [1,0,0,0],
               [1,1,0,0],
               [0,1,0,0],
               [0,1,1,0],
               [0,0,1,0],
               [0,0,1,1],
               [0,0,0,1]]
                
        self.StepCount = len(self.Seq)
        
        if len(sys.argv)>1:
          self.WaitTime = int(sys.argv[1])/float(1000)
        else:
          self.WaitTime = 10/float(1000)




    def  run_m(self, StepDir, num_steps):
        x = 0
        StepCounter = 0
        while x < num_steps:
 
            print StepCounter
           
             
            for pin in range(0, 4):
                xpin = self.StepPins[pin]
                if self.Seq[StepCounter][pin]!=0:
                    print " Enable GPIO %i" %(xpin)
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)
             
            StepCounter += StepDir
             
            
            if (StepCounter>=self.StepCount):
                StepCounter = 0

            if (StepCounter<0):
                StepCounter = self.StepCount+StepDir

            x = x + 1
            


            print " %i < %i" %(x, num_steps)
            time.sleep(self.WaitTime)
        return 0
           







StepPins_1 = [4,17,27,22]    #1
StepPins_2 = [24,25,8,7]      #2
StepPins_3 = [23,9,11,5]     #3
StepPins_4 = [6,13,19,26]    #4
StepPins_5 = [12,16,20,21]   #5


M1 = Motor(GPIO, StepPins_1, "1")
M2 = Motor(GPIO, StepPins_2, "2")
M3 = Motor(GPIO, StepPins_3, "3")
M4 = Motor(GPIO, StepPins_4, "4")
M5 = Motor(GPIO, StepPins_5, "5")

n=0

n = M1.run_m(1, 1000)




n = M2.run_m(1, 1500)


n = M1.run_m(-1, 1000)




n = M2.run_m(-1, 1500)



n = M3.run_m(1, 1000)



n = M4.run_m(1, 1000)



n = M5.run_m(1, 1000)



GPIO.cleanup() 
 