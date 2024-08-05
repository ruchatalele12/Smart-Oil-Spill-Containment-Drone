from keras.models import *
from keras.preprocessing.image import ImageDataGenerator
import cv2
import numpy as np



classifier = Sequential()
classifier.add(Convolution2D(32,3,3,input_shape=(64,64,3), activation='relu'))
classifier.add (MaxPooling2D(pool_size = (2,2)))
classifier.add(Convolution2D(32,3,3, activation='relu'))
classifier.add (MaxPooling2D(pool_size = (2,2)))
classifier.add(Flatten())
classifier.add(Dense (output_dim = 128 , activation='relu'))
classifier.add(Dense (output_dim = 1 , activation='sigmoid'))
classifier.compile( optimizer ='adam', loss='binary_crossentropy', metrics =['accuracy'])

train_datagen = ImageDataGenerator(

    rescale =1/255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True
    
    )

test_datagen = ImageDataGenerator ( rescale= 1/255)
train_data = train_datagen.flow_from_directory(
  'oilspill/training',
  target_size = (64,64),
  batch_size = 32,
  class_mode ='binary'

  )

inter = test_datagen.flow_from_directory(
  'oilspill/testing',
  target_size = (64,64),
  batch_size = 32,
  class_mode = 'binary'

    )

classifier.fit_generator(
                    train_data,
                    samples_per_epoch =8000,
                    nb_epoch =  25,
                    validation_data = inter,
                    nb_val_samples = 2000
                         )


# Training images stored in oilspill/training directory
# Testing image stored in oilspill/testing directory
# Testing using opencv SURF and ORB code..

orb = cv2.ORB_create()
bf = cv2.BFMatcher()
training_image_location ='oilspill/testing/positive_samples'
test_image = cv2.imread('wave1.jpg')
plus =0
length_training_data = 1000
kp1, des1 = orb.detectAndCompute(test_image,None)
for i in range (1000):
    image_train_compare = cv2.imread('wave1.jpg')
    kp2,des2 = orb.detectAndCompute(image_train_compare,None)
    matches = bf.knnMatch(des1,des2,k=2)
    for m,n in matcches:
        if m.distance < 0.7 * n.distance:    # 70 percent threshold
            plus+=1

if (plus > 800 ):           # if more than 800 out of 1000 traning + oil spill image match with the single test image with threshold > 70 percent
    print ("oil detected")
else:
    print ("no oil detected")


