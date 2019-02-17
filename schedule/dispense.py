"""
run this file: python3 dispense.py "med name"
"""

import sys
import os
from twilio.rest import Client
import time
from save_record.py import upload_record


def send_sms(body, to_num: str = '9786185596'):
    print('dispense.py - send_sms')
    acount_sid = 'AC819c0afb11b689eb481878955d9ada5f'
    auth_token = 'c1bb38dcaaa6ca7fc6a72f17d21ba38c'

    client = Client(acount_sid, auth_token)

    message = client.messages.create(
        to=str(to_num),  # '9786185596',
        from_='+19783103894',
        body=body)


if __name__ == '__main__':
    print('dispense.py - main')
    try:
        # send an sms
        send_sms('Remember to take your {}'.format(sys.argv[1]))
        # Run the C program
        os.system("./stepper.out")
        # wait and 
        time.sleep(5)
        try:
            f = open('meds.dat')
            l = f.readline()
            l = int(l)
            status = l
            f.close()
        except:
            print('dispense.py - error occured in second level of main')
            status = -1
        upload_record(sys.argv[2], status)
    except:
        print('dispense.py - error occurred in top level of main')
        pass
