from Doctor import Doctor
from Patient import Patient
import matplotlib.pyplot as plt
import numpy as np

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        f = open("admin_username.txt", "r")
        self.__username = f.read()
        f.close()

        f = open("admin_password.txt", "r")
        self.__password = f.read()
        f.close()

        f =  open("admin_address.txt", "r")
        self.__address = f.read()
        f.close()

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:^6}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if username == self.__username and password == self.__password:
            print("You've successfully logged in.")
            return True

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input("Enter first name of the doctor: ")
        surname = input("Enter surname of the doctor: ")
        speciality = input("Enter speciliaty of the doctor: ")
        doctor = Doctor(first_name, surname, speciality)
        return doctor



    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """
        running = True
        while running:
            print("-----Doctor Management-----")

            # menu
            print('Choose the operation:')
            print(' 1 - Register')
            print(' 2 - View')
            print(' 3 - Update')
            print(' 4 - Delete')
            print(' 5 - Go back')
            op = input("Input: ")

            # register
            if op == '1':
                print("-----Register-----")

                # get the doctor details
                print('Enter the doctor\'s details:')
                first_name = input("Enter the first name: ")
                surname = input("Enter the surname: ")
                speciality = input("Enter the speciality: ")
                full_name = first_name + " " + surname
                doctor = Doctor(first_name, surname, speciality)
                # check if the name is already registered
                name_exists = False
                for members in doctors:   
                    if full_name == members.full_name() and speciality == members.get_speciality():
                        print("Name already exists.")
                        name_exists = True

                if name_exists == False:
                    doctors.append(doctor)
                    print("Doctor successfully registered")

            # View
            elif op == '2':
                print("-----List of Doctors-----")
                print("{:^6}|{:^30}|{:>2}".format("ID", "Full name", "Speciality"))
                self.view(doctors)

            # Update
            elif op == '3':

                # menu
                def menu():
                    print('Choose the field to be updated:')
                    print(' 1 First name')
                    print(' 2 Surname')
                    print(' 3 Speciality')
                    print(' 4 Exit')
                    op = input('Input: ') # make the user input lowercase

                    if op == '1':
                        new_first_name = input("Enter the new first name: ")
                        for index, doctor in enumerate(doctors, start = 1):
                            if id == index:
                                doctor.set_first_name(new_first_name)
                                return False

                    elif op == '2':
                        new_second_name = input("Enter the new second name: ")
                        for index, doctor in enumerate(doctors, start = 1):
                            if id == index:
                                doctor.set_surname(new_second_name)
                                return False

                    elif op == '3':
                        new_speciality = input("Enter the new speciality: ")
                        for index, doctor in enumerate(doctors, start = 1):
                            if id == index:
                                doctor.set_speciality(new_speciality)
                                return False

                    elif op == '4':
                        return False
                    
                    else:
                        print("Please enter a valid choice i.e. 1/2/3/4")

                process_end = True
                while process_end:
                    print("-----Update Doctor`s Details-----")
                    print("{:^6}|{:^30}|{:>2}".format("ID", "Full name", "Speciality"))
                    self.view(doctors)
                    try:
                        id = int(input('Enter the ID of the doctor: '))
                        index = id-1
                        doctor_index=self.find_index(index,doctors)
                        if doctor_index!=False:
                            process_end = menu()

                        else:
                            print("Doctor not found")

                    except ValueError: # the entered id could not be changed into an int
                        print('The ID entered is incorrect')
            
            # Delete
            elif op == '4':
                print("-----Delete Doctor-----")
                print("{:^6}|{:^30}|{:>2}".format("ID", "Full name", "Speciality"))
                self.view(doctors)

                doctor_id = int(input('Enter the ID of the doctor to be deleted: '))
                index = doctor_id - 1
                try:
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                        for id, doctor in enumerate(doctors, start = 1):
                            if id == doctor_id:
                                doctors.pop(id-1)
                                print("Doctor deleted")

                    else:
                        print("The ID doesn't exist")

                except ValueError:           
                    print('The id entered is incorrect')

            elif op == '5':
                running = False

            else:
                print("Choose a valid option i.e. 1/2/3/4/5")

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print("{:^6}|{:^30}|{:^30}|{:^5}|{:^16}|{:>2}".format("ID", "Full Name", "Doctor's Full Name", "Age", "Mobile", "Postcode"))
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print("{:^6}|{:^30}|{:^30}|{:^5}|{:^16}|{:>2}".format("ID", "Full Name", "Doctor's Full Name", "Age", "Mobile", "Postcode"))
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures
            else:
                if patients[patient_index].get_doctor() == "Not Assigned":
                    print("-----Doctors Select-----")
                    print('Select the doctor that fits these symptoms:')
                    patients[patient_index].print_symptoms() # print the patient symptoms

                    print('--------------------------------------------------')
                    print("{:^6}|{:^30}|{:>2}".format("ID", "Full name", "Speciality"))
                    self.view(doctors)
                    doctor_index = input('Please enter the doctor ID: ')

                    try:
                        # doctor_index is the patient ID mines one (-1)
                        doctor_index = int(doctor_index) - 1

                        # check if the id is in the list of doctors
                        if self.find_index(doctor_index,doctors)!=False:
                            patients[patient_index].link_doctor(doctors[doctor_index].full_name())
                            with open("patient_data.txt", "r") as f:
                                lines = f.readlines()
                                for line in lines:
                                    if patients[patient_index].get_mobile_num() in line:
                                        index = lines.index(line)
                                        stripped_line = line.strip()
                                        list_form = stripped_line.rsplit(', ')
                                        list_form[6] = doctors[doctor_index].full_name()
                                        ready_string = ""
                                        for item in list_form:
                                            if item == list_form[0]:
                                                ready_string += f"{item}"
                                            else:
                                                ready_string += f", {item}"
                                        if index != len(lines)-1:
                                            ready_string += "\n"
                                        
                                        lines.pop(index)
                                        lines.insert(index, ready_string)
                                        with open("patient_data.txt", "w") as f:
                                            f.writelines(lines)
                                        print('The patient is now assigned to the doctor.')
                                        break

                        # if the id is not in the list of doctors
                        else:
                            print('The id entered was not found.')

                    except ValueError: # the entered id could not be changed into an in
                        print('The id entered is incorrect')

                else:
                    print("The patient is already assigned to a doctor.")

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patients-----")
        print("{:^6}|{:^30}|{:^30}|{:^5}|{:^16}|{:>2}".format("ID", "Full Name", "Doctor's Full Name", "Age", "Mobile", "Postcode"))
        self.view(patients)
        choice1 = input("Do you want to discharge a patient(Y/N): ")
        if choice1.lower() == 'y':
            discharge_running = True
            while discharge_running:
                try:
                    patient_index = int(input('Please enter the patient ID: '))
                    if patient_index in range(1, len(patients)+1):
                        choice2 = input(f"Do you want to discharge {patients[patient_index-1].full_name()} (Y/N): ")
                        if choice2.lower() == 'y':
                            discharge_patients.append(patients[patient_index-1])
                            patients.pop(patient_index-1)
                            print("Patient successfully discharged")
                            discharge_running = False

                        elif choice2.lower() == 'n':
                            print("Discharging process cancelled")
                            discharge_running = False

                        else:
                            print("Invalid choice, choose (Y/N)")
                            
                    else:
                        print("The ID doesn't exist.")

                except ValueError:
                    print("Sorry, the ID is invalid.")

        elif choice1.lower() == 'n':
            print("Discharging process cancelled")

        else:
            print("Please choose valid option i.e. (Y/N).")

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        if len(discharged_patients) == 0:
            print("{:^30}".format("No patient disharged yet"))
        else:
            print("{:^6}|{:^30}|{:^30}|{:^5}|{:^16}|{:>2}".format("ID", "Full Name", "Doctor's Full Name", "Age", "Mobile", "Postcode"))
            for index, discharged_patient in enumerate(discharged_patients, start=1):
                print("{:^6}|".format(index) + discharged_patient.__str__())

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        print(' 4 Go back')
        running = True
        while running:
            op = int(input('Input: '))

            if op == 1:
                f = open("admin_username.txt", "w")
                f.write(input("Enter a new username: "))
                f.close()
                print("Username successfully changed!")

            elif op == 2:
                new_password = input("Enter a new password: ")
                # validate the password
                if new_password == input('Enter the new password again: '):
                    f = open("admin_password.txt", "w")
                    f.write(new_password)
                    f.close()
                    print("Password successfully changed!")
                else:
                    print("You have to enter the same password both of the times.")

            elif op == 3:
                f = open("admin_address.txt", "w")
                f.write(input("Enter a new address: "))
                print("Address changed successfully")
                f.close()

            elif op == 4:
                running = False

            else:
                print("Please select a valid choice i.e. 1/2/3")

    def load_patient_data_from_file(self):
        with open("patient_data.txt", "r") as f:
            all_patient_data = []
            i = 0
            line_list = f.readlines()
            while i < len(line_list):
                patient_detail = line_list[i].strip().rsplit(', ')
                symptom_list = patient_detail[7:]
                del patient_detail[7:]
                patient_detail.append(symptom_list)
                a,b,c,d,e,f,g,h = patient_detail
                c = int(c)
                all_patient_data.append(Patient(a,b,c,d,e,f,g,h))
                i += 1

            return all_patient_data
        
    def patient_same_fam(self):
        edited_list = []
        patients = self.load_patient_data_from_file()
        for patient in patients:
            for index in range(0, len(patients)):
                if patient.get_surname() == patients[index].get_surname():
                    if patient.full_name() not in edited_list: 
                        edited_list.append(patient.full_name())
                    if patients[index].full_name() not in edited_list:
                        edited_list.append(patients[index].full_name())
                
        print("-----Family Grouping of Patients-----")
        i = 1
        for members in edited_list:
            print(f"{i}. {members}")
            i += 1

    def load_new_patient_data_to_file(self, patients):
        print("-----Add patient-----")
        first_name = input("Enter the first name of the patient: ")
        surname = input("Enter the surname of the patient: ")
        age = input("Enter the age of the patient: ")
        mobile_num = input("Enter the mobile number of the patient: ")
        postcode = input("Enter the postcode of the patient: ")
        illness = input("Enter the illness_type of the patient: ")
        doctor_name = "Not Assigned"
        symptoms = input("Enter the symptoms seen in the patient(Note: every symptom must be separated by ', '): ")
        symptoms_list = symptoms.rsplit(', ')
        final_info = f'\n{first_name}, {surname}, {age}, {mobile_num}, {postcode}, {illness}, {doctor_name}, {symptoms}'
        with open("patient_data.txt", "r") as f:
            line_list = f.readlines()
            dup_line_list = []
            for lines in line_list:
                lines = lines.strip()
                dup_line_list.append(lines)
        for patient in patients:
            if patient.full_name() == first_name + " " + surname:
                a = 1
            else:
                a = 0

            if patient.get_age() == int(age):
                b = 1
            else:
                b = 0

            if patient.get_mobile_num() == mobile_num:
                c = 1
            else:
                c = 0

            if patient.get_postcode() == postcode:
                d = 1
            else:
                d = 0

            if patient.get_illness_type() == illness:
                e = 1
            else:
                e = 0
            
            if patient.get_symptoms() == symptoms_list:
                f = 1
            else:
                f = 0

            final = a+b+c+d+e+f

            if final == 6:
                break

        if final < 6:
            if final_info.strip() not in dup_line_list:
                with open("patient_data.txt", "r+") as f:
                    f.read()
                    f.write(final_info)
                print("The patient data was successfully stored.")
                patients.append(Patient(first_name,surname,int(age),mobile_num,postcode,illness,doctor_name,symptoms_list))
            else:
                print("The patient data was successfully stored.")
        else:
            print("Sorry the patient with the exact same data already exists in the system.")

    def patient_relocation(self, patients, doctors):
        print("-----Relocation of patients-----")
        try:
            print("{:^6}|{:^30}|{:^30}|{:^5}|{:^16}|{:>2}".format("ID", "Full Name", "Doctor's Full Name", "Age", "Mobile", "Postcode"))
            self.view(patients)
            id = int(input('Enter the patient ID: '))
            if id in range(1, len(patients)+1):
                index = id-1
                if patients[index].get_doctor() != 'Not Assigned':
                    confirmation1 = input("Are you sure to proceed relocation (Y/N): ")
                    if confirmation1.lower() == 'y':
                        print("-----List of Doctors-----")
                        print("{:^6}|{:^30}|{:>2}".format("ID", "Full name", "Speciality"))
                        self.view(doctors)
                        new_doctor_id = int(input("Enter the ID of the doctor to whom the patient is to be relocated: "))
                        if new_doctor_id in range(1,len(doctors)+1):
                            if patients[index].get_doctor() != doctors[new_doctor_id-1].full_name():
                                confirmation2 = input(f"Are you sure to relocate {patients[index].full_name()} to Dr. {doctors[new_doctor_id-1].full_name()} (Y/N): ")
                                if confirmation2.lower() == 'y':
                                    patients[index].link_doctor(doctors[new_doctor_id-1].full_name())
                                    with open("patient_data.txt", "r") as f:
                                        lines = f.readlines()
                                    for line in lines:
                                        if patients[index].get_mobile_num() in line:
                                            index = lines.index(line)
                                            stripped_line = line.strip()
                                            list_form = stripped_line.rsplit(', ')
                                            list_form[6] = doctors[new_doctor_id-1].full_name()
                                            ready_string = ""
                                            for item in list_form:
                                                if item == list_form[0]:
                                                    ready_string += f"{item}"
                                                else:
                                                    ready_string += f", {item}"
                                            if index != len(lines)-1:
                                                ready_string += "\n"
                                            
                                            lines.pop(index)
                                            lines.insert(index, ready_string)
                                            with open("patient_data.txt", "w") as f:
                                                f.writelines(lines)
                                    print(f"{patients[index].full_name()} is successfully relocated to Dr. {doctors[new_doctor_id-1].full_name()}.")

                                elif confirmation2.lower() == 'n':
                                    print("Relocation process cancelled")
                                else:

                                    print("Please choose valid option i.e. (Y/N)")

                            else:
                                print("The patient is already assigned to the doctor, please choose another doctor.")

                        else:
                            print("Sorry, the doctor ID you've entered doesn't exist.")

                    elif confirmation1.lower() == 'n':
                        print("Relocation process cancelled")

                    else:
                        print("Please choose valid option i.e. (Y/N)")

                else:
                    print("Patient needs to be assigned to a doctor for relocation.")

            else:
                print("Sorry, the patient ID you've entered doesn't exist.")

        except ValueError:
            print("The ID is invalid.")

    def update_patient_data(self, patients):
        print("-----Update Patient Data-----")
        print("{:^6}|{:^30}|{:^30}|{:^5}|{:^16}|{:>2}".format("ID", "Full Name", "Doctor's Full Name", "Age", "Mobile", "Postcode"))
        self.view(patients)
        try:
            patient_id = int(input("Enter the ID of the patient whose data is to be updated: "))
            patient_index = patient_id-1
            if patient_index in range(0, len(patients)):
                patient_contact = patients[patient_index].get_mobile_num()
                running = True
                while running:
                    with open("patient_data.txt", "r") as f:
                        lines = f.readlines()
                    for line in lines:
                        if patient_contact in line:
                            print("1. First_name")
                            print("2. Surname")
                            print("3. Age")
                            print("4. Mobile number (NOTE: Once changed user will be redirected to main menu)")
                            print("5. Postcode")
                            print("6. Illness type")
                            print("7. Symptoms")
                            print("8. Go back")
                            choice = input("Choose the info to modify: ")
                            index = lines.index(line)
                            if choice == '1':
                                first_name = input("Enter the new first name: ")
                                stripped_line = line.strip()
                                list_form = stripped_line.rsplit(', ')
                                list_form[0] = first_name
                                ready_string = ""
                                for item in list_form:
                                    if item == list_form[0]:
                                        ready_string += f"{item}"
                                    else:
                                        ready_string += f", {item}"
                                if index != len(lines)-1:
                                    ready_string += "\n"
                                
                                lines.pop(index)
                                lines.insert(index, ready_string)
                                with open("patient_data.txt", "w") as f:
                                    f.writelines(lines)
                                print("First name successfully updated!")
                                break

                            elif choice == '2':
                                surname = input("Enter the new surname: ")
                                stripped_line = line.strip()
                                list_form = stripped_line.rsplit(', ')
                                list_form[1] = surname
                                ready_string = ""
                                for item in list_form:
                                    if item == list_form[0]:
                                        ready_string += f"{item}"
                                    else:
                                        ready_string += f", {item}"
                                if index != len(lines)-1:
                                    ready_string += "\n"
                                
                                lines.pop(index)
                                lines.insert(index, ready_string)
                                with open("patient_data.txt", "w") as f:
                                    f.writelines(lines)
                                print("Surname successfully updated!")
                                break
                        
                            elif choice == '3':
                                age = input("Enter the new age: ")
                                stripped_line = line.strip()
                                list_form = stripped_line.rsplit(', ')
                                list_form[2] = age
                                ready_string = ""
                                for item in list_form:
                                    if item == list_form[0]:
                                        ready_string += f"{item}"
                                    else:
                                        ready_string += f", {item}"
                                if index != len(lines)-1:
                                    ready_string += "\n"
                                
                                lines.pop(index)
                                lines.insert(index, ready_string)
                                with open("patient_data.txt", "w") as f:
                                    f.writelines(lines)
                                print("Age successfully updated!")
                                break

                            elif choice == '4':
                                mobile_num = input("Enter the new mobile number: ")
                                stripped_line = line.strip()
                                list_form = stripped_line.rsplit(', ')
                                list_form[3] = mobile_num
                                ready_string = ""
                                for item in list_form:
                                    if item == list_form[0]:
                                        ready_string += f"{item}"
                                    else:
                                        ready_string += f", {item}"
                                if index != len(lines)-1:
                                    ready_string += "\n"
                                
                                lines.pop(index)
                                lines.insert(index, ready_string)
                                with open("patient_data.txt", "w") as f:
                                    f.writelines(lines)
                                print("Mobile number successfully updated!")
                                running = False
                                break

                            elif choice == '5':
                                postcode = input("Enter the new postcode: ")
                                stripped_line = line.strip()
                                list_form = stripped_line.rsplit(', ')
                                list_form[4] = postcode
                                ready_string = ""
                                for item in list_form:
                                    if item == list_form[0]:
                                        ready_string += f"{item}"
                                    else:
                                        ready_string += f", {item}"
                                if index != len(lines)-1:
                                    ready_string += "\n"
                                
                                lines.pop(index)
                                lines.insert(index, ready_string)
                                with open("patient_data.txt", "w") as f:
                                    f.writelines(lines)
                                print("Postcode successfully updated!")
                                break

                            elif choice == '6':
                                illness = input("Enter the new illness type: ")
                                stripped_line = line.strip()
                                list_form = stripped_line.rsplit(', ')
                                list_form[5] = illness
                                ready_string = ""
                                for item in list_form:
                                    if item == list_form[0]:
                                        ready_string += f"{item}"
                                    else:
                                        ready_string += f", {item}"
                                if index != len(lines)-1:
                                    ready_string += "\n"
                                
                                lines.pop(index)
                                lines.insert(index, ready_string)
                                with open("patient_data.txt", "w") as f:
                                    f.writelines(lines)
                                print("Illness type successfully updated!")
                                break

                            elif choice == '7':
                                symptoms = input("Enter the new symptoms(Note: Each symptom should be separated by ', '): ")
                                stripped_line = line.strip()
                                list_form = stripped_line.rsplit(', ')
                                symptoms_list = symptoms.rsplit(', ')
                                del list_form[7:]
                                for symptom in symptoms_list:
                                    list_form.append(symptom)
                                ready_string = ""
                                for item in list_form:
                                    if item == list_form[0]:
                                        ready_string += f"{item}"
                                    else:
                                        ready_string += f", {item}"
                                if index != len(lines)-1:
                                    ready_string += "\n"
                                
                                lines.pop(index)
                                lines.insert(index, ready_string)
                                with open("patient_data.txt", "w") as f:
                                    f.writelines(lines)
                                print("Symptoms successfully updated!")
                                break

                            elif choice == '8':
                                running = False

                            else:
                                print("Please choose option that exists.")

            else:
                print("The patient ID doesn't exist.")
        
        except ValueError:
            print("The ID entered is invalid.")

    def set_appointment(self, doctors):
        print("-----Set Appointment-----")
        patient_name = input("Enter the name of the patient: ")
        print("-----List of Doctors-----")
        print("{:^6}|{:^30}|{:>2}".format("ID", "Full name", "Speciality"))
        self.view(doctors)
        try:
            doctor_for_apmnt = int(input("Enter the ID of the doctor with whom the appointment is to be set: "))
            if doctor_for_apmnt in range(1, len(doctors) + 1):
                doctor_name = doctors[doctor_for_apmnt-1].full_name()
                for doctor in doctors:
                    if doctor.full_name() == doctor_name:
                        month = input("Enter a month of appointment: ")
                        day = input("Enter a day of appointment: ")
                        a = 1
                        b = 2
                        meridian = "None"
                        for i in range(9, 17):
                            if i < 12:
                                meridian = 'AM'
                            else:
                                meridian = 'PM'

                            print(f"{a}. {i}:00 {meridian}")
                            print(f"{b}. {i}:30 {meridian}")
                            a += 2
                            b += 2
                        time = input("Choose a time for appointment: ")
                        if time == '1':
                            appointment_time = '9:00 AM'
                        if time == '2':
                            appointment_time = '9:30 AM'
                        if time == '3':
                            appointment_time = '10:00 AM'
                        if time == '4':
                            appointment_time = '10:30 AM'
                        if time == '5':
                            appointment_time = '11:00 AM'
                        if time == '6':
                            appointment_time = '11:30 AM'
                        if time == '7':
                            appointment_time = '12:00 PM'
                        if time == '8':
                            appointment_time = '12:30 PM'
                        if time == '9':
                            appointment_time = '13:00 PM'
                        if time == '10':
                            appointment_time = '13:30 PM'
                        if time == '11':
                            appointment_time = '14:00 PM'
                        if time == '12':
                            appointment_time = '14:30 PM'
                        if time == '13':
                            appointment_time = '15:00 PM'
                        if time == '14':
                            appointment_time = '15:30 PM'
                        if time == '15':
                            appointment_time = '16:00 PM'
                        if time == '16':
                            appointment_time = '16:30 PM'
                        finalized_time = f'{month} {day} {appointment_time}'
                        if finalized_time not in doctor.get_appointment():
                            doctor.set_appointment(finalized_time)
                            print(f"Appointment of {patient_name} with Dr. {doctor.full_name()} is successfully set on {month} {day} at {appointment_time}.")
                            break

                        else:
                            print("The time has already been booked.")
                            choice = input("Do you want to continue booking the appointment? (Y/N): ")
                            if choice.lower() == 'y':
                                self.set_appointment(doctors)
                            elif choice.lower() == 'n':
                                break

            else:
                print("The patient ID doesn't exist.")

        except ValueError:
            print("The ID you've entered is invalid.")

    def total_num_of_doctors(self, doctors):
        print(f"Total number of doctors: {len(doctors)}")

    def patients_per_doctor(self, patients, doctors):
        for doctor in doctors:
            total = 0
            for patient in patients:
                if patient.get_doctor() == doctor.full_name():
                    total += 1
            print(f"Total number of patients of Dr. {doctor.full_name()}: {total}")

    def num_of_appointments(self, doctors):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for doctor in doctors:
            print(f"\n\n-----Monthly Appointment Report of Dr. {doctor.full_name()}-----\n")
            for month in months:
                total = 0
                for appointment in doctor.get_appointment():
                    if month in appointment:
                        total += 1
                print(f"Total number of appointments in {month}: {total}")

    def illness_type(self, patients):
        illness_types = ['Respiratory', 'Cardiovascular', 'Neurological', 'Gastrointestinal', 'Endocrine', 'Musculoskeletal', 'Dermatological', 'Dental', 'Common']
        for illness in illness_types:
            total = 0
            for patient in patients:
                if patient.get_illness_type() == illness:
                    total += 1
            print(f"Total number of patient with {illness} illness: {total}")

    def management_report(self, patients, doctors):
        print("-----Management Report-----")
        print("1. Total number of doctors in the system")
        print("2. Total number of patients per doctor")
        print("3. Total number of appointments per month per doctor")
        print("4. Total number of patients based on the illness type")
        choice = input("Choose an option i.e.(1/2/3/4): ")
        if choice == '1':
            self.total_num_of_doctors(doctors)
        elif choice == '2':
            self.patients_per_doctor(patients, doctors)
        elif choice == '3':
            self.num_of_appointments(doctors)
        elif choice == '4':
            self.illness_type(patients)
        else:
            print("Please choose a valid option i.e. (1/2/3)")

    def monthly_report(self, month, doctors):
        doctor_names = []
        data_for_report = []
        for doctor in doctors:
            num_of_appointments = 0
            for appointment_date in doctor.get_appointments():
                if month in appointment_date:
                    num_of_appointments += 1
            if num_of_appointments != 0:
                data_for_report.append(num_of_appointments)
                doctor_names.append(doctor.full_name())

        final_data = [data_for_report, doctor_names]
        return final_data

    def patient_per_doctor_data(self, patients, doctors):
        data = []
        doctor_names = []
        for doctor in doctors:
            patient_num = 0
            for patient in patients:
                if patient.get_doctor() == doctor.full_name():
                    patient_num += 1
            if patient_num != 0:
                data.append(patient_num)
                doctor_names.append(doctor.full_name())

        final_data = [data, doctor_names]
        return final_data

    def illness_report(self, patients):
        data = []
        illness_types_data = []
        illness_types = ['Respiratory', 'Cardiovascular', 'Neurological', 'Gastrointestinal', 'Endocrine', 'Musculoskeletal', 'Dermatological', 'Dental', 'Common']
        for illness in illness_types:
            total = 0
            for patient in patients:
                if patient.get_illness_type() == illness:
                    total += 1
            if total != 0:
                data.append(total)
                illness_types_data.append(illness)
        
        final_data = [data, illness_types_data]
        return final_data

    def pie_chart_num_patients(self, patients, doctors):
        plt.title(f"Report of Number of Patients Per Doctor", fontweight='bold', fontsize=14)
        num_of_patients = np.array(self.patient_per_doctor_data(patients, doctors)[0])
        doctor_names = self.patient_per_doctor_data(patients, doctors)[1]
        plt.text(0, 1.07, f"Total number of patients: {sum(num_of_patients)}", ha='right', va='bottom', fontsize=12, fontstyle='italic')
        def autopct_format(pct, all_values):
            absolute = int(round(pct/100. * sum(all_values)))  # Calculate actual value
            return f"{pct:.1f}%\n({absolute})"  # Format both percentage and actual value
        
        plt.pie(num_of_patients, labels = doctor_names, startangle = 90, autopct=lambda pct: autopct_format(pct, num_of_patients))
        plt.show()

    def pie_chart_illness(self, patients):
        plt.title(f"Report of Number of Patients Per Illness Type", fontweight='bold', fontsize=14)
        num_of_patients = np.array(self.illness_report(patients)[0])
        illness_type = self.illness_report(patients)[1]
        plt.text(0, 1.07, f"Total number of patients: {sum(num_of_patients)}", ha='right', va='bottom', fontsize=12, fontstyle='italic')
        def autopct_format(pct, all_values):
            absolute = int(round(pct/100. * sum(all_values)))  # Calculate actual value
            return f"{pct:.1f}%\n({absolute})"  # Format both percentage and actual value
        
        plt.pie(num_of_patients, labels = illness_type, startangle = 90, autopct=lambda pct: autopct_format(pct, num_of_patients))
        plt.show()
    
    def pie_chart(self, month, doctors):
        plt.title(f"Report of Appointments Per Doctor for {month}", fontweight='bold', fontsize=14)
        appointments = np.array(self.monthly_report(month, doctors)[0])
        doctor_names = self.monthly_report(month, doctors)[1]
        plt.text(0, 1.07, f"Total number of appointments: {sum(appointments)}", ha='right', va='bottom', fontsize=12, fontstyle='italic')
        def autopct_format(pct, all_values):
            absolute = int(round(pct/100. * sum(all_values)))  # Calculate actual value
            return f"{pct:.1f}%\n({absolute})"  # Format both percentage and actual value
        
        plt.pie(appointments, labels = doctor_names, startangle = 90, autopct=lambda pct: autopct_format(pct, appointments))
        plt.show()

    def report_diagram(self, patients, doctors):
        running = True
        while running:
            print("1.  Report of number of patients per doctor")
            print("2.  Report of number of appointments per month per doctor")
            print("3.  Report of number of patients per illness")
            print("4.  Go back")
            try:
                option = int(input("Please choose an option i.e.(1/2/3/4): "))
                if option in range(1,5):

                    if option == 1:
                        self.pie_chart_num_patients(patients, doctors)

                    elif option == 2:
                        print("1.  January Report")
                        print("2.  February Report")
                        print("3.  March Report")
                        print("4.  April Report")
                        print("5.  May Report")
                        print("6.  June Report")
                        print("7.  July Report")
                        print("8.  August Report")
                        print("9.  September Report")
                        print("10. October Report")
                        print("11. November Report")
                        print("12. December Report")
                        print("13. Go back")

                        try:
                            choice = int(input("Choose a month to show the report of that month: "))
                            if choice in range(1,14):
                                if choice == 1:
                                    self.pie_chart("Jan", doctors)
                                elif choice == 2:
                                    self.pie_chart("Feb", doctors)
                                elif choice == 3:
                                    self.pie_chart("Mar", doctors)
                                elif choice == 4:
                                    self.pie_chart("Apr", doctors)
                                elif choice == 5:
                                    self.pie_chart("May", doctors)
                                elif choice == 6:
                                    self.pie_chart("Jun", doctors)
                                elif choice == 7:
                                    self.pie_chart("Jul", doctors)
                                elif choice == 8:
                                    self.pie_chart("Aug", doctors)
                                elif choice == 9:
                                    self.pie_chart("Sep", doctors)
                                elif choice == 10:
                                    self.pie_chart("Oct", doctors)
                                elif choice == 11:
                                    self.pie_chart("Nov", doctors)
                                elif choice == 12:
                                    self.pie_chart("Dec", doctors)
                                elif choice == 13:
                                    pass
                                
                            else:
                                print("The option you entered doesn't exist")


                        except ValueError:
                            print("Please enter a valid option")

                    elif option == 3:
                        self.pie_chart_illness(patients)

                    elif option == 4:
                        running = False

                else:
                    print("Please choose option that exists i.e.(1/2/3/4)")

            except ValueError:
                print("Please choose a valid option i.e.(1/2/3/4)")

    def load_patient_data_to_txt(self, patients):
        all_data = []
        for patient in patients:
            data = f"{patient.first_name()}, {patient.surname()}, {patient.get_age()}, {patient.get_mobile_num()}, {patient.get_postcode()}, {patient.get_illness_type()}, {patient.get_doctor()}"
            for symptom in patient.get_symptoms():
                data += f", {symptom}"
            if patient.get_mobile_num() != patients[-1].get_mobile_num():
                data += "\n"
            all_data.append(data)
        with open("patient_data.txt", "w") as f:
            f.writelines(all_data)