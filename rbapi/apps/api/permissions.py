import hashlib
import hmac
import base64
from rest_framework import permissions
from django.conf import settings


class IsCheckGov(permissions.BasePermission):

    message = 'Has no permission'

    def has_permission(self, request, view):
        password = request.headers['X-Hmac']
        message = bytes("{}{}".format(request.headers['X-Check-Id'], request.headers['X-Time']), 'utf-8')
        secret = bytes(settings.API_KEY, 'utf-8')
        signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest()).decode('utf-8')
        return signature == password
