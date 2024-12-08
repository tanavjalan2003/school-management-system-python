import mysql.connector as m

# Establishing connection to the database
con = m.connect(host="localhost", user="root", passwd="password", database="csproject")
cur = con.cursor()

def insertpaysalary():
    try:
        AccountNo = int(input("Enter the Account No: "))
        Month = input("Enter the Month: ")
        GivenOrNotGiven = input("Enter Salary Given or Not Given: ")
        data = (AccountNo, Month, GivenOrNotGiven)
        sql = "INSERT INTO PaySalary (AccountNo, Month, GivenOrNotGiven) VALUES (%s, %s, %s)"
        cur.execute(sql, data)
        con.commit()
        print("*" * 20)
        print("Data Entered")
        print("*" * 20)
    except Exception as e:
        print(e)

def deletepaysalary():
    try:
        AccountNo = int(input("Enter the Account No to Delete Salary Record: "))
        d = (AccountNo,)
        cur.execute("SELECT * FROM PaySalary WHERE AccountNo=%s", d)
        r = cur.fetchone()
        if r is None:
            print("Record not found")
        else:
            cur.execute("DELETE FROM PaySalary WHERE AccountNo=%s", d)
            con.commit()
            print("*" * 20)
            print("Data Removed")
            print("*" * 20)
    except Exception as e:
        print(e)

def updatepaysalary():
    try:
        AccountNo = int(input("Enter the Account No to Update Salary Record: "))
        d = (AccountNo,)
        cur.execute("SELECT * FROM PaySalary WHERE AccountNo=%s", d)
        r = cur.fetchone()
        if r is None:
            print("Record not found")
        else:
            Month = input("Enter the New Month: ")
            GivenOrNotGiven = input("Enter Salary Given or Not Given: ")
            data = (Month, GivenOrNotGiven, AccountNo)
            cur.execute(
                "UPDATE PaySalary SET Month=%s, GivenOrNotGiven=%s WHERE AccountNo=%s", 
                data
            )
            con.commit()
            print("*" * 20)
            print("Data Updated")
            print("*" * 20)
    except Exception as e:
        print(e)

def showpaysalarydata():
    try:
        print("1: Show All Records")
        print("2: Show Single Record")
        choice = int(input("Your Choice (1/2): "))
        if choice == 1:
            cur.execute("SELECT * FROM PaySalary")
            results = cur.fetchall()
            if not results:
                print("No Records Found")
            for row in results:
                print(f"AccountNo={row[0]}, Month={row[1]}, GivenOrNotGiven={row[2]}")
        elif choice == 2:
            AccountNo = int(input("Enter the Account No: "))
            cur.execute("SELECT * FROM PaySalary WHERE AccountNo=%s", (AccountNo,))
            r = cur.fetchone()
            if r is None:
                print("Record not found")
            else:
                print(f"AccountNo={r[0]}, Month={r[1]}, GivenOrNotGiven={r[2]}")
        else:
            print("Invalid Choice")
    except Exception as e:
        print(e)
