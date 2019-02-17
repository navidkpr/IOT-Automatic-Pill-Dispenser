import requests

def upload_record(_id, status, phone_num):
    requests.post('http://localhost:8000/req/', json={"command":"record", "id":_id, "status":status, "phone": phone_num})

#requests.post('http://localhost:8000/req/', json={"command":"remove", "name":"advil", "user_id":"1"})
#requests.post('http://localhost:8000/req/', json={"command":"add", "name":"advil", "time":"-1"})
#requests.post('http://localhost:8000/req/', json={"command":"give_record", "delete":"1"})
if  __name__ == "__main__":
    #upload_record(93, 0)
    pass
