import cv2
import random

video=cv2.VideoCapture('cars.mp4')

# our pre_trained car classifier
classifier_data='cars1.xml'
car_tracker=cv2.CascadeClassifier(classifier_data)

while True:
    # Read current frame
    read_successful,frame=video.read()
    
    if read_successful:
        
        # convert image to grayscale
        grayscale_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect the cars
    cars=car_tracker.detectMultiScale(grayscale_frame)
    # Make rectangles

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    # Display the frame
    cv2.imshow("--CAR_DETECTOR--",frame)
    key=cv2.waitKey(1)

 # stop if Q key is presssed
    if key==81 or key==113:
        break





print("code completed")


'''

# create opencv image
img=cv2.imread('car_im.jpg')

# create car classifier
car_tracker=cv2.CascadeClassifier(classifier_data)




# convert image to grayscale
grayscale_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detect cars
cars=car_tracker.detectMultiScale(grayscale_img)


for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


# Display the image  with faces spotted
cv2.imshow("--CAR_DETECTOR--",img)
cv2.waitKey()
print("code completed")
'''