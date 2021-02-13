from rest_framework import permissions


class IsRO(permissions.BasePermission):

    message = 'Has no permission'

    def has_permission(self, request, view):
        IP = request.headers['X-Ip']

        return IP in ['192.168.0.105', '192.168.0.100', '192.168.0.102']