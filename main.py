import sys
import os
from trainer import trainer

options = "1. take someone's photo\n2. train system\n3. arm system\n4. exit"
cascade = os.getcwd() + "/haarcascade_frontalface_default.xml"
imageRoot= os.path.join(os.getcwd(), "images")

def run():    
    while True:
        print "\n----------camera with face regcognition----------------"

        prompt = "select an option:\n{0}\ncamigo:\\>"
        option = raw_input(prompt.format(options))
        if option == "4":
            print "see you later mater"
            break;
        elif option == "3":
            armSystem()
        elif option == "2":
            trainSystem()
        elif option == "1":
            setUpFace()

def trainSystem():    
    t = trainer(imageRoot, cascade)
    t.train()
    pass

def armSystem():
    print "arming system"
    from watcher import watcher
    watcher = watcher(imageRoot, cascade)
    watcher.watch()
    pass


def setUpFace():
    name = raw_input("enter your name (letters only, no space):\ncamigo:\\>")    
    imageLocation =  os.path.join(imageRoot, name)
    if not os.path.exists(imageLocation):
        os.makedirs(imageLocation)
    
    print "please stand in front of the camera for a moment, be natural and try different facial expressions"
    from photography import photographer
    photographer = photographer(imageLocation, cascade)
    photographer.shoot(50)

run()