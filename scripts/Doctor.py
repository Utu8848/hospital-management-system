from Person import Person

class Doctor(Person):
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """
        super().__init__(first_name, surname)
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    def first_name(self) :
        return self.get_first_name()

    def set_first_name(self, new_first_name):
        super().set_first_name(new_first_name)

    def surname(self) :
        return self.get_surname()

    def set_surname(self, new_surname):
        super().set_surname(new_surname)

    def full_name(self) :
        full_name = self.get_first_name() + " " + self.get_surname()
        return full_name

    def get_speciality(self) :
        return self.__speciality

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_appointment(self):
        return self.__appointments
    
    def set_appointment(self, appointment):
        self.__appointments.append(appointment)
    
    def get_appointments(self):
        return self.__appointments

    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:>2}'