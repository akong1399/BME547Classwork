from flask import Flask, request, jsonify


app = Flask(__name__)
db = []


@app.route("/", methods=["GET"])
def status():
    return "Server is on"


@app.route("/new_patient", methods=["POST"])
def new_patient():
    in_data = request.get_json()
    error_string, status_code = validate_new_patient_input(in_data)
    if error_string is not True:
        return error_string, status_code
    new_patient = add_database_entry(in_data["name"], in_data["id"], in_data["blood_type"])
    return "Added patient {}".format(new_patient)


@app.route("/add_test", methods=["POST"])
def add_test():
    in_data = request.get_json()
    error_string, status_code = validate_add_test(in_data)
    if error_string is not True:
        return error_string, status_code
    patient_id_tested = in_data["id"]
    test_done = [in_data["test_name"], in_data["test_result"]]
    patient = get_patient(db, patient_id_tested)
    patient["tests"].append(test_done)
    return "Added test to patient {}".format(patient)


def get_patient(db, id_no):
    patient = db[id_no]
    return patient


def validate_add_test(in_data):
    if type(in_data) is not dict:
        return "The input was not a dictionary.", 400
    expected_keys = {"id": int, "test_name": str, "test_result": int}
    for key in expected_keys:
        if key not in in_data:
            return "The key {} is missing from input".format(key), 400
        if type(in_data[key] is not expected_keys[key]):
            return "The key {} has the wrong data type".format(key), 400
    return True, 200


def validate_new_patient_input(in_data):
    if type(in_data) is not dict:
        return "The input was not a dictionary.", 400
    expected_keys = {"name": str, "id": int, "blood_type": str}
    for key in expected_keys:
        if key not in in_data:
            return "The key {} is missing from input".format(key), 400
        if type(in_data[key] is not expected_keys[key]):
            return "The key {} has the wrong data type".format(key), 400
    # expected_types = {"name": str, "id": int, "blood_type": str}
    # for key in expected_types:
    #     if type(in_data[key] is expected_types[key]):
    return True, 200


def add_database_entry(patient_name, id_no, blood_type):
    new_patient = {"name": patient_name,
                   "id": id_no,
                   "blood_type": blood_type,
                   "tests": []}
    db.append(new_patient)
    return new_patient


if __name__ == '__main__':
    app.run()
