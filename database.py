def create_database_entry(patient_name, id_no, age):
    new_patient = [patient_name, id_no, age, []]
    return new_patient

def print_database(db):
    #for i in range(len(db)):
        # len --> length of database
        # range returns iterable list from 0 up to, but not including the number
        # print("{} - {}".format(i,db[i]))
    locations = ["Room 1", "Room 2", "ER", "Post-Op"]
    # for i, patient in enumerate(db):
    #     print("{} - {} - {}".format(i,patient,locations[i]))
    #     print(patient[0][0]) # getting first letter of each name
    for patient, location in zip(db, locations):
        print("{} - {}".format(patient,location))

def print_over_age(db,age):
    for patient in db:
        if patient[2] > age:
            print(patient[0])
    
def get_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient

def main():
    db = []
    x = create_database_entry("Ann Ables", 120, 30)
    db.append(x)
    # or db.append(create_database_entry("Ann Ables", 1, 30))
    x = create_database_entry("Bob Boyles", 24, 31)
    db.append(x)
    x = create_database_entry("Chris Chou", 33, 33)
    db.append(x)
    x = create_database_entry("David Dinkins", 14, 34)
    db.append(x)
    
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
    patient[3].append(test_done)
    patient[3].append(test_done)
    
    print_database(db)
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    