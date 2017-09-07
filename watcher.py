import sys, cv2, os
import numpy as np

class watcher:
    def __init__(self, imageRoot, cascadePath):
        self.imageRoot = imageRoot
        self.cascadePath = cascadePath

    def watch(self):
        
        if not os.path.exists('trainer.yml'):        
            print 'The system has not been trained. Please setup faces and train the system'
            return

        knownPersons = next(os.walk(self.imageRoot))[1]   
        print knownPersons
        faceCascade = cv2.CascadeClassifier(self.cascadePath)
        recognizer = cv2.face.createLBPHFaceRecognizer()        
        recognizer.load('trainer.yml')

        print 'loading recognizer and capturing video'
        cap = cv2.VideoCapture(0)        

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            font = cv2.FONT_HERSHEY_SIMPLEX
            roi = None
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                gray = cv2.cvtColor(frame[y:y+h, x:x+w], cv2.COLOR_BGR2GRAY)
                prediction, conf = recognizer.predict(gray)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 250, 100), 2)
                name ="intruder"

                if conf < 65:                
                    name = "{0} {1}".format(knownPersons[prediction - 1], int(conf))
                else:
                    print "intruder alert!!! calling 911"

                cv2.putText(frame,name,(int(x), int(y)), font, 1,(255,255,255),2)
                if (w > 0 and h > 0):
                    roi = frame[y:y+h, x:x+w]

            cv2.imshow('video', frame) 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()