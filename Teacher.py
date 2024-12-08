import mysql.connector as m

# Establishing connection to the database
con = m.connect(host="localhost", user="root", passwd="password", database="csproject")
cur = con.cursor()

def insertteacher():
    try:
        AccountNo = int(input("Enter the Account No: "))
        TeacherName = input("Enter the Teacher Name: ")
        Post = input("Enter the Post: ")
        Salary = int(input("Enter the Salary: "))
        Address = input("Enter the Address: ")
        PhoneNo = int(input("Enter the Phone No: "))
        data = (AccountNo, TeacherName, Post, Salary, Address, PhoneNo)
        sql = "INSERT INTO Teacher VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(sql, data)
        con.commit()
        print("*" * 20)
        print("Data Entered")
        print("*" * 20)
    except Exception as e:
        print(e)

def deleteteacher():
    try:
        AccountNo = int(input("Enter the Account No to Delete: "))
        d = (AccountNo,)
        cur.execute("SELECT * FROM Teacher WHERE AccountNo=%s", d)
        r = cur.fetchone()
        if r is None:
            print("Record not found")
        else:
            cur.execute("DELETE FROM Teacher WHERE AccountNo=%s", d)
            con.commit()
            print("*" * 20)
            print("Data Removed")
            print("*" * 20)
    except Exception as e:
        print(e)

def updateteacher():
    try:
        AccountNo = int(input("Enter the Account No to Update: "))
        d = (AccountNo,)
        cur.execute("SELECT * FROM Teacher WHERE AccountNo=%s", d)
        r = cur.fetchone()
        if r is None:
            print("Record not found")
        else:
            TeacherName = input("Enter the New Teacher Name: ")
            Post = input("Enter the New Post: ")
            Salary = int(input("Enter the New Salary: "))
            Address = input("Enter the New Address: ")
            PhoneNo = int(input("Enter the New Phone No: "))
            data = (TeacherName, Post, Salary, Address, PhoneNo, AccountNo)
            cur.execute(
                "UPDATE Teacher SET TeacherName=%s, Post=%s, Salary=%s, Address=%s, PhoneNo=%s WHERE AccountNo=%s", 
                data
            )
            con.commit()
            print("*" * 20)
            print("Data Updated")
            print("*" * 20)
    except Exception as e:
        print(e)

def showteacherdata():
    try:
        print("1: Show All Records")
        print("2: Show Single Record")
        choice = int(input("Your Choice (1/2): "))
        if choice == 1:
            cur.execute("SELECT * FROM Teacher")
            results = cur.fetchall()
            if not results:
                print("No Records Found")
            for row in results:
                print(f"AccountNo={row[0]}, TeacherName={row[1]}, Post={row[2]}, Salary={row[3]}, Address={row[4]}, PhoneNo={row[5]}")
        elif choice == 2:
            AccountNo = int(input("Enter the Account No: "))
            cur.execute("SELECT * FROM Teacher WHERE AccountNo=%s", (AccountNo,))
            r = cur.fetchone()
            if r is None:
                print("Record not found")
            else:
                print(f"AccountNo={r[0]}, TeacherName={r[1]}, Post={r[2]}, Salary={r[3]}, Address={r[4]}, PhoneNo={r[5]}")
        else:
            print("Invalid Choice")
    except Exception as e:
        print(e)
