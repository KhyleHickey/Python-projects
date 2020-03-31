#to be tested


import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# assumes database is not password protected
# and the database username is the default, 'test'
testdb = 'mysql+pymysql://test:@'
basedir  = '127.0.0.1'
# insert database name
dbname   = '/sockmarket'
# creates a linux specific socket 
socket   = '?unix_socket=/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
dbname   = dbname + socket

# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = testdb + basedir + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# this route will test the database connection only
@app.route('/')
def testdb():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return '<h1>It works.</h1>'
    except:
        return '<h1>Something is broken.</h1>'

if __name__ == '__main__':
    app.run(debug=True)
