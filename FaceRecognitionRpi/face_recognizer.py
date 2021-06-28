import cv2
import numpy as np
import os
import csv
import datetime
import time, psycopg2
from random import uniform
import pandas as pd
#from smbus2 import SMBus
#from mlx90614 import MLX90614
#bus = SMBus(1)
#sensor = MLX90614(bus, address=0x5A)

col_names = ['Id', 'student_name', 'date', 'time', 'student_bodyTemperature']
names = ["None", 'Jayateerth', 'Shreeraj', 'Tejas', 'Rupesh']
attendance = pd.DataFrame(columns=col_names)

#df = pd.read_csv('StudentDetails.csv')

con = psycopg2.connect(database="FaceRecognition", user="postgres", password="dragonforcE#1", host="127.0.0.1", port="5432")


def recog_func():
    global attendance
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("FaceRecognitionRpi/trainer/trainer.yml")
    casc_path = "FaceRecognitionRpi/haarcascade_frontalface_default.xml"

    face_cascade = cv2.CascadeClassifier(casc_path)
    font = cv2.FONT_HERSHEY_SIMPLEX
    Id = 0
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)

    min_width = 0.1 * cam.get(3)
    min_height = 0.1 * cam.get(4)
    while True:
        ret, img = cam.read()
        # img = cv2.flip(img, -1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.3,
            minNeighbors=5,
            minSize=(int(min_width), int(min_height))
        )
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            time.sleep(0.2)

            if confidence >= 25:
                name_ed = names[Id]
                confidence = " {0}%".format(round(100 - confidence))

                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(
                    ts).strftime('%H-%M-%S')
                #temp = sensor.get_object_1()
                # bus.close()
                temp = round(uniform(36.7, 39.9), 2)

                attendance.loc[len(attendance)] = [
                    Id, name_ed, date, timeStamp, temp]
                # name_ed = str(name_ed)
                print(name_ed)

                print("Attendance Recorded for->  ", name_ed)

            else:
                Id = "unknown"
                confidence = " {0}%".format(round(100 - confidence))
            cv2.putText(img, str(names[Id]), (x + 5,
                                              y - 5), font, 0.5, (155, 120, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5),
                        font, 0.5, (255, 120, 100), 1)

        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('Camera', img)
        if cv2.waitKey(1) & 0xFf == ord('q'):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H-%M-%S')
    Hour, Minute, Second = timeStamp.split("-")
    fileName = "FaceRecognitionRpi/Attendance"+os.sep+"Attendance_" + date + ".csv"
    insert_to_db(id=Id, name=name_ed, body_temp=temp, date=date, time=timeStamp)
    attendance.to_csv(fileName, index=False)

    print("Cleaning up Everything")
    cam.release()
    cv2.destroyAllWindows()


def insert_to_db(id, name,date, time, body_temp):
    cur = con.cursor()
    # time = "'" + time +"'"
    date = "'" + date +"'"
    sql_query = "INSERT INTO attendance_info (student_id, student_name, body_temp, date, time)\n" \
                "VALUES ({}, {}, {}, {}, {})".format(id, "'"+ name + "'", body_temp, date, "'" + time +"'")
    print(sql_query)
    cur.execute(sql_query)
    con.commit()
    print('Added to DB')
    con.close()



