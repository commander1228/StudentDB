import sqlite3

database = sqlite3.connect("studentdatabase.db")
cur = database.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students(name,GPA)")

print("welcome to StudentDB")

def mainMenu():
    programState = 1
    while programState == 1: 
        print("1) add a student to the Database")
        print("2) view students in the Database")
        print("3) exit program")
        menuSelection = int(input("Please select an option: "))
        match menuSelection:
            case 1:
                addStudentMenu()
            case 2:
                displayStudents()
            case 3:
                print("quiting program")
                programState = 0  
                
def addStudentMenu():
    addedStudentName = input("please input student name:")
    addedStudentGpa = input("please input student gpa:")
    cur.execute("insert into students (name, GPA) values (?, ?)",
            (addedStudentName,addedStudentGpa))
    database.commit()
    print("student ",addedStudentName ,"has been added")

def displayStudents():
    print("Current students in DB:")
    for row in cur.execute("SELECT name,GPA FROM students ORDER BY name"):
        print (row)


mainMenu()