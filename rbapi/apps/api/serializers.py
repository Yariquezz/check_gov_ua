from rest_framework import serializers
from apps.api.models import RBAResponse
from datetime import datetime
from django.conf import settings


class RBAResponseSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(read_only=True)
    recipient = serializers.CharField(read_only=True)
    amount = serializers.IntegerField(read_only=True)
    date = serializers.SerializerMethodField()
    description = serializers.CharField(max_length=500, read_only=True)
    currencyCode = serializers.IntegerField(read_only=True)
    commissionRate = serializers.IntegerField(read_only=True)
    link_code = serializers.SerializerMethodField()

    def get_link_code(self, obj):
        link = 'http://{}/api/{}'.format(settings.HOSTNAME, obj.link_code)
        return link

    def get_date(self, obj):
        normal_date = datetime.strftime(obj.date, '%Y-%m-%d')
        return normal_date

    class Meta:
        model = RBAResponse
        fields = [
            'sender',
            'recipient',
            'amount',
            'date',
            'description',
            'currencyCode',
            'commissionRate',
            'link_code',
        ]
