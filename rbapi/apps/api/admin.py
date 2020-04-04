from django.contrib import admin

from .models import RBAresponse

class RBAresponseAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'amount', 'date', 'description', 'currencyCode', 'comissionRate']

admin.site.register(RBAresponse, RBAresponseAdmin)