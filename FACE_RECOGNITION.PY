import cv2,os,numpy

face_cas = cv2.CascadeClassifier("C://Users//SIVA KOTESWARARAO//AppData//Roaming//Python//Python310//site-packages//cv2//data//haarcascade_frontalface_default.xml")

dataset = "D:\siva python\PROJECTS\CV_PROJECTS\DATASET"

print("Training.....")

(images,labels,names,id) = ([],[],{},0)

for (subdir,dirs,files) in os.walk(dataset):
    for subdir in dirs:
        names[id]=subdir
        subjectpath = os.path.join(dataset,subdir)

        for filename in os.listdir(subjectpath):
            path = subjectpath+'/'+filename
            label = id
            images.append(cv2.imread(path,0))
            labels.append(int(label))
            #print(label)
        id+=1
(width,height) = (130,100)
(images,labels) = [numpy.array(lis) for lis in[images,labels]]
# print(images,labels)

model = cv2.face.LBPHFaceRecognizer_create()
# model = cv2.face.FisherFaceRecognition_create()

model.train(images,labels)
face_cascade = cv2.CascadeClassifier('C://Users//SIVA KOTESWARARAO//AppData//Roaming//Python//Python310//site-packages//cv2//data//haarcascade_frontalface_default.xml')
webcam=cv2.VideoCapture(0)
cnt=0
while True:
    _,img=webcam.read()
    gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        face=gray[y:y+h,x:x+w]
        face_resize = cv2.resize(face,(width,height))
        prediction = model.predict(face_resize)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

        if prediction[1]<80:
            cv2.putText(img,"%s-%.0f"%(names[prediction[0]],prediction[1]),(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,255,255),2)
            print(names[prediction[0]])
            cnt =0
        else:
            cnt+=1
            cv2.putText(img,'unknown',(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
            if (cnt>100):
                print("unknown person")
                cv2.imwrite("input.jpg",img)
                cnt=0

    cv2.imshow("open-cv",img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
