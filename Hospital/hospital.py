

from management import *
import sqlite3
con = sqlite3.connect('Hospital_project.db')
cur = con.cursor()



def register_patient():
    try:
        cur.execute("CREATE TABLE patient_det(Id,name,age,gender,weight,height)")
        con.commit()

        cur.execute("CREATE TABLE patient_complaint(Id,complaint)")
        con.commit()
    except:
        pass


    #Form

    name = input("Enter your name: \n")
    age = int(input("Enter your age: \n"))
    gender = input('Are you a male or a female: \n')
    complaint = input('Enter your complaint: \n')
    patient_height = int(input("Enter your height (cm): \n"))
    patient_weight = int(input("Enter your weight (kg): \n "))

    #Data uploading

    cur.execute("SELECT MAX(Id) FROM patient_det")  # Check for existing IDs
    existing_max_id = cur.fetchone()[0]
    Id_no = 1 if existing_max_id is None else int(existing_max_id[2:]) + 1
    Id = "AJ" + str(Id_no)
    Id = Id.lower()
    cur.execute("INSERT INTO patient_det(Id,name,age,gender,weight,height) VALUES('{}','{}','{}','{}','{}','{}')".format(Id,name,age,gender,patient_height,patient_weight))
    con.commit()

    cur.execute("INSERT INTO patient_complaint(Id,complaint) VALUES('{}','{}')".format(Id,complaint))
    con.commit()

    return f'You have been registered. Your card number is {Id}'

def existing_patient():

    patient_id = input("Enter your hospital Id")
    patient_id = patient_id.lower()

    #Authentication
    cur.execute("SELECT * FROM patient_det WHERE Id = '{}'".format(patient_id))
    existing_patient_id = cur.fetchone()

    if existing_patient_id:
        prompt = input("WELCOME. ARE YOU HERE FOR A FOLLOW UP ON YOUR PREVIOUS TREATMENT? (YES OR NO):\n ")
        prompt = prompt.lower()
        if prompt == 'yes':
            print(f"Welcome {existing_patient_id[1]}. A doctor would attend to you shortly.")
        elif prompt == 'no':

            new_complaint = input("What is your new complaint:\n ")

            cur.execute("INSERT INTO patient_complaint(Id,complaint) VALUES('{}','{}')".format(patient_id,new_complaint))
            con.commit()

            return 'Your complaint has been stored. Get in the line to see a doctor.'

















