from flask import Flask, request, render_template, redirect, url_for, session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import csv
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per minute", "1 per second"])

@app.route('/')
def home():
    return 'Bienvenue !'

@app.route('/gaz', methods=['GET','POST'])
def save_gazouille():
	if request.method == 'POST':
		print(request.form)
		dump_to_csv(request.form)
		return redirect(url_for('timeline'))
		#return "OK"
	if request.method == 'GET':
		return render_template('formulaire.html')

@app.route('/timeline', methods=['GET'])
def timeline():
	gaz = parse_from_csv()
	return render_template("timeline.html", gaz = gaz)

def parse_from_csv():
	gaz = []
	with open('./gazouilles.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			gaz.append({"user":row[0], "text":row[1]})
	return gaz

def dump_to_csv(d):
	donnees = [d["user-name"],d["user-text"] ]
	with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(donnees)


#Add Login Code
app.secret_key = 'secret_key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'SalmaZR.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'SalmaZR'
app.config['MYSQL_PASSWORD'] = 'Zr@ibi@1994'
app.config['MYSQL_DB'] = 'SalmaZR$flask_project'

# Intialize MySQL
mysql = MySQL(app)


# http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('index.html', msg='')


