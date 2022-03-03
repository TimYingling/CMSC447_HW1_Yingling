import sqlite3
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

conn = sqlite3.connect('hw1data.db', check_same_thread=False)

c = conn.cursor()

#c.execute("""CREATE TABLE student (
#			name text,
#			id integer,
#			score integer
#			)""")

class Student:
	"""Class to hold student information for displaying"""
	def __init__(self, name, id, score):
		self.name = name
		self.id = id
		self.score = score

#Functions that handle information from the user
@app.route('/', methods = ["GET"])
def home_screen():
	return render_template("home.html")

@app.route('/create', methods =["GET", "POST"])
def add_new_students():
	if request.method == "POST":
		name = request.form.get("s_name")
		id = request.form.get("id")
		score = request.form.get("score")
		create_student(name, id, score)
	return render_template("create.html")

@app.route('/readall', methods=["GET"])
def display_all():
	students = list_all_students()
	return render_template("display.html", students=students)

@app.route('/search', methods=["GET", "POST"])
def display_scores():
	if request.method == "POST":
		score = request.form.get("score")
		students = list_all_score(score)
		return render_template("display.html", students=students)
	return render_template("ask_score.html")

@app.route('/update', methods=["GET", "POST"])
def update_students():
	if request.method == "POST":
		name = request.form.get("s_name")
		id = request.form.get("id")
		new_score = request.form.get("new_score")
		update_score(name, id, new_score)
	return render_template("update.html")

@app.route('/delete', methods=["GET", "POST"])
def delete_students():
	if request.method == "POST":
		name = request.form.get("s_name")
		id = request.form.get("id")
		remove_student(name, id)
	return render_template("delete.html")


#Functions for interacting with the database
def create_student(name, id, score):
	with conn:
		c.execute("INSERT INTO student VALUES (:name, :id, :score)", {'name':name, 'id':id, 'score':score})

def list_all_students():
	c.execute("SELECT * FROM student")
	#make an array to hold student objects
	student_list = []
	for x in c.fetchall():
		name, id, score = x
		#Create a student object using data extracted from tuple
		a_student = Student(name, id, score)
		#add student to the list
		student_list.append(a_student)
	return student_list
		

def list_all_score(score):
	c.execute("SELECT * FROM student WHERE score=:score", {'score':score})
	#make an array to hold student objects
	student_list = []
	for x in c.fetchall():
		name, id, score = x
		#Create a student object using data extracted from tuple
		a_student = Student(name, id, score)
		#add student to the list
		student_list.append(a_student)
	return student_list

def update_score(name, id, new_score):
	with conn:
		c.execute("""UPDATE student SET score=:score
					WHERE name=:name AND id=:id""",
					{'score':new_score, 'name':name, 'id':id})

def remove_student(name, id):
	with conn:
		c.execute("DELETE from student WHERE name=:name AND id=id",
					{'name':name, 'id':id})

#manually add all of the sample data from the hw
#create_student('Steve Smith', '211', '80')
#create_student('Jian Wong', '122', '92')
#create_student('Chris Peterson', '213', '91')
#create_student('Sai Patel', '524', '94')
#create_student('Andrew Whitehead', '425', '99')
#create_student('Lynn Roberts', '626', '90')
#create_student('Robert Sanders', '287', '75')

if __name__ == '__main__':
	app.run()