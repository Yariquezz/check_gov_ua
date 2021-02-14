from django.contrib import admin

from .models import RBAresponse, BankInfo


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


class BankInfoAdmin(admin.ModelAdmin):

    list_display = [
        'tax_code',
        'bank_name',
        'support_number_1',
        'support_number_2',
        'support_number_3',
        'email',
        'website',
        'info',
        'signature_person',
        'sign',
        'logo'
    ]


admin.site.register(RBAresponse, RBAresponseAdmin)
admin.site.register(BankInfo, BankInfoAdmin)
