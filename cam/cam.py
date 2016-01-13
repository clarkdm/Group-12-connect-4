









class cam:
    import numpy as np
    import cv2
    from matplotlib import pyplot as plt
    from PIL import Image
    import picamera


    def __init__(self):
        
        self.camera = picamera.PiCamera()
        self.coordinates = [[[300, 990],[300, 825],[300, 665],[300, 516],[300, 366],[300, 217]],[[440, 990],[440, 825],[440, 665],[440, 510],[440, 350],[440, 210]],[[600, 990],[600, 825],[600, 665],[600, 490],[600, 333],[600, 179]],[[770, 990],[770, 825],[770, 665],[770, 475],[770, 316],[770, 153]],[[930, 991],[930, 800],[930, 634],[930, 462],[930, 291],[930, 133]],[[1110, 986],[1110, 796],[1110, 614],[1110, 442],[1110, 267],[1110, 106]],[[1340, 990],[1340, 800],[1340, 608],[1314, 427],[1293, 254],[1293, 82]]]
            #coordinates = [column [rule [X,Y]]]


    def getstat():
        



        self.camera.capture('image.jpg')

        frame = cv2.imread('image.jpg')


            # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)

            # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

            # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        ret,mask = cv2.threshold(mask,127,255,cv2.THRESH_BINARY_INV)
            # Bitwise-AND mask and original image



        kernel = np.ones((15,15),np.uint8)
        mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel, iterations = 2)


        res = cv2.bitwise_and(frame,frame, mask= mask)

        ret,mask = cv2.threshold(mask,127,255,cv2.THRESH_BINARY_INV)







        cv2.imwrite('image2_frame.jpg',frame)
        cv2.imwrite('image3_mask.jpg',mask)
        cv2.imwrite('image2_res.jpg',res)






        im = Image.open("image3_mask.jpg") 
        pix = im.load()

        c = 0
        r = 0
        while c < 7:
            while r < 6:

                pix = pix[self.coordinates[c][r][0], self.coordinates[c][r][1]]
                if pix = 0:
                    pass
                    board[c][r] = 0
                else:
                    board[c][r] = 1
               r = r + 1
            r = 0
            c = c + 1
        return board



















