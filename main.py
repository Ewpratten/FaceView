import urllib
import cv2
import numpy as np
import urllib.request

# def sendState(x):
#
cascPath = "haarcascade_frontalface_default.xml"
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
ahg = ''
while ahg != 'r':

    with urllib.request.urlopen("http://172.16.10.241:8080/shot.jpg") as url:
        imgReard = url.read()
    imgNp = np.array(bytearray(imgReard), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)

    img = cv2.resize(img, (570, 340))
    image = img

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    # print("h")
    # print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("Face Found At: " + str(x) + ", " + str(y))

    cv2.imshow("Faces found", image)
    cv2.waitKey(10)
