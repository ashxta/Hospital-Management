title = 'HOSPITAL MANAGEMENT'
d = '--**************--'
x = title.center(80)
y = d.center(85)
print(x)
print(y)
import mysql.connector as con

# Function to validate date
def is_valid_date(day, month, year):
    # Check if the day, month, and year form a valid date
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    else:
        return False
    
    if 1 <= day <= max_day:
        return True
    else:
        return False

# Doctor Management
def add_doctor():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter doctor ID: "))
    Name = input("Enter doctor name: ")
    Phone_Number = input("Enter doctor phone number: ")
    Address = input("Enter doctor address: ")
    DOB = input("Enter doctor date of birth (dd/mm/yyyy): ")
    Speciality = input("Enter doctor speciality: ")
    Branch = input("Enter branch: ")
    Date_of_Joining = input("Enter date of joining (dd/mm/yyyy): ")
    Date_of_Resignation = input("Enter date of resignation (dd/mm/yyyy) or leave empty if still working: ")

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

    specific = input("Do you want to display specific ID (yes/no)? ")
    if specific.lower() == 'yes':
        ID = int(input("Enter doctor ID: "))
        cur.execute("SELECT * FROM doctor WHERE ID=%s", (ID,))
        doctors = cur.fetchall()
    else:
        cur.execute("SELECT * FROM doctor")
        doctors = cur.fetchall()

    if doctors:
        print("ID\tName\tPhone Number\tAddress\tDOB\tSpeciality\tBranch\tDate of Joining\tDate of Resignation")
        for doctor in doctors:
            print(f"{doctor[0]}\t{doctor[1]}\t{doctor[2]}\t{doctor[3]}\t{doctor[4]}\t{doctor[5]}\t{doctor[6]}\t{doctor[7]}\t{doctor[8]}")
    else:
        print("No doctors found")

    mydb.close()

# Nurse Management
def add_nurse():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter nurse ID: "))
    Name = input("Enter nurse name: ")
    Phone_Number = input("Enter nurse phone number: ")
    Address = input("Enter nurse address: ")
    DOB = input("Enter nurse date of birth (dd/mm/yyyy): ")
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

    specific = input("Do you want to display specific ID (yes/no)? ")
    if specific.lower() == 'yes':
        ID = int(input("Enter nurse ID: "))
        cur.execute("SELECT * FROM nurse WHERE ID=%s", (ID,))
        nurses = cur.fetchall()
    else:
        cur.execute("SELECT * FROM nurse")
        nurses = cur.fetchall()

    if nurses:
        print("ID\tName\tPhone Number\tAddress\tDOB\tDepartment\tDate of Joining")
        for nurse in nurses:
            print(f"{nurse[0]}\t{nurse[1]}\t{nurse[2]}\t{nurse[3]}\t{nurse[4]}\t{nurse[5]}\t{nurse[6]}")
    else:
        print("No nurses found")

    mydb.close()

# Labour Management
def add_labour():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter labour ID: "))
    Name = input("Enter labour name: ")
    Phone_Number = input("Enter labour phone number: ")
    Address = input("Enter labour address: ")
    DOB = input("Enter labour date of birth (dd/mm/yyyy): ")
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

    specific = input("Do you want to display specific ID (yes/no)? ")
    if specific.lower() == 'yes':
        ID = int(input("Enter labour ID: "))
        cur.execute("SELECT * FROM labour WHERE ID=%s", (ID,))
        labours = cur.fetchall()
    else:
        cur.execute("SELECT * FROM labour")
        labours = cur.fetchall()

    if labours:
        print("ID\tName\tPhone Number\tAddress\tDOB\tDepartment\tDate of Joining")
        for labour in labours:
            print(f"{labour[0]}\t{labour[1]}\t{labour[2]}\t{labour[3]}\t{labour[4]}\t{labour[5]}\t{labour[6]}")
    else:
        print("No labours found")

    mydb.close()

# Patient Management
def add_patient():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter patient ID: "))
    Name = input("Enter patient name: ")
    Phone_Number = input("Enter patient phone number: ")
    Address = input("Enter patient address: ")
    DOB = input("Enter patient date of birth (dd/mm/yyyy): ")
    Date_of_Appointment = input("Enter date of appointment (dd/mm/yyyy): ")
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

import mysql.connector as con

def add_patient():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter patient ID: "))
    Name = input("Enter patient name: ")
    Phone_Number = input("Enter patient phone number: ")
    Address = input("Enter patient address: ")
    DOB = input("Enter patient date of birth (dd/mm/yyyy): ")
    Date_of_Appointment = input("Enter date of appointment (dd/mm/yyyy): ")
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

    specific = input("Do you want to display specific ID (yes/no)? ")
    if specific.lower() == 'yes':
        ID = int(input("Enter patient ID: "))
        cur.execute("SELECT * FROM patient WHERE ID=%s", (ID,))
        patients = cur.fetchall()
    else:
        cur.execute("SELECT * FROM patient")
        patients = cur.fetchall()

    if patients:
        print("ID\tName\tPhone Number\tAddress\tDOB\tDate of Appointment\tBranch of Consultancy")
        for patient in patients:
            print(f"{patient[0]}\t{patient[1]}\t{patient[2]}\t{patient[3]}\t{patient[4]}\t{patient[5]}\t{patient[6]}")
    else:
        print("No patients found")

    mydb.close()

