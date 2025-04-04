from Person import Person

class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, illness, doctor_name, symptoms):
        super().__init__(first_name, surname)
        self.__symptoms = symptoms
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = doctor_name
        self.__illness_type = illness

    def first_name(self):
        return self.get_first_name()
    
    def surname(self):
        return self.get_surname()

    def get_doctor(self):
        return self.__doctor
    
    def full_name(self):
        """full name is first_name and surname"""
        full_name = self.first_name() + " " + self.surname()
        return full_name
    
    def get_age(self):
        return self.__age

    def print_symptoms(self):
        i = 1
        for symptom in self.__symptoms:
            print(f"{i}. {symptom}")
            i += 1

    def link_doctor(self, doctor):
        self.__doctor = doctor

    def get_illness_type(self):
        return self.__illness_type
    
    def get_mobile_num(self):
        return self.__mobile
    
    def get_postcode(self):
        return self.__postcode
    
    def get_symptoms(self):
        return self.__symptoms

    def __str__(self):
        return f'{self.full_name():^30}|{self.get_doctor():^30}|{self.__age:^5}|{self.__mobile:^16}|{self.__postcode:>2}'