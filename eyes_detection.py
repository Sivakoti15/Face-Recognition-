import cv2

cam=cv2.VideoCapture(0)

eye = cv2.CascadeClassifier("C://Users//SIVA KOTESWARARAO//AppData//Roaming//Python//Python310//site-packages//cv2//data//haarcascade_eye.xml")

while True:
    siva,frame=cam.read()

    detect = eye.detectMultiScale(frame,scaleFactor=1.3,minNeighbors=5)

    for (x,y,w,h) in detect:
        cv2.circle(frame,(x+27,y+27),20,(0,0,0),5)


    cv2.imshow("eyes_detection",frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
