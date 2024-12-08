import Student
import Teacher
import Studentattendance
import Teacherattendance
import PayFees
import PaySalary

def student():
    while True:
        print("=="*20)
        print("Student Record Management")
        print("=="*20)
        print("1: Show Student Records", '\n', "2: Insert Student Record", '\n', "3: Delete Student Record", '\n', 
              "4: Update Student Record", '\n', "5: Return To Main Menu")
        print("=="*20)
        ch = int(input("Enter Your Choice [1-5]: "))
        print("=="*20)
        if ch == 1:
            Student.showstudentdata()
        elif ch == 2:
            Student.insertstudent()
        elif ch == 3:
            Student.deletestudent()
        elif ch == 4:
            Student.updatestudent()
        elif ch == 5:
            return
        else:
            print("=="*20)
            print("Invalid Choice")
            print("=="*20)

def teacher():
    while True:
        print("=="*20)
        print("Teacher Record Management")
        print("=="*20)
        print("1: Show Teacher Records", '\n', "2: Insert Teacher Record", '\n', "3: Delete Teacher Record", '\n', 
              "4: Update Teacher Record", '\n', "5: Return To Main Menu")
        print("=="*20)
        ch = int(input("Enter Your Choice [1-5]: "))
        print("=="*20)
        if ch == 1:
            Teacher.showteacherdata()
        elif ch == 2:
            Teacher.insertteacher()
        elif ch == 3:
            Teacher.deleteteacher()
        elif ch == 4:
            Teacher.updateteacher()
        elif ch == 5:
            return
        else:
            print("=="*20)
            print("Invalid Choice")
            print("=="*20)

def studentattendance():
    while True:
        print("=="*20)
        print("Student Attendance Record Management")
        print("=="*20)
        print("1: Show Student Attendance Records", '\n', "2: Insert Student Attendance Records", '\n', 
              "3: Delete Student Attendance Records", '\n', "4: Update Student Attendance Records", '\n', 
              "5: Return To Main Menu")
        print("=="*20)
        ch = int(input("Enter Your Choice [1-5]: "))
        print("=="*20)
        if ch == 1:
            Studentattendance.showattendancestudentdata()
        elif ch == 2:
            Studentattendance.insertattendancestudent()
        elif ch == 3:
            Studentattendance.deleteattendancestudent()
        elif ch == 4:
            Studentattendance.updateattendancestudent()
        elif ch == 5:
            return
        else:
            print("=="*20)
            print("Invalid Choice")
            print("=="*20)

def teacherattendance():
    while True:
        print("=="*20)
        print("Teacher Attendance Record Management")
        print("=="*20)
        print("1: Show Teacher Attendance Records", '\n', "2: Insert Teacher Attendance Records", '\n', 
              "3: Delete Teacher Attendance Records", '\n', "4: Update Teacher Attendance Records", '\n', 
              "5: Return To Main Menu")
        print("=="*20)
        ch = int(input("Enter Your Choice [1-5]: "))
        print("=="*20)
        if ch == 1:
            Teacherattendance.showattendanceteacherdata()
        elif ch == 2:
            Teacherattendance.insertattendanceteacher()
        elif ch == 3:
            Teacherattendance.deleteattendanceteacher()
        elif ch == 4:
            Teacherattendance.updateattendanceteacher()
        elif ch == 5:
            return
        else:
            print("=="*20)
            print("Invalid Choice")
            print("=="*20)

def payfees():
    while True:
        print("=="*20)
        print("Pay Fees Record Management")
        print("=="*20)
        print("1: Show Pay Fees Records", '\n', "2: Insert Pay Fees Records", '\n', "3: Delete Pay Fees Records", '\n', 
              "4: Update Pay Fees Records", '\n', "5: Return To Main Menu")
        print("=="*20)
        ch = int(input("Enter Your Choice [1-5]: "))
        print("=="*20)
        if ch == 1:
            PayFees.showpayfeesdata()
        elif ch == 2:
            PayFees.insertpayfees()
        elif ch == 3:
            PayFees.deletepayfees()
        elif ch == 4:
            PayFees.updatepayfees()
        elif ch == 5:
            return
        else:
            print("=="*20)
            print("Invalid Choice")
            print("=="*20)

def paysalary():
    while True:
        print("=="*20)
        print("Pay Salary Record Management")
        print("=="*20)
        print("1: Show Pay Salary Records", '\n', "2: Insert Pay Salary Records", '\n', 
              "3: Delete Pay Salary Records", '\n', "4: Update Pay Salary Records", '\n', 
              "5: Return To Main Menu")
        print("=="*20)
        ch = int(input("Enter Your Choice [1-5]: "))
        print("=="*20)
        if ch == 1:
            PaySalary.showpaysalarydata()
        elif ch == 2:
            PaySalary.insertpaysalary()
        elif ch == 3:
            PaySalary.deletepaysalary()
        elif ch == 4:
            PaySalary.updatepaysalary()
        elif ch == 5:
            return
        else:
            print("=="*20)
            print("Invalid Choice")
            print("=="*20)
