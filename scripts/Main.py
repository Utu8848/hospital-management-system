# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin() # username is 'admin', password is '123', address is 'B1 1AB' set through file handling for updating it in future
    doctors = [Doctor('John','Smith', 'Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient("Sara", "Smith", 20, "07012345678", "B1 234", "Neurological", "Not Assigned", ["Anxiety", "Depression"]), Patient("Mike", "Jones", 37, "07555551234", "L2 2AB", "Gastrointestinal", "Not Assigned", ["Nausea", "Vomitting"]), Patient("David", "Smith", 15, "07123456789", "C1 ABC", "Cardiovascular", "Not Assigned", ["Chest Pain", "High BP"])]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    running = True
    while running:
        if admin.login():
            running_1 = True # allow the program to run
            running = False
            running_3 = True
        else:
            print('Incorrect username or password.')

    while running_3:
        print("1. Continue with the previous patient data (NOTE: Choose only if the program is already run previously)")
        print("2. Reset the patient data (*Mandatory when running the program for first time, to create a txt file and load patient data into the file)")
        try:
            choice = int(input("Choose an option (1/2): "))
            if choice == 1:
                try:
                    patients = admin.load_patient_data_from_file()
                    running_2 = True
                    running = False
                    running_3 = False
                except:
                    print("Read NOTE before choosing the option!!!")

            elif choice == 2:
                admin.load_patient_data_to_txt(patients)
                running_2 = True
                running = False
                running_3 = False
            else:
                print("Please choose an option that exists i.e.(1/2).")

        except ValueError:
            print("Please choose a valid option.")

    final_running = running_1 and running_2
    while final_running:
        # print the menu
        print('Choose the operation:')
        print(' 1-  Register/view/update/delete doctor')
        print(' 2-  Discharge patients')
        print(' 3-  View discharged patient')
        print(' 4-  Assign doctor to a patient')
        print(' 5-  Update admin details')
        print(' 6-  Family grouping of patients')
        print(' 7-  Add patient') # Loading of new patients data to txt file "patient_data.txt" where all the data of patients are stored
        print(' 8-  Update patient data') # Edits patient data not just for instance
        print(' 9-  Relocate patient')
        print(' 10- Set appointment')
        print(' 11- Management report')
        print(' 12- Diagrammatic management report')
        print(' 13- Exit')

        # get the option
        op = input('Option: ')

        if op == '1':
            admin.doctor_management(doctors)

        elif op == '2':
            admin.discharge(patients, discharged_patients)

        elif op == '3':
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif op == '6':
            admin.patient_same_fam()

        elif op == '7':
            admin.load_new_patient_data_to_file(patients)

        elif op == '8':
            patients = admin.load_patient_data_from_file()
            admin.update_patient_data(patients)

        elif op == '9':
            patients = admin.load_patient_data_from_file()
            admin.patient_relocation(patients, doctors)

        elif op == '10':
            admin.set_appointment(doctors)

        elif op == '11':
            patients = admin.load_patient_data_from_file()
            admin.management_report(patients, doctors)

        elif op == '12':
            patients = admin.load_patient_data_from_file()
            admin.report_diagram(patients, doctors)

        elif op == '13':
            print("-----Goodbye!-----")
            final_running = False

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()