from rest_framework import permissions
from django.conf import settings

class IsRO(permissions.BasePermission):

    message = 'Has no permission'

    def has_permission(self, request, view):
        IP = request.headers['X-Ip']

        return IP in settings.PERMITTED_HOSTS