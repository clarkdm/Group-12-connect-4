#gpio_test_2

import time
import sys
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class Motor:
    
    

    def __init__(self, GPIO, StepPins, temp, home_pin):
        print temp
        self.home_pin = home_pin
        self.position = 0
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
          
        #self.home()


    def  home(self):
        
        home = False
        while home == False:



            input_state = GPIO.input(self.home_pin)

            if input_state == False:
                home = True
                print('Button Pressed')
                time.sleep(0.2)
            else: 
                self.run_m(0, 1)

        self.position = 0
        

      

    def  run_m(self, StepDir, num_steps):
        x = 0
        
        if StepDir == 0 :
            StepDir = -1
        while x < num_steps:
 
            print self.StepCounter
           
             
            for pin in range(0, 4):
                xpin = self.StepPins[pin]
                if self.Seq[self.StepCounter][pin]!=0:
                    print " Enable GPIO %i" %(xpin)
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)
             
            self.StepCounter += StepDir
             
            
            if (self.StepCounter>=self.StepCount):
                self.StepCounter = 0

            if (self.StepCounter<0):
                self.StepCounter = self.StepCount+StepDir
            self.position = self.position + StepDir
            x = x + 1
            


            print " %i < %i" %(x, num_steps)
            time.sleep(self.WaitTime)
        
        
    def go_to(self,destination):


        if destination < self.position:
            self.run_m(0,(self.position - destination))
        elif destination > self.position:
            self.run_m(1,(destination - self.position))
        





home_pin = 14



StepPins_1 = [4,17,27,22]    #1
StepPins_2 = [24,25,8,7]      #2
StepPins_3 = [23,9,11,5]     #3
StepPins_4 = [6,13,19,26]    #4
StepPins_5 = [12,16,20,21]   #5


M1 = Motor(GPIO, StepPins_1, "1", home_pin)
M2 = Motor(GPIO, StepPins_2, "2", home_pin)
M3 = Motor(GPIO, StepPins_3, "3", home_pin)
M4 = Motor(GPIO, StepPins_4, "4", home_pin)
M5 = Motor(GPIO, StepPins_5, "5", home_pin)


#M5.home()

M5.run_m(0, 100)
#print StepCounter_5 + " : StepCounter_5 test"
#M1.run_m(1, 1000)
print M5.position



#M2.run_m(1, 1500)


#M1.run_m(-1, 1000)




#M2.run_m(-1, 1500)



#M3.run_m(1, 1000)



#M4.run_m(1, 1000)



#M5.run_m(1, 1000)



GPIO.cleanup() 
 