import requests

server_name = "http://vcm-21170.vm.duke.edu:5000/"

request_json = {"name": "Alissa Kong", "net_id": "ak492", "e-mail": "alissa.kong@duke.edu"}
r = requests.post(server_name + "student", json=request_json)
