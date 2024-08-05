import numpy as np
import cv2
np.set_printoptions(threshold=np.inf)

#images stored as web_x, waves_x etc., x=1,2,3,....

#im = cv2.imread('web_1.jpg' ,1)   #images downloaded from web
im = cv2.imread('waves_1.jpg' , 1) #bucket images 
#im = cv2.imread('still_2.jpg',1) 
#im = cv2.imread('no_oil.jpg',1)

imgr = cv2.resize(im,(1000,1300)) #resizing

cv2.imshow('Actual Image' , imgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

b,g,r = cv2.split(imgr)  #splitting colour channels of the image

#thresholding
#ret, thresh = cv2.threshold(r, 100, 255, cv2.THRESH_BINARY_INV) # if images are like web imgs. threshold = 100

ret, thresh = cv2.threshold(r, 130, 255, cv2.THRESH_BINARY) # if images are like bucket imgs. threshold = 130

'''
imgray = cv2.cvtColor(imgr, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 130, 255, cv2.THRESH_BINARY_INV) #imgray more suitable for bucket like images
'''

#finding contours
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

'''
print(type(contours))
'''

#Selecting contours with area greater than threshold value(100 or 10000) as per image category.

f = open("coordinates_1.txt" , "w") #should be put in for-loop for every image by iterating filename for each image

areas = [cv2.contourArea(c) for c in contours]

indices = [i for i,v in enumerate(areas) if v>10000] #parameter tuning required, (v>100 for web imgs), (v>10000 for bucket imgs)
print('\nIndices of contours with area greater than threshold value')
print(indices)

f.write('\nIndices of contours with area greater than threshold value')
f.write('\n%s\n' %indices)
f.write('\n\n')

for i in indices:
	cv2.drawContours(imgr, contours, i, (50,255,50), 3)
	'''	
	cv2.imshow('Contours' , imgr) #To view each contour separately
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	'''
	'''	
	print('\nContour[%d]\n') %i
	print(contours[i])
	print('********************************************************************************************')
	'''
	f.write("\nThe coordinates of Contour[%d] are:\n\n%s" %(i,contours[i] ))
	f.write('\n\n')
	

print('\n')

f.close()

cv2.imshow('thresh' , thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Contours' , imgr) #View all contours drawn on the image
cv2.waitKey(0)
cv2.destroyAllWindows()

