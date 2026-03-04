import cv2

video_capture = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

while True:
    ret, image = video_capture.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h),(0,0,0),3)
        smileCascade.detectMultiScale(gray, 1.8, 15)
        print("Image Saved")
        filename = "D:/output.jpg"
        cv2.imwrite("C:/Users/jcenr/Pictures/image_0.jpg", image)
    cv2.imshow('live video', image)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
video.release()
cv2.destroyAllWindows()