# Pharmacy Management
def add_pharmacy():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter pharmacy ID: "))
    Name = input("Enter pharmacy name: ")
    Phone_Number = input("Enter pharmacy phone number: ")
    Address = input("Enter pharmacy address: ")
    DOB = input("Enter pharmacy date of birth (dd/mm/yyyy): ")
    Date_of_Joining = input("Enter date of joining (dd/mm/yyyy): ")

    z = "INSERT INTO pharmacy (ID, Name, Phone_Number, Address, DOB, Date_of_Joining) VALUES (%s, %s, %s, %s, %s, %s)"
    y = (ID, Name, Phone_Number, Address, DOB, Date_of_Joining)
    
    cur.execute(z, y)
    mydb.commit()
    mydb.close()
    print("Pharmacy added successfully")

def update_pharmacy():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter pharmacy ID to update: "))
    print("1. Update Name")
    print("2. Update Phone Number")
    print("3. Update Address")
    print("4. Update Date of Birth")
    print("5. Update Date of Joining")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        Name = input("Enter updated name: ")
        z = "UPDATE pharmacy SET Name=%s WHERE ID=%s"
        y = (Name, ID)
    elif choice == 2:
        Phone_Number = input("Enter updated phone number: ")
        z = "UPDATE pharmacy SET Phone_Number=%s WHERE ID=%s"
        y = (Phone_Number, ID)
    elif choice == 3:
        Address = input("Enter updated address: ")
        z = "UPDATE pharmacy SET Address=%s WHERE ID=%s"
        y = (Address, ID)
    elif choice == 4:
        DOB = input("Enter updated date of birth (dd/mm/yyyy): ")
        z = "UPDATE pharmacy SET DOB=%s WHERE ID=%s"
        y = (DOB, ID)
    elif choice == 5:
        Date_of_Joining = input("Enter updated date of joining (dd/mm/yyyy): ")
        z = "UPDATE pharmacy SET Date_of_Joining=%s WHERE ID=%s"
        y = (Date_of_Joining, ID)
    else:
        print("Invalid choice")
        return

    cur.execute(z, y)
    if cur.rowcount > 0:
        print("Pharmacy details updated successfully")
    else:
        print("No pharmacy found with the provided ID")
    mydb.commit()
    mydb.close()

def delete_pharmacy():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    ID = int(input("Enter pharmacy ID to delete: "))
    z = "DELETE FROM pharmacy WHERE ID=%s"
    y = (ID,)

    cur.execute(z, y)
    if cur.rowcount > 0:
        print("Pharmacy deleted successfully")
    else:
        print("No pharmacy found with the provided ID")
    mydb.commit()
    mydb.close()

def display_pharmacies():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='hospital_management')
    cur = mydb.cursor()

    specific = input("Do you want to display specific ID (yes/no)? ")
    if specific.lower() == 'yes':
        ID = int(input("Enter pharmacy ID: "))
        cur.execute("SELECT * FROM pharmacy WHERE ID=%s", (ID,))
        pharmacies = cur.fetchall()
    else:
        cur.execute("SELECT * FROM pharmacy")
        pharmacies = cur.fetchall()

    if pharmacies:
        print("ID\tName\tPhone Number\tAddress\tDOB\tDate of Joining")
        for pharmacy in pharmacies:
            print(f"{pharmacy[0]}\t{pharmacy[1]}\t{pharmacy[2]}\t{pharmacy[3]}\t{pharmacy[4]}\t{pharmacy[5]}")
    else:
        print("No pharmacies found")

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

    specific = input("Do you want to display specific ward (yes/no)? ")
    if specific.lower() == 'yes':
        Name = input("Enter ward name: ")
        cur.execute("SELECT * FROM ward WHERE Name=%s", (Name,))
        wards = cur.fetchall()
    else:
        cur.execute("SELECT * FROM ward")
        wards = cur.fetchall()

    if wards:
        print("Name\tBeds Available\tPatients Admitted\tDaily Rent\tStaff Assigned")
        for ward in wards:
            print(f"{ward[0]}\t{ward[1]}\t{ward[2]}\t{ward[3]}\t{ward[4]}")
    else:
        print("No wards found")

    mydb.close()

# Main Program Loop
def main():
    while True:
        print("\nHospital Management System")
        print("1. Doctor")
        print("2. Nurse")
        print("3. Labour")
        print("4. Patient")
        print("5. Pharmacy")
        print("6. Ward")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
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
        elif choice == 2:
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
        elif choice == 3:
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
        elif choice == 4:
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
        elif choice == 5:
            print("\nPharmacy Management")
            print("1. Add Pharmacy")
            print("2. Update Pharmacy")
            print("3. Delete Pharmacy")
            print("4. Display Pharmacies")
            sub_choice = int(input("Enter your choice: "))

            if sub_choice == 1:
                add_pharmacy()
            elif sub_choice == 2:
                update_pharmacy()
            elif sub_choice == 3:
                delete_pharmacy()
            elif sub_choice == 4:
                display_pharmacies()
            else:
                print("Invalid choice")
        elif choice == 6:
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
        elif choice == 7:
            print("Exiting program...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
