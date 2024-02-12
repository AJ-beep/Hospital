
import sqlite3
from datetime import datetime
con = sqlite3.connect('Hospital_project.db')
cur = con.cursor()

def doctor():
    doctor_todo =True
    password = input("What is the passkey for doctors: \n")
    password = password.lower()
    if password == 'doctor':
        while doctor_todo:
            todo = int(input('What do you want to do....\n 1.Check patient\n 2.Logout'))
            if todo == 1:
                department = input("You're from which department:\n ")
                doctor_name = input("Your name:\n ")
                patient = input("Enter the patient Id:\n ")
                patient = patient.lower()
                cur.execute("SELECT * FROM patient_det WHERE Id = '{}'".format(patient))
                patient_detail = cur.fetchone()

                cur.execute("SELECT * FROM patient_complaint WHERE Id = '{}'".format(patient))
                patient_complaint = cur.fetchall()

                if patient_detail and len(patient_complaint) == 1:

                    patient_details = f' Name:{patient_detail[1]}\n Age:{patient_detail[2]}\n Gender:{patient_detail[3]}\n Weight:{patient_detail[4]}\n Complaint:{patient_complaint[0][1]}'
                    print(patient_details)
                    date = datetime.today()
                    try:
                        cur.execute("CREATE TABLE doctor_assessment(department, doctor, patient_id, diagnosis, prescription, date)")

                        con.commit()
                    except:
                        pass
                    diagnosis = input("What is your diagnosis: \n")
                    prescription = input("What will you prescribe: \n")

                    cur.execute("INSERT INTO doctor_assessment(department, doctor, patient_id, diagnosis, prescription, date) VALUES('{}','{}','{}','{}','{}','{}')".format(department,doctor_name,patient,diagnosis,prescription,date))
                    con.commit()


                elif patient_detail and len((patient_complaint)) > 1:

                    date = datetime.today()

                    cur.execute("SELECT * FROM doctor_assessment WHERE patient_id='{}'".format(patient))
                    detail_from_previous_diagnosis = cur.fetchall()
                    patient_details = f'Name:{patient_detail[1]}\n Age:{patient_detail[2]}\n Gender:{patient_detail[3]}\n Weight:{patient_detail[4]}\n Previously managed for:{detail_from_previous_diagnosis[-1][3]}\n Previous prescription:{detail_from_previous_diagnosis[-1][4]}'
                    print(patient_details)

                    diagnosis = input("What is your diagnosis: \n")
                    diagnosis = diagnosis or 'N/A'

                    prescription = input("What will you prescribe: \n")
                    prescription = prescription or 'N/A'

                    cur.execute("INSERT INTO doctor_assessment(department, doctor, patient_id, diagnosis, prescription, date) VALUES('{}','{}','{}','{}','{}','{}')".format(department, doctor_name, patient, diagnosis, prescription, date))
                    con.commit()

                else:
                    print('No record found for the patient!')

            elif todo == 2:
                doctor_todo = False
    else:
        print('Incorrect password')
        doctor()



