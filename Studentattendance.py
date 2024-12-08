import mysql.connector as m

# Establishing connection to the database
con = m.connect(host="localhost", user="root", passwd="password", database="csproject")
cur = con.cursor()

def insertattendancestudent():
    try:
        RollNo = int(input("Enter the Roll No: "))
        PresentOrAbsent = input("Enter if Present or Absent: ")
        data = (RollNo, PresentOrAbsent)
        sql = "INSERT INTO StudentAttendance (RollNo, Date, PresentOrAbsent) VALUES (%s, CURDATE(), %s)"
        cur.execute(sql, data)
        con.commit()
        print("*" * 20)
        print("Data Entered")
        print("*" * 20)
    except Exception as e:
        print(e)

def deleteattendancestudent():
    try:
        RollNo = int(input("Enter the Roll No to Delete Attendance: "))
        d = (RollNo,)
        cur.execute("SELECT * FROM StudentAttendance WHERE RollNo=%s", d)
        r = cur.fetchone()
        if r is None:
            print("Record not found")
        else:
            cur.execute("DELETE FROM StudentAttendance WHERE RollNo=%s", d)
            con.commit()
            print("*" * 20)
            print("Data Removed")
            print("*" * 20)
    except Exception as e:
        print(e)

def updateattendancestudent():
    try:
        RollNo = int(input("Enter the Roll No to Update Attendance: "))
        d = (RollNo,)
        cur.execute("SELECT * FROM StudentAttendance WHERE RollNo=%s", d)
        r = cur.fetchone()
        if r is None:
            print("Record not found")
        else:
            PresentOrAbsent = input("Enter if Present or Absent: ")
            data = (PresentOrAbsent, RollNo)
            cur.execute(
                "UPDATE StudentAttendance SET Date=CURDATE(), PresentOrAbsent=%s WHERE RollNo=%s", 
                data
            )
            con.commit()
            print("*" * 20)
            print("Data Updated")
            print("*" * 20)
    except Exception as e:
        print(e)

def showattendancestudentdata():
    try:
        print("1: Show All Records")
        print("2: Show Single Record")
        choice = int(input("Your Choice (1/2): "))
        if choice == 1:
            cur.execute("SELECT * FROM StudentAttendance")
            results = cur.fetchall()
            if not results:
                print("No Records Found")
            for row in results:
                print(f"RollNo={row[0]}, Date={row[1]}, PresentOrAbsent={row[2]}")
        elif choice == 2:
            RollNo = int(input("Enter the Roll No: "))
            cur.execute("SELECT * FROM StudentAttendance WHERE RollNo=%s", (RollNo,))
            r = cur.fetchone()
            if r is None:
                print("Record not found")
            else:
                print(f"RollNo={r[0]}, Date={r[1]}, PresentOrAbsent={r[2]}")
        else:
            print("Invalid Choice")
    except Exception as e:
        print(e)
