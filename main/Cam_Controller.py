
class Cam_Controller:
	

 	def __init__(self):
		

		self.board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
		for c in xrange(0,6):
			for r in xrange(0,5):

				self.board[c][r] = 0
 		
		

	def get_new_move(self, cam, picamera, Image, cv2, np):
		x = True
		while x:
			camera = cam.cam(picamera)	
			new_board = camera.getstat(picamera, Image, cv2, np)
			c = 0
			r = 0	 
			for c in xrange(0,6):
				for r in xrange(0,5):
					print new_board[c][r]
					if self.board[c][r] == new_board[c][r]:
        
        

						self.board[c][r] = 1
						x = False
						return c

  					