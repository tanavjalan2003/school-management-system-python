import mysql.connector as m

# Establishing connection to the database
con = m.connect(host="localhost", user="root", passwd="password", database="csproject")
cur = con.cursor()

def insertstudent():
    try:
        RollNo = int(input("Enter the Roll No: "))
        StudentName = input("Enter the Student Name: ")
        Class = input("Enter the Class and Section: ")
        Address = input("Enter the Address: ")
        PhoneNo = int(input("Enter the Phone No: "))
        data = (RollNo, StudentName, Class, Address, PhoneNo)
        sql = "INSERT INTO Student VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, data)
        con.commit()
        print("*" * 20)
        print("Data Entered")
        print("*" * 20)
    except Exception as e:
        print(e)

def deletestudent():
    try:
        RollNo = int(input("Enter the Roll No to Delete: "))
        d = (RollNo,)
        cur.execute("SELECT * FROM Student WHERE RollNo=%s", d)
        r = cur.fetchone()
        if r is None:
            print("Record not found")
        else:
            cur.execute("DELETE FROM Student WHERE RollNo=%s", d)
            con.commit()
            print("*" * 20)
            print("Data Removed")
            print("*" * 20)
    except Exception as e:
        print(e)

def updatestudent():
    try:
        RollNo = int(input("Enter the Roll No to Update: "))
        d = (RollNo,)
        cur.execute("SELECT * FROM Student WHERE RollNo=%s", d)
        r = cur.fetchone()
        if r is None:
            print("Record not found")
        else:
            StudentName = input("Enter the New Student Name: ")
            Class = input("Enter the New Class and Section: ")
            Address = input("Enter the New Address: ")
            PhoneNo = int(input("Enter the New Phone No: "))
            data = (StudentName, Class, Address, PhoneNo, RollNo)
            cur.execute(
                "UPDATE Student SET StudentName=%s, Class=%s, Address=%s, PhoneNo=%s WHERE RollNo=%s", 
                data
            )
            con.commit()
            print("*" * 20)
            print("Data Updated")
            print("*" * 20)
    except Exception as e:
        print(e)

def showstudentdata():
    try:
        print("1: Show All Records")
        print("2: Show Single Record")
        choice = int(input("Your Choice (1/2): "))
        if choice == 1:
            cur.execute("SELECT * FROM Student")
            results = cur.fetchall()
            if not results:
                print("No Records Found")
            for row in results:
                print(f"RollNo={row[0]}, StudentName={row[1]}, Class={row[2]}, Address={row[3]}, PhoneNo={row[4]}")
        elif choice == 2:
            RollNo = int(input("Enter the Roll No: "))
            cur.execute("SELECT * FROM Student WHERE RollNo=%s", (RollNo,))
            r = cur.fetchone()
            if r is None:
                print("Record not found")
            else:
                print(f"RollNo={r[0]}, StudentName={r[1]}, Class={r[2]}, Address={r[3]}, PhoneNo={r[4]}")
        else:
            print("Invalid Choice")
    except Exception as e:
        print(e)
