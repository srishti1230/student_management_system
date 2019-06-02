import tkinter as tk
from tkinter import ttk
import student_sql as sq

mainWindow=tk.Tk()
mainWindow.title('student management')

label_1=tk.Label(mainWindow,text="DIT UNIVERSITY STUDENT MANAGEMENT PORTAL",font=("Arial Bold",15))
label_1.pack()


button_1=tk.Button(mainWindow,text="ADD_STUDENT",command=lambda:add(),padx=(20),pady=(5),width=(20))
button_1.pack()

button_2=tk.Button(mainWindow,text="UPDATE_STUDENT",command=lambda:update(),padx=(20),pady=(5),width=(20))
button_2.pack()

button_3=tk.Button(mainWindow,text="VIEW_STUDENT",command=lambda:view(),padx=(20),pady=(5),width=(20))
button_3.pack()

button_4=tk.Button(mainWindow,text="DELETE_STUDENT",command=lambda:delete(),padx=(20),pady=(5),width=(20))
button_4.pack()

button_5=tk.Button(mainWindow,text="SEARCH_STUDENT",command=lambda:search(),padx=(20),pady=(5),width=(20))
button_5.pack()


def add():
    addWindow = tk.Tk()
    addWindow.title("ADD STUDENT DETAIL")

    name_label=tk.Label(addWindow,text="ENTER NAME:",)
    name_label.pack()
    name_entry=tk.Entry(addWindow)
    name_entry.pack()
    branch_label = tk.Label(addWindow, text="ENTER BRANCH:")
    branch_label.pack()
    branch_entry = tk.Entry(addWindow)
    branch_entry.pack()
    class_label = tk.Label(addWindow, text="ENTER CLASS:")
    class_label.pack()
    class_entry = tk.Entry(addWindow)
    class_entry.pack()
    roll_label = tk.Label(addWindow, text="ENTER ROLL:")
    roll_label.pack()
    roll_entry = tk.Entry(addWindow)
    roll_entry.pack()
    grade_label = tk.Label(addWindow, text="ENTER CGPA:")
    grade_label.pack()
    grade_entry = tk.Entry(addWindow)
    grade_entry.pack()
    button = tk.Button(addWindow, text="ADD RECORD", command=lambda: sq.insert_data(name_entry.get(), branch_entry.get(), class_entry.get(), roll_entry.get(), str(grade_entry.get())))
    button.pack()
    addWindow.mainloop()



def update():
    updateWindow = tk.Tk()
    updateWindow.title("UPDATE STUDENT DETAIL")
    roll_label = tk.Label(updateWindow, text="ENTER Roll No:", )
    roll_label.pack()
    roll_entry = tk.Entry(updateWindow)
    roll_entry.pack()
    button = tk.Button(updateWindow, text="SHOW RECORD",command=lambda: show_details(str(roll_entry.get())))
    button.pack()
    updateWindow.mainloop()


def view():
    viewWindow = tk.Tk()
    viewWindow.title("Display results")

    appLabel = tk.Label(viewWindow, text="Student Management System", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(viewWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="BRANCH")
    tree.heading("two", text="CLASS")
    tree.heading("three", text="ROLL NUMBER")
    tree.heading("four", text="GRADE")

    cursor = sq.view_data()
    i = 0

    for row in cursor:
        tree.insert('', i, text=str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()
    viewWindow.mainloop()


def delete():
    deleteWindow = tk.Tk()
    deleteWindow.title("DELETE STUDENT DETAIL")
    roll_label = tk.Label(deleteWindow, text="ENTER Roll No:", )
    roll_label.pack()
    roll_entry = tk.Entry(deleteWindow)
    roll_entry.pack()
    button = tk.Button(deleteWindow, text="DELETE RECORD", command=lambda: sq.delete_data(str(roll_entry.get())))
    button.pack()
    deleteWindow.mainloop()


def search():
    searchWindow = tk.Tk()
    searchWindow.title("SEARCH STUDENT DETAIL")
    roll_label = tk.Label(searchWindow, text="ENTER Roll No:", )
    roll_label.pack()
    roll_entry = tk.Entry(searchWindow)
    roll_entry.pack()
    button = tk.Button(searchWindow, text="SEARCH RECORD", command=lambda: show_search(str(roll_entry.get())))
    button.pack()
    searchWindow.mainloop()

def show_details(roll_entry):
    cursor = sq.fetch_data(roll_entry)
    addWindow = tk.Tk()
    addWindow.title("STUDENT DETAIL")
    name_label = tk.Label(addWindow, text="NAME:", )
    name_label.pack()
    name_entry = tk.Entry(addWindow)
    name_entry.insert(0, cursor[0])
    name_entry.pack()
    branch_label = tk.Label(addWindow, text="BRANCH:")
    branch_label.pack()
    branch_entry = tk.Entry(addWindow, text= cursor[1])
    branch_entry.insert(0, cursor[1])
    branch_entry.pack()
    class_label = tk.Label(addWindow, text="CLASS:")
    class_label.pack()
    class_entry = tk.Entry(addWindow, text= cursor[2])
    class_entry.insert(0, cursor[2])
    class_entry.pack()
    roll_label = tk.Label(addWindow, text="ROLL:")
    roll_label.pack()
    roll_entry = tk.Entry(addWindow, text= cursor[3])
    roll_entry.insert(0, cursor[3])
    roll_entry.pack()
    grade_label = tk.Label(addWindow, text="CGPA:")
    grade_label.pack()
    grade_entry = tk.Entry(addWindow, text= cursor[4])
    grade_entry.insert(0, cursor[4])
    grade_entry.pack()
    button = tk.Button(addWindow, text="UPDATE RECORD",command=lambda: sq.update_data(name_entry.get(),
                        branch_entry.get(), class_entry.get(), str(roll_entry.get()), str(grade_entry.get())))
    button.pack()
    addWindow.mainloop()

def show_search(roll_entry):
    cursor = sq.fetch_data(roll_entry)
    addWindow = tk.Tk()
    addWindow.title("STUDENT DETAIL")
    name_label = tk.Label(addWindow, text="NAME:")
    name_label.pack()
    namelabel = tk.Label(addWindow, text=cursor[0])
    namelabel.pack()
    branch_label = tk.Label(addWindow, text="BRANCH:")
    branch_label.pack()
    branchlabel = tk.Label(addWindow, text=cursor[1])
    branchlabel.pack()
    class_label = tk.Label(addWindow, text="CLASS:")
    class_label.pack()
    classlabel = tk.Label(addWindow, text=cursor[2])
    classlabel.pack()
    roll_label = tk.Label(addWindow, text="ROLL:")
    roll_label.pack()
    rolllabel = tk.Label(addWindow, text=cursor[3])
    rolllabel.pack()
    grade_label = tk.Label(addWindow, text="CGPA:")
    grade_label.pack()
    gradelabel = tk.Label(addWindow, text=cursor[4])
    gradelabel.pack()
    addWindow.mainloop()

mainWindow.mainloop()