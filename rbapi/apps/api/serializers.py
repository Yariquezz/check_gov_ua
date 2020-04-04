from rest_framework import serializers
from apps.api.models import RBAresponse, Receipt
from datetime import datetime


class RBAresponseSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(read_only=True)
    recipient = serializers.CharField(read_only=True)
    amount = serializers.IntegerField(read_only=True)
    date = serializers.SerializerMethodField()
    description = serializers.CharField(max_length=500, read_only=True)
    currencyCode = serializers.IntegerField(read_only=True)
    comissionRate = serializers.IntegerField(read_only=True)
    link_code = serializers.SerializerMethodField()

    def get_link_code(self, obj):
        link = 'http://localhost:8000/api/{}'.format(obj.link_code)
        return link

    def get_date(self, obj):
        normal_date = datetime.strftime(obj.date, '%Y-%m-%d')
        return normal_date

    class Meta:
        model = RBAresponse
        fields = [
            'sender',
            'recipient',
            'amount',
            'date',
            'description', 
            'currencyCode', 
            'comissionRate',
            'link_code'
        ]


