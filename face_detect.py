import cv2
#face=cv2.CascadeClassifier("C://Users//SIVA KOTESWARARAO//AppData//Roaming//Python//Python310//site-packages//cv2//data//haarcascade_frontalface_default.xml")
eyes=cv2.CascadeClassifier("C:\\Users\\SIVA KOTESWARARAO\\AppData\\Roaming\\Python\\Python310\\site-packages\\cv2\\data\\haarcascade_eye.xml")

cap=cv2.VideoCapture(0) #("D://siva python//COMPUTER VISION//VIDEOS_CV//video_of_people_walking.mp4")   #video_of_people_walking

while(True):
    ret,frame=cap.read()
    frame=cv2.resize(frame,(400,400))
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detection=eyes.detectMultiScale(frame,scaleFactor=1.3,minNeighbors=5)

    if(len(detection)>0):
        
        (x,y,w,h)=detection[0]
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("frame",frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
             break

cap.release()
cv2.destroyAllWindows()
