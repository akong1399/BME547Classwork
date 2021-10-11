import requests

server_name = "http://vcm-7631.vm.duke.edu:5002/"

r = requests.get(server_name + "get_patients/ak492")
print(r.json())


r1 = requests.get(server_name + "get_blood_type/F4")
print(r1.text)

r2 = requests.get(server_name + "get_blood_type/M8")
print(r2.text)

request_json = {"Name": "ak492", "Match": "Yes"}
r3 = requests.post(server_name + "match_check", json=request_json)
print(r3.text)
