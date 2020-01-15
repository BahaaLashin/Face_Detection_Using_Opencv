import cv2 
import matplotlib.pyplot as plt
image = cv2.imread('team.jpg')

classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

faces = classifier.detectMultiScale(image)


for face in faces:

    x,y,w,h = face

    cv2.rectangle(image,(x,y),(x+w,h+y),[255,0,0],4)

cv2.imshow('Imahe',image)
cv2.waitKey(0)
cv2.destroyAllWindows()