import requests

if __name__ == '__main__':
    rest_endpoint = 'http://localhost:8000/req/'
    print('update_docs_req.py - sending post to {} for give_record'.format(rest_endpoint))
    requests.post(rest_endpoint, json={"command": "give_record", "delete": "1"})
