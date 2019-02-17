import requests

def upload_record(_id, status):
    requests.post('http://localhost:8000/req/', json={"command":"record", "id":_id, "status":status})
    #requests.post('http://localhost:8000/req/', json={"command":"add", "name":"hi", "time":"5", "status":status})

if  __name__ == "__main__":
    upload_record(15, 1)
