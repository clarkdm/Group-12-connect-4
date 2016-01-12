
class Motor_Controller:


 	def __init__(self,time,sys,GPIO,Motor):
		

		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)




		home_pin = 14



		StepPins_1 = [22,27,17,4]    #1 	R3
		StepPins_2 = [7,8,25,24]      #2 	G
		StepPins_3 = [23,9,11,5]     #3		B
		StepPins_4 = [26,19,13,6]    #4		R1
		StepPins_5 = [21,20,16,12]   #5		R2

		self.M1 = Motor.Motor(GPIO, sys, time, StepPins_1, "Motor 1", home_pin)
		self.M2 = Motor.Motor(GPIO, sys, time, StepPins_2, "Motor 2", home_pin)
		self.M3 = Motor.Motor(GPIO, sys, time, StepPins_3, "Motor 3", home_pin)
		self.M4 = Motor.Motor(GPIO, sys, time, StepPins_4, "Motor 4", home_pin)
		self.M5 = Motor.Motor(GPIO, sys, time, StepPins_5, "Motor 5", home_pin)






	def off(self,GPIO):
		self.M1.off(GPIO)
		self.M2.off(GPIO)
		self.M3.off(GPIO)
		self.M4.off(GPIO)
		self.M5.off(GPIO)

	def home(self,GPIO):
		self.M1.home()
		#self.M2.home()
		self.M3.home()
		self.M4.home()
		self.M5.home()

	def go_to_base(self):

		self.M1.go_to_base()
		#self.M2.go_to_base()
		self.M3.go_to_base()
		self.M4.go_to_base()
		self.M5.go_to_base()




	def go_to_column_0(self):
		self.M5.go_to(2900)
		self.M1.go_to(300)
		self.M3.go_to(4900)
		self.M4.go_to(2450)



	def go_to_column_1(self):
		self.M5.go_to(2800)
		self.M1.go_to(400)
		self.M3.go_to(4700)
		self.M4.go_to(2450)

		

	def go_to_column_2(self):
		self.M5.go_to(2450)
		self.M1.go_to(800)
		self.M3.go_to(4400)
		self.M4.go_to(2050)

		

	def go_to_column_3(self):
		self.M5.go_to(2280)
		self.M1.go_to(self.M1.base)
		self.M3.go_to(4200)
		self.M4.go_to(2150)

		

	def go_to_column_4(self):
		self.M5.go_to(2280)
		self.M1.go_to(self.M1.base)
		self.M3.go_to(self.M3.base)
		self.M4.go_to(2150)

		

	def go_to_column_5(self):
		self.M5.go_to(self.M5.base)
		self.M1.go_to(self.M1.base)
		self.M3.go_to(self.M3.base)
		self.M4.go_to(self.M4.base)

		

	def go_to_column_6(self):
		self.M5.go_to(self.M5.base)
		self.M1.go_to(self.M1.base)
		self.M3.go_to(self.M3.base)
		self.M4.go_to(self.M4.base)

	def open_grabber(self):
		self.M2.run_m(-1, 1200)


	


	


