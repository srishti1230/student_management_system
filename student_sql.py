
import sqlite3   ##sqlite library ##database

connection=sqlite3.connect("student.db") ##file name
print("Database opened successfully")


TABLE_NAME="student_table"
NAME="student_name"
BRANCH="student_branch"
CLASS="student_class"
ROLL="student_roll"
GRADE="student_grade"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + NAME + " TEXT, " +
                   BRANCH + " TEXT, " + CLASS + " TEXT, " + ROLL + " INTEGER PRIMARY KEY, " + GRADE + " FLOAT);")
print("table created successfully")

###insert new record
def insert_data(name_entry, branch_entry, class_entry, roll_entry, grade_entry):
        connection.execute("INSERT INTO " + TABLE_NAME + " ( " + NAME + ", " + BRANCH + ", " +
                          CLASS + ", " + ROLL + ", " + GRADE + " ) VALUES ( '"+name_entry+"','"+branch_entry+"','"+class_entry+"',"+roll_entry+","+grade_entry+" ); ")
        connection.commit()

def fetch_data(roll_entry):
        cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " WHERE " + ROLL + " = " + str(roll_entry) + " ;")
        for row in cursor:
                return row

def update_data(name_entry, branch_entry, class_entry, roll_entry, grade_entry):
        connection.execute("UPDATE " + TABLE_NAME + " SET " + NAME + " = '" + name_entry + "', " +
                           BRANCH + " = '" + branch_entry + "', " + CLASS + " = '" + class_entry + "', " +
                           GRADE + " = " + grade_entry + " WHERE " + ROLL + " = " + roll_entry + " ;")
        connection.commit()

def delete_data(roll_entry):
        connection.execute("DELETE FROM " + TABLE_NAME + " WHERE " + ROLL + " = " + roll_entry + " ;")
        connection.commit()

def search_data(roll_entry):
        cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " WHERE " + ROLL + " = " + str(roll_entry) + " ;")
        for row in cursor:
                return row
        connection.commit()

def view_data():
        cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
        return cursor
        connection.commit()


