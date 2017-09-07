import sys, cv2, os
import numpy as np

class trainer:
    def __init__(self, imageRoot, cascadePath):
        self.imageRoot = imageRoot
        self.cascadePath = cascadePath

    def train(self):        
        print "training the system to recognize faces"        
        faceCascade = cv2.CascadeClassifier(self.cascadePath)
        recognizer = cv2.face.createLBPHFaceRecognizer()
        images, labels = self.getImagesAndLabels(self.imageRoot)        
        recognizer.train(images, np.array(labels))
        recognizer.save('trainer.yml')

    def getImagesAndLabels(self, path):
        #get list of all subdirectories
        persons = next(os.walk(path))[1]        
        nbr = 0        
        images = []            
        labels = []

        print "found images for ", persons
        for person in persons:
            nbr = nbr + 1            
            personFileLocation = os.path.join(path, person)
            imagePaths = [os.path.join(personFileLocation, f) for f in os.listdir(personFileLocation)]            
            faceCascade = cv2.CascadeClassifier(self.cascadePath)
            count = 0
            for imagePath in imagePaths:
                count = count + 1
                # Read the image and convert to grayscale
                imagePil = cv2.imread(imagePath, 0)
                # Convert the image format into numpy array
                image = np.array(imagePil, 'uint8')
                
                # Detect the face in the image
                faces = faceCascade.detectMultiScale(image, 
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=cv2.CASCADE_SCALE_IMAGE
                )
                # If face is detected, append the face to images and the label to labels
                for (x, y, w, h) in faces:
                    print "adding image ", nbr, " - ", person, count
                    images.append(image[y: y + h, x: x + w])
                    labels.append(nbr)

        return images, labels