# camigo
Camigo is a python app that attempts to recognize people faces streamed via a camera (or webcam) using haar cascade.
Pre-requisites: python 2.7, opencv, numpy

Usage: python camigo.py

When application runs, it presents 4 menu options:
1. take photo
2. train system
3. arm system
4. exit

To set up someone's face, select option 1. This will prompt to enter the person's name (specify with no spaces). The system will take a set up pictures (50) and store them in a folder named after the person. Repeat this procedure to setup a different person.

Once everyone's pictures are taken, select option 2 to train the system.

Then select option 3 to arm the system which will start the camera and display a green rectangle around people's faces with their name. If the system cannot recognise the person, it will display "intruder" as the name.
