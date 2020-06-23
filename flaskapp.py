import json
import mysql.connector
import os
from flask import Flask, request, make_response


application = Flask(__name__)

dbhost = os.getenv('DBHOST')
dbuser = os.getenv('DBUSER') 
dbpassword = os.getenv('DBPASSWORD') 
dbname = os.getenv('DBNAME') 


mydb = mysql.connector.connect(
  host=dbhost,
  user=dbuser,
  passwd=dbpassword,
  database=dbname
)

result = type('', (), {})()


@application.route('/users')
def getUsers():
    sql = "select * from users"
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    result.data = myresult
    return json.loads(json.dumps(result.__dict__, default=str))

if __name__ == "__main__":
    application.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)

