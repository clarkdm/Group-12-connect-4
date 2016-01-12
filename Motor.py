class Motor:
    

    def __init__(self, GPIO, sys, time, StepPins, temp, home_pin):
        print temp
        self.GPIO = GPIO
        self.time = time
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

    def off(self, GPIO):

        for pin in range(0, 4):
                xpin = self.StepPins[pin]
               
                self.GPIO.output(xpin, False)



    def  home(self):
        
        home = False
        while home == False:



            input_state = self.GPIO.input(self.home_pin)

            if input_state == False:
                home = True
                print('Button Pressed')
                self.time.sleep(0.2)
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
                    self.GPIO.output(xpin, True)
                else:
                    self.GPIO.output(xpin, False)
             
            self.StepCounter += StepDir
             
            
            if (self.StepCounter>=self.StepCount):
                self.StepCounter = 0

            if (self.StepCounter<0):
                self.StepCounter = self.StepCount+StepDir
            self.position = self.position - StepDir
            x = x + 1
            


           # print " %i < %i" %(x, num_steps)
            self.time.sleep(self.WaitTime)
        
        
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