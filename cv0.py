import cv2
import numpy as np
import time
import matplotlib.image as mpimg

get_ipython().run_line_magic('matplotlib', 'inline')
test_photos = 30
camera = cv2.VideoCapture(0)

file = "my_face_"+str(int(time.time()))+".png"
for i in range(test_photos):
    temp = camera.read()[1]
    
print("Taking image...")
camera_capture = camera.read()[1]
cv2.imwrite(file, camera_capture)
del(camera)
print("finish")
img = cv2.imread(file,-1)

cv2.namedWindow("Face")
cv2.startWindowThread()
cv2.imshow('face',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
height, width = img.shape[:2]
img_line=cv2.line(gray_image,(0,0),(width,height),(255,255,0),4)
img_line_rect =cv2.rectangle(img_line,(width//3,height//3),(width*2//3,height*2//3),(0,255,255),6)
cv2.namedWindow("Face_line")
cv2.startWindowThread()
cv2.imshow('gray_face',img_line_rect)
cv2.waitKey(0)
cv2.destroyAllWindows()
