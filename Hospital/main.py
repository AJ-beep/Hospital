from hospital import register_patient, existing_patient

import sqlite3
con = sqlite3.connect('Hospital_project.db')
cur = con.cursor()

patient_on =True

while patient_on:

    print("*****WELCOME*****")

    typical = int(input("Enter 1 if you're new here. Otherwise, enter 2\n "))

    if typical == 1:
        print(register_patient())

    elif typical == 2:
        print(existing_patient())























