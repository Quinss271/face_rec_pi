from flask import Flask, url_for
from flask import request
from flask import render_template
import mysql.connector
import shutil
import os


app = Flask(__name__)
@app.route('/add', methods=['POST', 'GET'])

def login():
    
    error = None
    mydb = mysql.connector.connect(
              host="localhost",
              user="pi",
              passwd="root",
              database="pi"
    )
    if request.method == "POST":
        mycursor = mydb.cursor()
        sql = "SELECT MAX(id) FROM `verify_pi`"
        res = mycursor.execute(sql)
        res = mycursor.fetchone()
        n_id = res[0]+1
               
        fio = request.form['fio']
        image = request.form["image"]
        #shutil.move("/home/pi/Templates/Face_recognition/dataset/"+image, "/home/pi/Templates/face_rec2/photos/3.jpg")
        print(os.path.abspath(image))
        #sql = 'INSERT INTO `verify_pi`(`id`, `fio`) VALUES ('+str(n_id)+',"'+str(fio)+'")'
        mycursor.execute(sql)
        mydb.commit()
    
    return render_template('add.html', error=error)
