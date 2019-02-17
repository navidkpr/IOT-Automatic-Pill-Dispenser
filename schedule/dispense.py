"""
run this file: python3 dispense.py "name" "new_location"
"""

import sys
import os
from twilio.rest import Client
import time
from save_record import upload_record


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
    print('dispense.py arguments - {}'.format(sys.argv))
    try:
        # send an sms
        send_sms('Remember to take your {}'.format(sys.argv[1]))
        # Run the C program
        stepper_cmd = '/home/pi/stepper {}'.format(sys.argv[2])
        print('dispense.py - {}'.format(stepper_cmd))
        os.system(stepper_cmd)
        # wait and 
        time.sleep(5)
        try:
            f = open('/home/pi/meds.dat')
            l = f.readline()
            l = l.split(',')
            status = int(l[0])
            last_pos = int(l[1])
            f.close()
        except Exception as e:
            print('dispense.py - error occured in second level of main')
            print(str(e))
            status = -1
            last_pos = -1
        upload_record(status, last_pos)
    except Exception as e:
        print('dispense.py - error occurred in top level of main')
        print(str(e))
        pass
