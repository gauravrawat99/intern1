import time
import os
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    database="process",
    user="root",
    password="rawat123"
)
cursor = connection.cursor()

processing = 'processing'
queue = 'queue'
processed = 'processed'


for i in range (1,11):
    file = str(i)
    name = file + ".txt"
    with open(os.path.join(processing,name),'w') as f:
        pass
    query = "INSERT INTO file (fname, status) VALUES (%s, %s)"
    up = (name,"0")
    cursor.execute(query, up)
    connection.commit()    
    time.sleep(1)
    if i % 5 == 0:
            allfiles = os.listdir(processing)
            for k in allfiles:
                os.rename(processing +'/'+ k, queue+'/'+ k)
            all_file = os.listdir(queue)
            for j in all_file:
                os.rename( queue +'/'+ j, processed +'/'+ j)
                for z in all_file:
                    query1 = "UPDATE file SET status = %s WHERE fname = %s"
                    update = ("1",z)
                    cursor.execute(query1,update)
                    connection.commit()

