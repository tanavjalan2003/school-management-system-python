import Sm
import time

print("Executing Program")
time.sleep(3)

while True:
    print("=="*20)
    print("School Management")
    print("=="*20)
    print(" 1: Student Record", '\n', "2: Teacher Record", '\n', "3: Student Attendance Records", '\n', 
          "4: Teacher Attendance Records", '\n', "5: Pay Fees Records", '\n', "6: Pay Salary Records", '\n', "7: Exit")
    time.sleep(1)
    print("=="*20)
    ch = int(input("Enter your Choice [1-7]: "))
    print("=="*20)
    
    if ch == 1:
        Sm.student()
    elif ch == 2:
        Sm.teacher()
    elif ch == 3:
        Sm.studentattendance()
    elif ch == 4:
        Sm.teacherattendance()
    elif ch == 5:
        Sm.payfees()
    elif ch == 6:
        Sm.paysalary()
    elif ch == 7:
        break
    else:
        print("=="*20)
        print("Invalid Choice")
        print("=="*20)
