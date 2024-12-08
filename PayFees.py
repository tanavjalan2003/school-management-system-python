import mysql.connector as m

# Establishing connection to the database
con = m.connect(host="localhost", user="root", passwd="password", database="csproject")
cur = con.cursor()

def insertpayfees():
    try:
        RollNo = int(input("Enter the Roll No: "))
        Month = input("Enter the Month: ")
        PaidOrNotPaid = input("Enter Fees Paid or Not Paid: ")
        data = (RollNo, Month, PaidOrNotPaid)
        sql = "INSERT INTO PayFees (RollNo, Month, PaidOrNotPaid) VALUES (%s, %s, %s)"
        cur.execute(sql, data)
        con.commit()
        print("*" * 20)
        print("Data Entered")
        print("*" * 20)
    except Exception as e:
        print(e)

def deletepayfees():
    try:
        RollNo = int(input("Enter the Roll No to Delete Fees Record: "))
        d = (RollNo,)
        cur.execute("SELECT * FROM PayFees WHERE RollNo=%s", d)
        r = cur.fetchone()
        if r is None:
            print("Record not found")
        else:
            cur.execute("DELETE FROM PayFees WHERE RollNo=%s", d)
            con.commit()
            print("*" * 20)
            print("Data Removed")
            print("*" * 20)
    except Exception as e:
        print(e)

def updatepayfees():
    try:
        RollNo = int(input("Enter the Roll No to Update Fees Record: "))
        d = (RollNo,)
        cur.execute("SELECT * FROM PayFees WHERE RollNo=%s", d)
        r = cur.fetchone()
        if r is None:
            print("Record not found")
        else:
            Month = input("Enter the New Month: ")
            PaidOrNotPaid = input("Enter Fees Paid or Not Paid: ")
            data = (Month, PaidOrNotPaid, RollNo)
            cur.execute(
                "UPDATE PayFees SET Month=%s, PaidOrNotPaid=%s WHERE RollNo=%s", 
                data
            )
            con.commit()
            print("*" * 20)
            print("Data Updated")
            print("*" * 20)
    except Exception as e:
        print(e)

def showpayfeesdata():
    try:
        print("1: Show All Records")
        print("2: Show Single Record")
        choice = int(input("Your Choice (1/2): "))
        if choice == 1:
            cur.execute("SELECT * FROM PayFees")
            results = cur.fetchall()
            if not results:
                print("No Records Found")
            for row in results:
                print(f"RollNo={row[0]}, Month={row[1]}, PaidOrNotPaid={row[2]}")
        elif choice == 2:
            RollNo = int(input("Enter the Roll No: "))
            cur.execute("SELECT * FROM PayFees WHERE RollNo=%s", (RollNo,))
            r = cur.fetchone()
            if r is None:
                print("Record not found")
            else:
                print(f"RollNo={r[0]}, Month={r[1]}, PaidOrNotPaid={r[2]}")
        else:
            print("Invalid Choice")
    except Exception as e:
        print(e)
