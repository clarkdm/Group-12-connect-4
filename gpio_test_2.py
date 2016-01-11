#gpio_test_2

import time
import sys
import RPi.GPIO as GPIO
import lcddriver # LCD
GPIO.cleanup() 
lcd = lcddriver.lcd()
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class Motor:
    
    

    def __init__(self, GPIO, StepPins, temp, home_pin):
        print temp
        self.base = 400
        self.home_pin = home_pin
        self.position = 0
        self.StepPins = StepPins
        for pin in self.StepPins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, False)
            print "Setup pins %i" %(pin)
        # Define advanced sequence\\\
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
        self.StepCounter = 0 
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
                self.run_m(2, 2)

        self.position = 0
        self.run_m(-2, 400)
        

    def go_to_base(self):
        self.go_to_fast(self.base)

    def set_base(self, base):
        self.base = base

    def  run_m(self, StepDir, num_steps):
        x = 0
        
        if StepDir == 0 :
            StepDir = -1

        if StepDir == 2:
            num_steps = num_steps / 2
        if StepDir == -2:
            num_steps = num_steps / 2
        while x < num_steps:
 
           # print self.StepCounter
           # print x
             
            for pin in range(0, 4):
                xpin = self.StepPins[pin]
                if self.Seq[self.StepCounter][pin]!=0:
                #    print " Enable GPIO %i" %(xpin)
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)
             
            self.StepCounter += StepDir
             
            
            if (self.StepCounter>=self.StepCount):
                self.StepCounter = 0

            if (self.StepCounter<0):
                self.StepCounter = self.StepCount+StepDir
            self.position = self.position - StepDir
            x = x + 1
            


           # print " %i < %i" %(x, num_steps)
            time.sleep(self.WaitTime)
        
        
    def go_to(self,destination):
        print destination - self.position

        if destination < self.position:
            travel = self.position - destination
            self.run_m(1,travel)

        elif destination > self.position:
            travel = destination - self.position
            self.run_m(-1,travel)

    def go_to_fast(self,destination):
        print destination - self.position

        if destination < self.position:
            travel = self.position - destination
            self.run_m(2,travel)

        elif destination > self.position:
            travel = destination - self.position
            self.run_m(-2,travel)

    def grt_position(self):
        return self.position






home_pin = 14



StepPins_1 = [22,27,17,4]    #1
StepPins_2 = [24,25,8,7]      #2
StepPins_3 = [23,9,11,5]     #3
StepPins_4 = [26,19,13,6]    #4
StepPins_5 = [21,20,16,12]   #5

M1 = Motor(GPIO, StepPins_1, "1", home_pin)
M2 = Motor(GPIO, StepPins_2, "2", home_pin)
M3 = Motor(GPIO, StepPins_3, "3", home_pin)
M4 = Motor(GPIO, StepPins_4, "4", home_pin)
M5 = Motor(GPIO, StepPins_5, "5", home_pin)


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

 