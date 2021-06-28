import psycopg2
import pandas as pd
import datetime
import os
import json

## Database Variables
db_username = 'postgres'
db_name = 'FaceRecognition'
db_pass = 'dragonforcE#1'
db_host = '127.0.0.1'
db_port = '5432'


path = 'Attendance'
os.chdir(path)

# Todays Date and Newest file from Folder
today = datetime.datetime.today().strftime('%d-%m-%Y')
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
print(newest[11:-4])

df=pd.read_csv(newest)
df.to_json('N:/PycharmProjects/FaceRecognition/FaceRecognitionRpi/JsonFiles/{0}.{1}'.format(newest[:-4], 'json'),
            orient='records', indent=4)


df.to_json('N:/PycharmProjects/FaceRecognitionWebModule/JsonFiles/{0}.{1}'.format(newest[:-4], 'json'),
            orient='records', indent=4)




































# ['id', 'date', 'time', 'student_name', 'student_id', 'student_bodyTemperature', 'attend_status']

# print(df.head())
