# CMSC447_HW1_Yingling
 Homework 1 for Software Engineering: CRUD Application

## Initial Set-up:

This application was tested in a python virtual environment. Make sure to use in a virtual environment to replicate similar behavior

- Once files are downloaded and virtual environment is activated, execute `pip install -r requirements.txt` to install necessary packages
- Traverse to `/CMSC447_HW1_Yingling` in your file system
- Type `python data_manage.py` to run and get the webpage started
- Type `localhost:5000` in your browser to see the webpage

## How to Use the Application:

### General Notes:

- Names are in alphabetical characters and a space is used to separate the first and last name of a student
- IDs are represented by numbers
- Scores are also represented by numbers

### Home Page:

There are multiple links on the home page that will allow you to create, read, update, and delete student information from the database. Each link will have a corresponding `home` link that will return you to the home page.

### Create:

After entering a name (first and last separated by a space), an ID number, and a score into the text boxes, a new student will be added to the database upon hitting the `Register` button.

### Read:

There are two types of reads. One will display all of the students who are currently in the database, and one will display all of the students with a specific score. The score will have to be input into the textbox and the list will return upon hitting the `Search` button.

### Update:

After entering the name of the student to be updated, their ID, and the new score to be given, the student will have an updated score in the database upon hitting the `Update` button.

### Delete:

After entering the name of the student to be deleted and their ID, the student will be removed from the database upon hitting the `Delete` button.
