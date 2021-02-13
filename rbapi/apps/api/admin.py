from django.contrib import admin

from .models import RBAresponse


class RBAresponseAdmin(admin.ModelAdmin):
    list_display = [
        'reciept_id',
        'sender',
        'recipient',
        'amount',
        'date',
        'description',
        'currencyCode',
        'commissionRate'
    ]


admin.site.register(RBAresponse, RBAresponseAdmin)
