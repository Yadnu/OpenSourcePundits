import cv2
import os
from time import sleep
import csv


def student_images():
    cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier("FaceRecognitionRpi/haarcascade_frontalface_default.xml")

    Id = input("Enter your FaceId --> ")
    name = input("Enter the Student Name --> ")
    sampleNum = 0
    print("Collecting Your Face Images Please be Patient and Look into Camera")
    while True:
        ret, img = cam.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray,
                                               scaleFactor=1.3, minNeighbors=5)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            sampleNum = sampleNum + 1
            # print(sampleNum)
            cv2.imwrite("FaceRecognitionRpi/dataset/User." + Id +
                        '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
            cv2.imshow("Your Image", img)
            sleep(0.3)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        elif sampleNum >= 30:
            break

    cam.release()
    cv2.destroyAllWindows()
    data = "Saved Images of Id-->  " + Id + " Name--> " + name
    print(data)
    row = [Id, name]
    with open("FaceRecognitionRpi/ClientDetails.csv", 'a+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
