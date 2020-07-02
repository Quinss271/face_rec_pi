from flask import Flask
from flask import request
from flask import render_template

import mysql.connector


app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])

def login():
    
    error = None
    mydb = mysql.connector.connect(
              host="localhost",
              user="pi",
              passwd="root",
              database="pi"
    )

    mycursor = mydb.cursor()
    sql = "SELECT MAX(id) FROM `pi_recognaze`"
    res= mycursor.execute(sql)
    res=mycursor.fetchone()
    if (request.method == "POST"):
        print(res[0]+1)
        from recog import cam
        cam()
    
    return render_template('login.html', error=error)