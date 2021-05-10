from django.test import TestCase

import requests
import json
import socket
import hashlib
import hmac
import base64
from datetime import datetime


def signature(check, time, word):
    message = bytes("{}{}".format(check, time), 'utf-8')
    secret = bytes(word, 'utf-8')
    sign = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest()).decode('utf-8')

    return sign


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception as err:
        IP = '127.0.0.1'
        print(err)
    finally:
        s.close()
    return IP


def run(check):
    ip = get_ip()
    time = str(int(datetime.now().timestamp()))
    password = signature(check=check, time=time, word='12345')

    params = {}
    url = 'http://localhost:8000/api/check'
    response = requests.get(
        url=url,
        json=params,
        headers={
                    'Content-Type': 'application/json',
                    'x-time': time,
                    'x-check-id': check,
                    'x-real-ip': ip,
                    'x-hmac': password
                }
    ).text
    return response


ck = ['2000', '2001', '2002', '2003', '2004', '2005', '2006']

for j in ck:
    check_num = j
    resp = ""
    my_response = json.loads(run(check_num))

    try:
        doc = {
            "sender": "платник",
            "recipient": "отримувач",
            "amount": "сумма",
            "date": "дата",
            "description": "призначення",
            "currencyCode": "валюта",
            "commissionRate": "комісія",
            "link_code": "скачати квитанцію тут"
        }
        for i in my_response['payments'][0]:
            resp += ("{}{} {}\n".format(doc[i], ":", my_response['payments'][0][i]))
    except Exception as err:
        print('Error: {}'.format(err))
    else:
        print(resp)

print(signature(1, t)
