__author__ = 'ashik'

import numpy
import scipy
import cv2
import intrusion as movement
from alarm import IntrusionAlarm as AlarmRing

cascPath = "haarcascade_frontalface_default.xml"
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=1
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (55, 200, 70), 1)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 34), 1)
            # print("Detected {0} faces".format(len(faces)))
            # print(list(faces))
            # print("Eyes: {0}".format(len(eyes)))
            # print(list(eyes))
            # checking if there is 2 eyes against every single face
            if len(faces) * 2 == len(eyes):
                print("I think there is a human in front of the camera!")
                t = AlarmRing()
                t.run()

    # Display the resulting frame
    cv2.imshow('Virtual Eye', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
