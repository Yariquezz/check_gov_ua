from django.test import TestCase, RequestFactory
from apps.api.models import BankInfo, RBAResponse
from apps.api.views import index, Enter
from django.conf import settings

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


class TestApi(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.bank = BankInfo(
            tax_code=21133352,
            bank_name="АТ Універсал Банк",
            support_number_1="0 800 205 205",
            support_number_2="0 800 205 205",
            support_number_3="0 800 205 205",
            email='support@monobank.com',
            website='http://www.monobank.com',
            info='monobank',
            signature_info='Deputy Charmain',
            signature_person='Oleg Gorokhovskyi',
            sign=None,
            logo=None,
        )
        self.bank.save()
        self.response = RBAResponse(
            receipt_id=2,
            sender='Me',
            recipient='You',
            amount=100.00,
            date=datetime.now(),
            description='For that',
            currencyCode=980,
            commissionRate=0,
            sender_bank_tax_code=self.bank,
        )
        self.response.save()

    def tearDown(self):
        pass

    def test_index(self):
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_api_check_good(self):
        check = 2
        time = str(int(datetime.now().timestamp()))
        ip = get_ip()
        password = signature(check=check, time=time, word=settings.API_KEY)
        link = RBAResponse.objects.get(pk=check)
        request = self.factory.get('api/check')
        request.headers = {
            'Content-Type': 'application/json',
            'x-time': time,
            'X-Check-Id': check,
            'x-real-ip': ip,
            'x-hmac': password
        }
        r = Enter()
        response = r.get(request)
        self.assertEqual(
            response.data,
            {
                'payments': [
                    {
                        'amount': 100,
                        'commissionRate': 0,
                        'currencyCode': 980,
                        'date': '2021-06-21',
                        'description': 'For that',
                        'link_code': 'http://localhost:8000/api/' + str(link.link_code),
                        'recipient': 'You',
                        'sender': 'Me'
                    }
                ]
            }
        )

    def test_api_check_not_found(self):
        check = 1
        time = str(int(datetime.now().timestamp()))
        ip = get_ip()
        password = signature(check=check, time=time, word=settings.API_KEY)
        link = RBAResponse.objects.get(pk=2)
        request = self.factory.get('api/check')
        request.headers = {
            'Content-Type': 'application/json',
            'x-time': time,
            'X-Check-Id': check,
            'x-real-ip': ip,
            'x-hmac': password
        }
        r = Enter()
        response = r.get(request)
        self.assertEqual(
            response.data,
            {
                'message': 'Check is not found'
            },
        )

    def test_api_check_goes_wrong(self):
        check = 1
        time = str(int(datetime.now().timestamp()))
        ip = get_ip()
        password = signature(check=check, time=time, word=settings.API_KEY)
        request = self.factory.get('api/check')
        request.headers = {
            'Content-Type': 'application/json',
            'x-time': time,
            'X-check-id': check,
            'x-real-ip': ip,
            'x-hmac': password
        }
        r = Enter()
        response = r.get(request)
        self.assertEqual(
            response.data,
            {
                'message': 'Something goes wrong'
            },
        )
