import numpy as np
import cv2
import matplotlib.pyplot as plt
import time 


camera = cv2.VideoCapture(0)
i = 0
while True:
	i = i+1
	return_value, image = camera.read()
	time.sleep(5)
	cv2.imwrite('img'+str(i)+'.jpg', image)
	cv2.imshow('ORIGINAL' , image)


	if cv2.waitKey(30) & 0xFF == ord('q'):
		break
	else: 
		continue

n = i-1
arr = np.zeros((1,n))
h = n/2
#print(h)

for i in range(1,n+1):
	
	
	img = cv2.imread("img"+str(i)+".jpg" , 0) #base images from webcam saves as: img1,img2....imgn

	template = cv2.imread('template.jpg' , 0)  #random_test_image saved on pc
	
	orb = cv2.ORB_create()

	kp1 , des1 = orb.detectAndCompute(img,None)
	kp2 , des2 = orb.detectAndCompute(template,None)


	bf = cv2.BFMatcher() 

	matches = bf.knnMatch(des1,des2,k=2)

	print("\n****************************\n")
	print(len(matches))
	print("\n****************************\n")

	good = []

	print("\n++++++++++++++++++++++++++++\n")
	print(len(good))
	print("\n++++++++++++++++++++++++++++\n")

	for m,n in matches:
    		if m.distance <  0.7*n.distance:   #threshold value
       		 good.append(m)                    #finding best matches

	print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
	print(len(good))
	print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")


	c = len(good)

#	img_ft = cv2.drawMatches(img,kp1,template,kp2,good,None,flags = 2 )
#	plt.imshow(img)
#	plt.show() 

	if c >= 6:  #if more than 6 good matches found
		arr[0][i-1] = 1

	else:
		arr[0][i-1] = 0


t = np.sum(arr)
print(t)

if t >= h:       #if the template matches with more that 50% of the images, print yes.
	print("Yes")
else:
	print("No")

