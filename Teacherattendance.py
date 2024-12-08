import mysql.connector as m

# Establishing connection to the database
con = m.connect(host="localhost", user="root", passwd="password", database="csproject")
cur = con.cursor()

def insertattendanceteacher():
    try:
        AccountNo = int(input("Enter the Account No: "))
        PresentOrAbsent = input("Enter if Present or Absent: ")
        data = (AccountNo, PresentOrAbsent)
        sql = "INSERT INTO TeacherAttendance (AccountNo, Date, PresentOrAbsent) VALUES (%s, CURDATE(), %s)"
        cur.execute(sql, data)
        con.commit()
        print("*" * 20)
        print("Data Entered")
        print("*" * 20)
    except Exception as e:
        print(e)

def deleteattendanceteacher():
    try:
        AccountNo = int(input("Enter the Account No to Delete Attendance: "))
        d = (AccountNo,)
        cur.execute("SELECT * FROM TeacherAttendance WHERE AccountNo=%s", d)
        r = cur.fetchone()
        if r is None:
            print("Record not found")
        else:
            cur.execute("DELETE FROM TeacherAttendance WHERE AccountNo=%s", d)
            con.commit()
            print("*" * 20)
            print("Data Removed")
            print("*" * 20)
    except Exception as e:
        print(e)

def updateattendanceteacher():
    try:
        AccountNo = int(input("Enter the Account No to Update Attendance: "))
        d = (AccountNo,)
        cur.execute("SELECT * FROM TeacherAttendance WHERE AccountNo=%s", d)
        r = cur.fetchone()
        if r is None:
            print("Record not found")
        else:
            PresentOrAbsent = input("Enter if Present or Absent: ")
            data = (PresentOrAbsent, AccountNo)
            cur.execute(
                "UPDATE TeacherAttendance SET Date=CURDATE(), PresentOrAbsent=%s WHERE AccountNo=%s", 
                data
            )
            con.commit()
            print("*" * 20)
            print("Data Updated")
            print("*" * 20)
    except Exception as e:
        print(e)

def showattendanceteacherdata():
    try:
        print("1: Show All Records")
        print("2: Show Single Record")
        choice = int(input("Your Choice (1/2): "))
        if choice == 1:
            cur.execute("SELECT * FROM TeacherAttendance")
            results = cur.fetchall()
            if not results:
                print("No Records Found")
            for row in results:
                print(f"AccountNo={row[0]}, Date={row[1]}, PresentOrAbsent={row[2]}")
        elif choice == 2:
            AccountNo = int(input("Enter the Account No: "))
            cur.execute("SELECT * FROM TeacherAttendance WHERE AccountNo=%s", (AccountNo,))
            r = cur.fetchone()
            if r is None:
                print("Record not found")
            else:
                print(f"AccountNo={r[0]}, Date={r[1]}, PresentOrAbsent={r[2]}")
        else:
            print("Invalid Choice")
    except Exception as e:
        print(e)
