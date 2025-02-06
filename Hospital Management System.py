title = 'HOSPITAL MANAGEMENT'
d = '--**************--'
x = title.center(80)
y = d.center(85)
print(x)
print(y)
import mysql.connector as con

def db_setup():
    mydb = con.connect(host='localhost', user='root', passwd='root')
    cur = mydb.cursor()
    try:
        cur.execute('CREATE DATABASE IF NOT EXISTS hospital_management')
        print("Database created")
    except:
        print("Database hospital_management already exists")
    mydb.close()

def tb_setup():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()
    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS doctor (
                        ID INT PRIMARY KEY,
                        Name VARCHAR(50),
                        Phone_Number VARCHAR(15),
                        Address VARCHAR(100),
                        DOB DATE,
                        Speciality VARCHAR(50),
                        Branch VARCHAR(50),
                        Date_of_Joining DATE,
                        Date_of_Resignation DATE)''')
        print("Doctor Table setup done")

        cur.execute('''CREATE TABLE IF NOT EXISTS nurse (
                        ID INT PRIMARY KEY,
                        Name VARCHAR(50),
                        Phone_Number VARCHAR(15),
                        Address VARCHAR(100),
                        DOB DATE,
                        Department VARCHAR(50),
                        Date_of_Joining DATE)''')
        print("Nurse Table setup done")

        cur.execute('''CREATE TABLE IF NOT EXISTS patient (
                        ID INT PRIMARY KEY,
                        Name VARCHAR(50),
                        Phone_Number VARCHAR(15),
                        Address VARCHAR(100),
                        DOB DATE,
                        Date_of_Appointment DATE,
                        Branch_of_Consultancy VARCHAR(50),
                        Doctor_ID INT,
                        FOREIGN KEY (Doctor_ID) REFERENCES doctor(ID))''')
        print("Patient Table setup done")

        cur.execute('''CREATE TABLE IF NOT EXISTS pharmacy (
                        Medicine_ID INT PRIMARY KEY,
                        Medicine_Name VARCHAR(100),
                        Manufacturing_Date DATE,
                        Expiry_Date DATE,
                        Medicine_Price DECIMAL(10,2),
                        Units_Available INT)''')
        print("Pharmacy Table setup done")

        cur.execute('''CREATE TABLE IF NOT EXISTS ward (
                        Ward_ID INT PRIMARY KEY,
                        Name VARCHAR(50),
                        Beds_Available INT,
                        Daily_Rent DECIMAL(10,2),
                        Nurse_ID INT,
                        FOREIGN KEY (Nurse_ID) REFERENCES nurse(ID))''')
        print("Ward Table setup done")

    except Exception as e:
        print("Error:", e)

    mydb.close()

def database_setup():
    while True:
        print("\nPress 1 to setup database")
        print("Press 2 to setup tables")
        print("Press 3 to go back to main menu\n")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            db_setup()
        elif ch == 2:
            tb_setup()
        elif ch == 3:
            return
        else:
            print("Invalid choice")

# Function to validate date
from datetime import datetime

def format_valid_date(date_str):
    """
    Validates and formats a date from 'DD/MM/YYYY' to 'YYYY-MM-DD'.
    Returns the formatted date if valid, else returns None.
    """
    try:
        day, month, year = map(int, date_str.split('/'))
        
        # Check if the date is valid
        if not is_valid_date(day, month, year):
            print("Error: Invalid date entered.")
            return None

        # Convert to 'YYYY-MM-DD' format
        return datetime(year, month, day).strftime("%Y-%m-%d")
    
    except ValueError:
        print("Error: Invalid date format. Please enter in 'DD/MM/YYYY'.")
        return None

def is_valid_date(day, month, year):
    """Checks if the given day, month, and year form a valid date."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_day = 29  # Leap year
        else:
            max_day = 28
    else:
        return False  # Invalid month

    return 1 <= day <= max_day

# Doctor Management
def add_doctor():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    while True:
    try:
        ID = int(input("Enter doctor ID: "))
        break
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

    Name = input("Enter doctor name: ")
    Phone_Number = input("Enter doctor phone number: ")
    Address = input("Enter doctor address: ")
    DOB = format_valid_date(input("Enter doctor date of birth (dd/mm/yyyy): "))
    Speciality = input("Enter doctor speciality: ")
    Branch = input("Enter branch: ")
    Date_of_Joining = input("Enter date of joining (dd/mm/yyyy): ")
    Date_of_Resignation = input("Enter date of resignation (dd/mm/yyyy) or leave empty if still working: ")
    Date_of_Resignation = format_valid_date(Date_of_Resignation) if Date_of_Resignation else None

    z = "INSERT INTO doctor (ID, Name, Phone_Number, Address, DOB, Speciality, Branch, Date_of_Joining, Date_of_Resignation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    y = (ID, Name, Phone_Number, Address, DOB, Speciality, Branch, Date_of_Joining, Date_of_Resignation)
    
    cur.execute(z, y)
    mydb.commit()
    mydb.close()
    print("Doctor added successfully")

def update_doctor():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter doctor ID to update: "))
    print("1. Update Name")
    print("2. Update Phone Number")
    print("3. Update Address")
    print("4. Update Speciality")
    print("5. Update Branch")
    print("6. Update Date of Joining")
    print("7. Update Date of Resignation")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        Name = input("Enter updated name: ")
        z = "UPDATE doctor SET Name=%s WHERE ID=%s"
        y = (Name, ID)
    elif choice == 2:
        Phone_Number = input("Enter updated phone number: ")
        z = "UPDATE doctor SET Phone_Number=%s WHERE ID=%s"
        y = (Phone_Number, ID)
    elif choice == 3:
        Address = input("Enter updated address: ")
        z = "UPDATE doctor SET Address=%s WHERE ID=%s"
        y = (Address, ID)
    elif choice == 4:
        Speciality = input("Enter updated speciality: ")
        z = "UPDATE doctor SET Speciality=%s WHERE ID=%s"
        y = (Speciality, ID)
    elif choice == 5:
        Branch = input("Enter updated branch: ")
        z = "UPDATE doctor SET Branch=%s WHERE ID=%s"
        y = (Branch, ID)
    elif choice == 6:
        Date_of_Joining = input("Enter updated date of joining (dd/mm/yyyy): ")
        z = "UPDATE doctor SET Date_of_Joining=%s WHERE ID=%s"
        y = (Date_of_Joining, ID)
    elif choice == 7:
        Date_of_Resignation = input("Enter updated date of resignation (dd/mm/yyyy) or leave empty if still working: ")
        z = "UPDATE doctor SET Date_of_Resignation=%s WHERE ID=%s"
        y = (Date_of_Resignation, ID)
    else:
        print("Invalid choice")
        return

    cur.execute(z, y)
    if cur.rowcount > 0:
        print("Doctor details updated successfully")
    else:
        print("No doctor found with the provided ID")
    mydb.commit()
    mydb.close()

def delete_doctor():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter doctor ID to delete: "))
    z = "DELETE FROM doctor WHERE ID=%s"
    y = (ID,)

    cur.execute(z, y)
    if cur.rowcount > 0:
        print("Doctor deleted successfully")
    else:
        print("No doctor found with the provided ID")
    mydb.commit()
    mydb.close()

def display_doctors():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()
    while True:
        print('\nPress 1 to display all doctor records')
        print('Press 2 to display a specific doctor')
        print('Press 3 to return\n')
        choice = int(input("Enter choice: "))
        if choice == 1:
            cur.execute("SELECT * FROM doctor")
            records = cur.fetchall()
            print('|Doctor_ID| |Name| |Speciality| |Phone Number| |Address| |Branch|')
            for record in records:
                print(" | ".join(map(str, record)))
            print("Doctor records successfully displayed")
        elif choice == 2:
            doctor_id = int(input("Enter doctor ID: "))
            cur.execute("SELECT * FROM doctor WHERE ID=%s", (doctor_id,))
            record = cur.fetchone()
            if record:
                print(" | ".join(map(str, record)))
            else:
                print("No doctor found with the provided ID")
        elif choice == 3:
            break
        else:
            print("Invalid choice")
    mydb.close()

# Nurse Management
def add_nurse():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter nurse ID: "))
    Name = input("Enter nurse name: ")
    Phone_Number = input("Enter nurse phone number: ")
    Address = input("Enter nurse address: ")
    DOB = format_valid_date(input("Enter nurse date of birth (dd/mm/yyyy): "))
    Department = input("Enter nurse department: ")
    Date_of_Joining = input("Enter date of joining (dd/mm/yyyy): ")

    z = "INSERT INTO nurse (ID, Name, Phone_Number, Address, DOB, Department, Date_of_Joining) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    y = (ID, Name, Phone_Number, Address, DOB, Department, Date_of_Joining)
    
    cur.execute(z, y)
    mydb.commit()
    mydb.close()
    print("Nurse added successfully")

def update_nurse():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter nurse ID to update: "))
    print("1. Update Name")
    print("2. Update Phone Number")
    print("3. Update Address")
    print("4. Update Department")
    print("5. Update Date of Joining")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        Name = input("Enter updated name: ")
        z = "UPDATE nurse SET Name=%s WHERE ID=%s"
        y = (Name, ID)
    elif choice == 2:
        Phone_Number = input("Enter updated phone number: ")
        z = "UPDATE nurse SET Phone_Number=%s WHERE ID=%s"
        y = (Phone_Number, ID)
    elif choice == 3:
        Address = input("Enter updated address: ")
        z = "UPDATE nurse SET Address=%s WHERE ID=%s"
        y = (Address, ID)
    elif choice == 4:
        Department = input("Enter updated department: ")
        z = "UPDATE nurse SET Department=%s WHERE ID=%s"
        y = (Department, ID)
    elif choice == 5:
        Date_of_Joining = input("Enter updated date of joining (dd/mm/yyyy): ")
        z = "UPDATE nurse SET Date_of_Joining=%s WHERE ID=%s"
        y = (Date_of_Joining, ID)
    else:
        print("Invalid choice")
        return

    cur.execute(z, y)
    if cur.rowcount > 0:
        print("Nurse details updated successfully")
    else:
        print("No nurse found with the provided ID")
    mydb.commit()
    mydb.close()

def delete_nurse():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter nurse ID to delete: "))
    z = "DELETE FROM nurse WHERE ID=%s"
    y = (ID,)

    cur.execute(z, y)
    if cur.rowcount > 0:
        print("Nurse deleted successfully")
    else:
        print("No nurse found with the provided ID")
    mydb.commit()
    mydb.close()

def display_nurses():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()
    while True:
        print('\nPress 1 to display all nurse records')
        print('Press 2 to display a specific nurse')
        print('Press 3 to return\n')
        choice = int(input("Enter choice: "))
        if choice == 1:
            cur.execute("SELECT * FROM nurse")
            records = cur.fetchall()
            print('|Nurse_ID| |Name| |Department| |Phone Number| |Address|')
            for record in records:
                print(" | ".join(map(str, record)))
            print("Nurse records successfully displayed")
        elif choice == 2:
            nurse_id = int(input("Enter nurse ID: "))
            cur.execute("SELECT * FROM nurse WHERE ID=%s", (nurse_id,))
            record = cur.fetchone()
            if record:
                print(" | ".join(map(str, record)))
            else:
                print("No nurse found with the provided ID")
        elif choice == 3:
            break
        else:
            print("Invalid choice")
    mydb.close()


# Labour Management
def add_labour():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter labour ID: "))
    Name = input("Enter labour name: ")
    Phone_Number = input("Enter labour phone number: ")
    Address = input("Enter labour address: ")
    DOB = format_valid_date(input("Enter labour date of birth (dd/mm/yyyy): "))
    Department = input("Enter labour department: ")
    Date_of_Joining = input("Enter date of joining (dd/mm/yyyy): ")

    z = "INSERT INTO labour (ID, Name, Phone_Number, Address, DOB, Department, Date_of_Joining) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    y = (ID, Name, Phone_Number, Address, DOB, Department, Date_of_Joining)
    
    cur.execute(z, y)
    mydb.commit()
    mydb.close()
    print("Labour added successfully")

def update_labour():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter labour ID to update: "))
    print("1. Update Name")
    print("2. Update Phone Number")
    print("3. Update Address")
    print("4. Update Department")
    print("5. Update Date of Joining")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        Name = input("Enter updated name: ")
        z = "UPDATE labour SET Name=%s WHERE ID=%s"
        y = (Name, ID)
    elif choice == 2:
        Phone_Number = input("Enter updated phone number: ")
        z = "UPDATE labour SET Phone_Number=%s WHERE ID=%s"
        y = (Phone_Number, ID)
    elif choice == 3:
        Address = input("Enter updated address: ")
        z = "UPDATE labour SET Address=%s WHERE ID=%s"
        y = (Address, ID)
    elif choice == 4:
        Department = input("Enter updated department: ")
        z = "UPDATE labour SET Department=%s WHERE ID=%s"
        y = (Department, ID)
    elif choice == 5:
        Date_of_Joining = input("Enter updated date of joining (dd/mm/yyyy): ")
        z = "UPDATE labour SET Date_of_Joining=%s WHERE ID=%s"
        y = (Date_of_Joining, ID)
    else:
        print("Invalid choice")
        return

    cur.execute(z, y)
    if cur.rowcount > 0:
        print("Labour details updated successfully")
    else:
        print("No labour found with the provided ID")
    mydb.commit()
    mydb.close()

def delete_labour():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter labour ID to delete: "))
    z = "DELETE FROM labour WHERE ID=%s"
    y = (ID,)

    cur.execute(z, y)
    if cur.rowcount > 0:
        print("Labour deleted successfully")
    else:
        print("No labour found with the provided ID")
    mydb.commit()
    mydb.close()

def display_labours():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()
    
    while True:
        print('\nPress 1 to display all labour records')
        print('Press 2 to display a specific labour')
        print('Press 3 to return\n')
        choice = int(input("Enter choice: "))

        if choice == 1:
            cur.execute("SELECT * FROM labour")
            records = cur.fetchall()
            print('|Labour_ID| |Name| |Phone Number| |Address| |DOB| |Department| |Date of Joining|')
            for record in records:
                print(" | ".join(map(str, record)))
            print("Labour records successfully displayed")
        
        elif choice == 2:
            labour_id = int(input("Enter labour ID: "))
            cur.execute("SELECT * FROM labour WHERE ID=%s", (labour_id,))
            record = cur.fetchone()
            if record:
                print(" | ".join(map(str, record)))
            else:
                print("No labour found with the provided ID")

        elif choice == 3:
            break
        else:
            print("Invalid choice")
    
    mydb.close()


# Patient Management

def add_patient():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter patient ID: "))
    Name = input("Enter patient name: ")
    Phone_Number = input("Enter patient phone number: ")
    Address = input("Enter patient address: ")
    DOB = format_valid_date(input("Enter patient date of birth (dd/mm/yyyy): "))
    Date_of_Appointment = format_valid_date(input("Enter date of appointment (dd/mm/yyyy): "))
    Branch_of_Consultancy = input("Enter branch of consultancy: ")
    Doctor_ID = int(input("Enter Doctor ID: "))
    
    cur.execute("SELECT Name, Speciality FROM doctor WHERE ID=%s", (Doctor_ID,))
    doctor = cur.fetchone()
    if not doctor:
        print("Error: Doctor ID does not exist.")
        return

    Doctor_Name, Speciality = doctor
    
    cur.execute("INSERT INTO patient (ID, Name, Phone_Number, Address, DOB, Date_of_Appointment, Branch_of_Consultancy, Doctor_ID, Doctor_Name, Speciality) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (ID, Name, Phone_Number, Address, DOB, Date_of_Appointment, Branch_of_Consultancy, Doctor_ID, Doctor_Name, Speciality))
    mydb.commit()
    
    admitted = input("Is the patient admitted? (yes/no): ").lower()
    if admitted == 'yes':
        Ward_ID = int(input("Enter ward ID: "))
        cur.execute("SELECT Daily_Rent FROM ward WHERE ID=%s", (Ward_ID,))
        ward = cur.fetchone()
        
        if not ward:
            print("Error: Ward ID does not exist.")
            return
        
        cur.execute("INSERT INTO admission (Patient_ID, Ward_ID) VALUES (%s, %s)", (ID, Ward_ID))
        mydb.commit()
    
    mydb.close()
    print("Patient added successfully")

def update_patient():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter patient ID to update: "))
    print("1. Update Name")
    print("2. Update Phone Number")
    print("3. Update Address")
    print("4. Update Date of Birth")
    print("5. Update Date of Appointment")
    print("6. Update Branch of Consultancy")
    print("7. Update Ward")
    print("8. Update Doctor")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_value = input("Enter updated name: ")
        column = "Name"
    elif choice == 2:
        new_value = input("Enter updated phone number: ")
        column = "Phone_Number"
    elif choice == 3:
        new_value = input("Enter updated address: ")
        column = "Address"
    elif choice == 4:
        new_value = input("Enter updated date of birth (dd/mm/yyyy): ")
        column = "DOB"
    elif choice == 5:
        new_value = input("Enter updated date of appointment (dd/mm/yyyy): ")
        column = "Date_of_Appointment"
    elif choice == 6:
        new_value = input("Enter updated branch of consultancy: ")
        column = "Branch_of_Consultancy"
    elif choice == 7:
        new_value = int(input("Enter updated ward ID: "))
        cur.execute("SELECT ID FROM ward WHERE ID=%s", (new_value,))
        if not cur.fetchone():
            print("Error: Ward ID does not exist.")
            return
        column = "Ward_ID"
    elif choice == 8:
        new_value = int(input("Enter updated doctor ID: "))
        cur.execute("SELECT ID FROM doctor WHERE ID=%s", (new_value,))
        if not cur.fetchone():
            print("Error: Doctor ID does not exist.")
            return
        column = "Doctor_ID"
    else:
        print("Invalid choice")
        return
    
    query = f"UPDATE patient SET {column} = %s WHERE ID = %s"
    cur.execute(query, (new_value, ID))
    if cur.rowcount > 0:
        print("Patient details updated successfully")
    else:
        print("No patient found with the provided ID")
    mydb.commit()
    mydb.close()

def delete_patient():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter patient ID to delete: "))
    z = "DELETE FROM patient WHERE ID=%s"
    y = (ID,)

    cur.execute(z, y)
    if cur.rowcount > 0:
        print("Patient deleted successfully")
    else:
        print("No patient found with the provided ID")
    mydb.commit()
    mydb.close()

def display_patients():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()
    while True:
        print('\nPress 1 to display all patient records')
        print('Press 2 to display a specific patient')
        print('Press 3 to return\n')
        choice = int(input("Enter choice: "))
        if choice == 1:
            cur.execute("SELECT * FROM patient")
            records = cur.fetchall()
            print('|Patient_ID| |Name| |Phone Number| |Address| |DOB| |Date of Appointment| |Branch of Consultancy| |Doctor_ID|')
            for record in records:
                print(" | ".join(map(str, record)))
            print("Patient records successfully displayed")
        elif choice == 2:
            patient_id = int(input("Enter patient ID: "))
            cur.execute("SELECT * FROM patient WHERE ID=%s", (patient_id,))
            record = cur.fetchone()
            if record:
                print(" | ".join(map(str, record)))
            else:
                print("No patient found with the provided ID")
        elif choice == 3:
            break
        else:
            print("Invalid choice")
    mydb.close()

# Pharmacy Management
def add_pharmacy():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    Medicine_ID = int(input("Enter medicine ID: "))
    Medicine_Name = input("Enter medicine name: ")
    
    Mfg_Day, Mfg_Month, Mfg_Year = map(int, input("Enter medicine manufacturing date (dd mm yyyy): ").split())
    if not is_valid_date(Mfg_Day, Mfg_Month, Mfg_Year):
        print("Error: Invalid manufacturing date.")
        return
    Manufacturing_Date = f"{Mfg_Year}-{Mfg_Month:02d}-{Mfg_Day:02d}"
    
    Exp_Day, Exp_Month, Exp_Year = map(int, input("Enter medicine expiry date (dd mm yyyy): ").split())
    if not is_valid_date(Exp_Day, Exp_Month, Exp_Year):
        print("Error: Invalid expiry date.")
        return
    Expiry_Date = f"{Exp_Year}-{Exp_Month:02d}-{Exp_Day:02d}"
    
    Medicine_Price = float(input("Enter medicine price: "))
    Units_Available = int(input("Enter units available: "))
    
    cur.execute("INSERT INTO pharmacy (Medicine_ID, Medicine_Name, Manufacturing_Date, Expiry_Date, Medicine_Price, Units_Available) VALUES (%s, %s, %s, %s, %s, %s)",
                (Medicine_ID, Medicine_Name, Manufacturing_Date, Expiry_Date, Medicine_Price, Units_Available))
    mydb.commit()
    mydb.close()
    print("Medicine added successfully")

def update_pharmacy():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    Medicine_ID = int(input("Enter medicine ID to update: "))
    print("1. Update Medicine Name")
    print("2. Update Manufacturing Date")
    print("3. Update Expiry Date")
    print("4. Update Medicine Price")
    print("5. Update Units Available")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        new_value = input("Enter updated medicine name: ")
        column = "Medicine_Name"
    elif choice == 2:
        day, month, year = map(int, input("Enter updated manufacturing date (dd mm yyyy): ").split())
        if not is_valid_date(day, month, year):
            print("Error: Invalid manufacturing date.")
            return
        new_value = f"{year}-{month:02d}-{day:02d}"
        column = "Manufacturing_Date"
    elif choice == 3:
        day, month, year = map(int, input("Enter updated expiry date (dd mm yyyy): ").split())
        if not is_valid_date(day, month, year):
            print("Error: Invalid expiry date.")
            return
        new_value = f"{year}-{month:02d}-{day:02d}"
        column = "Expiry_Date"
    elif choice == 4:
        new_value = float(input("Enter updated medicine price: "))
        column = "Medicine_Price"
    elif choice == 5:
        new_value = int(input("Enter updated units available: "))
        column = "Units_Available"
    else:
        print("Invalid choice")
        return
    
    query = f"UPDATE pharmacy SET {column} = %s WHERE Medicine_ID = %s"
    cur.execute(query, (new_value, Medicine_ID))
    if cur.rowcount > 0:
        print("Medicine details updated successfully")
    else:
        print("No medicine found with the provided ID")
    mydb.commit()
    mydb.close()

def delete_pharmacy():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    Medicine_ID = int(input("Enter medicine ID to delete: "))
    cur.execute("DELETE FROM pharmacy WHERE Medicine_ID = %s", (Medicine_ID,))
    if cur.rowcount > 0:
        print("Medicine deleted successfully")
    else:
        print("No medicine found with the provided ID")
    mydb.commit()
    mydb.close()
    
def display_pharmacy():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()
    while True:
        print('\nPress 1 to display all pharmacy records')
        print('Press 2 to display a specific medicine')
        print('Press 3 to return\n')
        choice = int(input("Enter choice: "))
        if choice == 1:
            cur.execute("SELECT * FROM pharmacy")
            records = cur.fetchall()
            print('|Medicine_ID| |Medicine_Name| |Manufacturing_Date| |Expiry_Date| |Medicine_Price| |Units_Available|')
            for record in records:
                print(" | ".join(map(str, record)))
            print("Pharmacy records successfully displayed")
        elif choice == 2:
            medicine_id = int(input("Enter medicine ID: "))
            cur.execute("SELECT * FROM pharmacy WHERE Medicine_ID=%s", (medicine_id,))
            record = cur.fetchone()
            if record:
                print(" | ".join(map(str, record)))
            else:
                print("No medicine found with the provided ID")
        elif choice == 3:
            break
        else:
            print("Invalid choice")
    mydb.close()



# Ward Management
def add_ward():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter ward ID: "))
    Name = input("Enter ward name: ")
    Beds_Available = int(input("Enter number of beds available: "))
    Daily_Rent = float(input("Enter daily rent: "))
    Nurse_ID = int(input("Enter Nurse ID: "))
    
    cur.execute("SELECT Name FROM nurse WHERE ID=%s", (Nurse_ID,))
    nurse = cur.fetchone()
    if not nurse:
        print("Error: Nurse ID does not exist.")
        return
    
    cur.execute("INSERT INTO ward (ID, Name, Beds_Available, Daily_Rent, Nurse_ID) VALUES (%s, %s, %s, %s, %s)",
                (ID, Name, Beds_Available, Daily_Rent, Nurse_ID))
    mydb.commit()
    mydb.close()
    print("Ward added successfully")

def update_ward():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter ward ID to update: "))
    print("1. Update Name")
    print("2. Update Beds Available")
    print("3. Update Daily Rent")
    print("4. Update Nurse ID")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        new_value = input("Enter updated ward name: ")
        column = "Name"
    elif choice == 2:
        new_value = int(input("Enter updated number of beds available: "))
        column = "Beds_Available"
    elif choice == 3:
        new_value = float(input("Enter updated daily rent: "))
        column = "Daily_Rent"
    elif choice == 4:
        new_value = int(input("Enter updated Nurse ID: "))
        cur.execute("SELECT ID FROM nurse WHERE ID=%s", (new_value,))
        if not cur.fetchone():
            print("Error: Nurse ID does not exist.")
            return
        column = "Nurse_ID"
    else:
        print("Invalid choice")
        return
    
    query = f"UPDATE ward SET {column} = %s WHERE ID = %s"
    cur.execute(query, (new_value, ID))
    if cur.rowcount > 0:
        print("Ward details updated successfully")
    else:
        print("No ward found with the provided ID")
    mydb.commit()
    mydb.close()



def delete_ward():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    Name = input("Enter ward name to delete: ")
    z = "DELETE FROM ward WHERE Name=%s"
    y = (Name,)

    cur.execute(z, y)
    if cur.rowcount > 0:
        print("Ward deleted successfully")
    else:
        print("No ward found with the provided name")
    mydb.commit()
    mydb.close()

def display_wards():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()
    
    while True:
        print('\nPress 1 to display all ward records')
        print('Press 2 to display a specific ward')
        print('Press 3 to return\n')
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            cur.execute("SELECT * FROM ward")
            records = cur.fetchall()
            print('|Ward_ID| |Ward_Name| |Beds_Available| |Daily_Rent| |Nurse_ID|')
            for record in records:
                print(" | ".join(map(str, record)))
            print("Ward records successfully displayed")
        
        elif choice == 2:
            ward_id = int(input("Enter ward ID: "))
            cur.execute("SELECT * FROM ward WHERE ID=%s", (ward_id,))
            record = cur.fetchone()
            if record:
                print(" | ".join(map(str, record)))
            else:
                print("No ward found with the provided ID")
        
        elif choice == 3:
            break
        else:
            print("Invalid choice")
    
    mydb.close()

# Main Program Loop
def main():
    while True:
        print("\nHospital Management System")
        print("1. Database Setup")
        print("2. Doctor Management")
        print("3. Nurse Management")
        print("4. Labour Management")
        print("5. Patient Management")
        print("6. Pharmacy Management")
        print("7. Ward Management")
        print("8. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            database_setup()
        elif choice == 2:
            print("\nDoctor Management")
            print("1. Add Doctor")
            print("2. Update Doctor")
            print("3. Delete Doctor")
            print("4. Display Doctors")
            sub_choice = int(input("Enter your choice: "))

            if sub_choice == 1:
                add_doctor()
            elif sub_choice == 2:
                update_doctor()
            elif sub_choice == 3:
                delete_doctor()
            elif sub_choice == 4:
                display_doctors()
            else:
                print("Invalid choice")
        
        elif choice == 3:
            print("\nNurse Management")
            print("1. Add Nurse")
            print("2. Update Nurse")
            print("3. Delete Nurse")
            print("4. Display Nurses")
            sub_choice = int(input("Enter your choice: "))

            if sub_choice == 1:
                add_nurse()
            elif sub_choice == 2:
                update_nurse()
            elif sub_choice == 3:
                delete_nurse()
            elif sub_choice == 4:
                display_nurses()
            else:
                print("Invalid choice")
        
        elif choice == 4:
            print("\nLabour Management")
            print("1. Add Labour")
            print("2. Update Labour")
            print("3. Delete Labour")
            print("4. Display Labours")
            sub_choice = int(input("Enter your choice: "))

            if sub_choice == 1:
                add_labour()
            elif sub_choice == 2:
                update_labour()
            elif sub_choice == 3:
                delete_labour()
            elif sub_choice == 4:
                display_labours()
            else:
                print("Invalid choice")

        elif choice == 5:
            print("\nPatient Management")
            print("1. Add Patient")
            print("2. Update Patient")
            print("3. Delete Patient")
            print("4. Display Patients")
            sub_choice = int(input("Enter your choice: "))

            if sub_choice == 1:
                add_patient()
            elif sub_choice == 2:
                update_patient()
            elif sub_choice == 3:
                delete_patient()
            elif sub_choice == 4:
                display_patients()
            else:
                print("Invalid choice")

        elif choice == 6:
            print("\nPharmacy Management")
            print("1. Add Medicine")
            print("2. Update Medicine")
            print("3. Delete Medicine")
            print("4. Display Pharmacy Records")
            sub_choice = int(input("Enter your choice: "))

            if sub_choice == 1:
                add_pharmacy()
            elif sub_choice == 2:
                update_pharmacy()
            elif sub_choice == 3:
                delete_pharmacy()
            elif sub_choice == 4:
                display_pharmacy()
            else:
                print("Invalid choice")

        elif choice == 7:
            print("\nWard Management")
            print("1. Add Ward")
            print("2. Update Ward")
            print("3. Delete Ward")
            print("4. Display Wards")
            sub_choice = int(input("Enter your choice: "))

            if sub_choice == 1:
                add_ward()
            elif sub_choice == 2:
                update_ward()
            elif sub_choice == 3:
                delete_ward()
            elif sub_choice == 4:
                display_wards()
            else:
                print("Invalid choice")

        elif choice == 8:
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
