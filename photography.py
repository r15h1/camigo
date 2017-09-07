import sys, cv2, os
import numpy as np
import datetime
from time import sleep


class photographer:
    def __init__(self, imageLocation, cascadePath):
        self.imageLocation = imageLocation
        self.cascadePath = cascadePath

    #take pictures of the subject
    def shoot(self, numPictures):
        faceCascade = cv2.CascadeClassifier(self.cascadePath)
        cap = cv2.VideoCapture(0)        
        pic = 0
        while pic <= numPictures:
            ret, frame = cap.read()            
            cv2.imshow('video', frame) 
            hasFace = self.hasFace(frame, faceCascade)            
            filename = os.path.join(self.imageLocation, "{0}.jpg".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
            
            if hasFace == True:
                print "saving picture: ", pic, "file: ", filename
                cv2.imwrite(filename, frame)
                pic = pic + 1
            sleep(0.5) 

        cap.release()
        cv2.destroyAllWindows()


    def hasFace(self, frame, faceCascade):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        roi = None
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            if (w > 0 and h > 0):
                roi = frame[y:y+h, x:x+w]
        
        if roi is not None:
            if roi.size:        
                return True

        return False