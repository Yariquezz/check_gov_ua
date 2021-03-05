from rest_framework import serializers
from apps.api.models import RBAResponse


class UpdateBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RBAResponse
        fields = [
            'receipt_id',
            'sender',
            'recipient',
            'amount',
            'date',
            'description', 
            'currencyCode', 
            'commissionRate',
        ]
