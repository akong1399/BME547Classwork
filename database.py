class Patient:
    
    def __init__(self, input_name, id_no, age):
        self.name = input_name
        self.id_no = id_no
        self.age = age
        self.tests = []
        # self._x = 3
        
    def __repr__(self):
        return "{}: {}".format(self.id_no, self.name)
    
    def is_adult(self):
        if self.age >= 21:
            return True
        else:
            return False
        

# def class_work():
#     new_patient = Patient("Ann Ables", 120, 36)
#     print(new_patient.id_no)
#     print(new_patient.name)
#     x = Patient("Bob Boyles", 24, 33)
#     print(x.name)
#     print(x)
#     print(x._x)
    

def create_database_entry(patient_name, id_no, age):
    new_patient = Patient(patient_name, id_no, age)
    # new_patient = {"name": patient_name, "id_no": id_no,
    #                "age": age, "tests": []}
    # new_patient = [patient_name, id_no, age, []]
    return new_patient


def print_database(db):
    # for i in range(len(db)):
        # len --> length of database
        # range returns iterable list from 0 up to, but not including the number
        # print("{} - {}".format(i,db[i]))
    locations = ["Room 1", "Room 2", "ER", "Post-Op"]
    # for i, patient in enumerate(db):
    #     print("{} - {} - {}".format(i,patient,locations[i]))
    #     print(patient[0][0]) # getting first letter of each name
    for patient, location in zip(db, locations):
        print("{} - {}".format(patient, location))


def print_over_age(db,age):
    for patient in db:
        if patient[2] > age:
            print(patient[0])
    
    
def get_patient(db, id_no):
    patient = db[id_no]
    return patient
    # for patient in db:
    #     if patient["id_no"] == id_no:
    #         return patient


def main():
    db = {}
    x = create_database_entry("Ann Ables", 120, 30)
    db[x.id_no] = x
    # or db.append(create_database_entry("Ann Ables", 1, 30))
    x = create_database_entry("Bob Boyles", 24, 31)
    db[x.id_no] = x
    x = create_database_entry("Chris Chou", 33, 33)
    db[x.id_no] = x
    x = create_database_entry("David Dinkins", 14, 34)
    db[x.id_no] = x
    print(db)
    
    
    # y = db[1] # second entry in the database
    # y = db[len(db)-1] # last entry in the database
    # y = db[-1] # last entry in the database
    # y = db[1:3]
    
    # bobsname = db[1][0]
    
    # found_patient = get_patient(db, 3)
    # print(found_patient)
    
    # print_database(db)
    
    patient_id_tested = 24
    test_done = ("HDL", 65)
    
    patient = get_patient(db, patient_id_tested)
    patient.tests.append(test_done)
    # patient[3].append(test_done)
    print(db[24].tests)
    
    
    print_database(db)


if __name__ == "__main__":
    main()
