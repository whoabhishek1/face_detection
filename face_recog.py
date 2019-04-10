#made by abhishek tripathi!
import cv2




cam = cv2.VideoCapture(0)
face_cascade= cv2.CascadeClassifier('lbpcascade_frontalface_improved.xml')
while 1:
    _,image = cam.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,8)
    #x,y,w,h
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),5)
    cv2.imshow("frame",image)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cam.release()
cv2.destroyAllWindows()






