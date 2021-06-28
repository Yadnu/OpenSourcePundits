import json, sys
from psycopg2 import connect, Error
import os

## Database Variables
db_username = 'postgres'
db_name = 'FaceRecognition'
db_pass = 'dragonforcE#1'
db_host = '127.0.0.1'
db_port = '5432'


file_path = 'N:/PycharmProjects/FaceRecognition/FaceRecognitionRpi/JsonFiles'
os.chdir(file_path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
# print(newest)


## Opening the file
with open(newest) as json_data:
    record_list = json.load(json_data)
    # print(type(record_list))
    if type(record_list) == list:
        first_record = record_list[0]
        # print(first_record)
        col_names = list(first_record.keys())
        # print(col_names)
        # print('Columns- ', col_names) Columns-  ['Id', 'Name', 'Date', 'Time', 'BodyTemperature']
    values = [list(x.values()) for x in record_list]
    print('values: ', values)
    values_str = ""
    for i, record in enumerate(values):
        val_list = []

        for v, val in enumerate(record):
            # print('val: ', val)
            val_list += [str(val)]

        values_str += "(" + ','.join(val_list) + "),\n"

    values_str = values_str[:-2] + ';'
    print(values_str)

    table_name = 'attendance_info'
    sql_query = "INSERT INTO {0} ({1})\nVALUES {2}".format(table_name,
                                                    ', '.join(col_names),
                                                    values_str)
    print('sql_query:-', sql_query)






try:
    conn = connect(
        dbname = db_name, host=db_host,
        user = db_username, password=db_pass,
        port = db_port
    )
    cur = conn.cursor()
    print('Cursor Created')


    cur.execute(sql_query)
    conn.commit()
    print('Added to Database')

except (Exception, Error) as err:
    print("Cant't connect to DB due to:-> ", err)
