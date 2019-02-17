"""
run this file: python3 dispense.py "name" "new_location" "to_number"
"""

import sys
import os
from twilio.rest import Client
import time
from save_record import upload_record
from datetime import datetime as dt


def send_sms(body, to_num: str = '9786185596'):
    log('dispense.py - send_sms')
    acount_sid = 'AC819c0afb11b689eb481878955d9ada5f'
    auth_token = 'c1bb38dcaaa6ca7fc6a72f17d21ba38c'

    client = Client(acount_sid, auth_token)

    message = client.messages.create(
        to=str(to_num),  # '9786185596',
        from_='+19783103894',
        body=body+' :: '+str(dt.now()))


def log(message: str):
    f = open('/home/pi/sms_log.txt', 'a')
    f.write(message)
    f.write('\n')
    f.close()


if __name__ == '__main__':
    log('=' * 30)
    log('dispense.py - main')
    log('dispense.py arguments - {}'.format(sys.argv))
    try:
        # send an sms
        send_sms('Remember to take your {}'.format(sys.argv[1]))
        # Run the C program
        stepper_cmd = '/home/pi/stepper {}'.format(sys.argv[2])
        log('dispense.py - {}'.format(stepper_cmd))
        os.system(stepper_cmd)
        # wait and 
        time.sleep(5)
        try:
            f = log('/home/pi/meds.dat')
            l = f.readline()
            l = l.split(',')
            status = int(l[0])
            last_pos = int(l[1])
            f.close()
        except Exception as e:
            log('dispense.py - error occured in second level of main')
            log(str(e))
            status = -1
            last_pos = -1
        upload_record(status, last_pos, sys.argv[3])
    except Exception as e:
        log('dispense.py - error occurred in top level of main')
        log(str(e))
        pass
