import cv2

video_capture = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

while True:
    ret, image = video_capture.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for(x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h),(255,0,0),2)
        smile_cascade.detectMultiScale(gray, 1.1, 5)
        print("Image Saved")
        output_path("C:/Users/jcenr/Pictures/image_0.jpg", image)

    cv2.imshow('live_video', image)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()







