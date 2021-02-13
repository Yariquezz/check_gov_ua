from rest_framework import serializers
from apps.api.models import RBAresponse


class UpdateBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RBAresponse
        fields = [
            'reciept_id',
            'sender',
            'recipient',
            'amount',
            'date',
            'description', 
            'currencyCode', 
            'commissionRate',
        ]
