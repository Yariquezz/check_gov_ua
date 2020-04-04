from django.db import models
import uuid


def get_default_uuid():
    return uuid.uuid4().hex


class RBAresponse(models.Model):
    reciept_id = models.IntegerField()
    sender = models.CharField(max_length=200, default=None, null=True)
    recipient = models.CharField(max_length=200, default=None, null=True)
    amount = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField()
    description = models.CharField(max_length=500, default=None, null=True)
    currencyCode = models.IntegerField (default=None, null=True)
    comissionRate = models.IntegerField(null=True,blank=False)
    link_code = models.UUIDField(default=get_default_uuid(), editable=False)


class Receipt(models.Model):
    link = models.CharField(max_length=500, default=None, null=True)


class Logs(models.Model):
    recipept_id = models.OneToOneField(RBAresponse, on_delete=models.CASCADE, related_name='check_gov_log', blank=True, null=True)
    send_date = models.DateTimeField(verbose_name='Send Date', auto_now_add=True)
    log_field = models.TextField(verbose_name='Log', blank=True, null=True)
    request = models.TextField(verbose_name='Request', blank=True, null=True)
    response_status = models.CharField(max_length=100, default=None, null=True)







    

