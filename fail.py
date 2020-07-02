import mysql.connector
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(st_ID, Name, Photo):
    #print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='pi',
                                             user='pi',
                                             password='root')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO verify_in
                          (ID, Name, Photo) VALUES (%s,%s,%s)"""

        empPicture = convertToBinaryData(Photo)
        # Convert data into tuple format
        insert_blob_tuple = (st_ID, Name, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#print(convertToBinaryData("./img/bill.jpg"))
insertBLOB(1, "Obama", "./photos/0.jpg")