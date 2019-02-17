"""
run this file: python3 dispense.py "med name"
"""

import sys
import os
from twilio.rest import Client


def send_sms(body, to_num: str = '9786185596'):
    acount_sid = 'AC819c0afb11b689eb481878955d9ada5f'
    auth_token = 'c1bb38dcaaa6ca7fc6a72f17d21ba38c'

    client = Client(acount_sid, auth_token)

    message = client.messages.create(
        to=str(to_num),  # '9786185596',
        from_='+19783103894',
        body=body)


if __name__ == '__main__':
    try:
        # send an sms
        send_sms('Remember to take your {}'.format(sys.argv[1]))
        # Run the C program
        os.system("./stepper.out")
    except:
        pass
