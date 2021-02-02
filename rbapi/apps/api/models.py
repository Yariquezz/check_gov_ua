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
    currencyCode = models.IntegerField(default=None, null=True)
    commissionRate = models.IntegerField(null=True, blank=False)
    link_code = models.UUIDField(default=get_default_uuid(), editable=False)

    class Meta:
        ordering = ['reciept_id']

    def __str__(self):
        return 'receipt {}'.format(self.reciept_id)


class Receipt(models.Model):
    link = models.CharField(max_length=500, default=None, null=True)
