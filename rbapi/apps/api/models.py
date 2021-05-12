from django.db import models
import uuid


def get_default_uuid():
    return uuid.uuid4().hex


class BankInfo(models.Model):
    tax_code = models.CharField(primary_key=True, max_lenght=20)
    bank_name = models.CharField(max_length=200, default=None, null=True)
    support_number_1 = models.CharField(max_length=13, default=None, null=True)
    support_number_2 = models.CharField(max_length=13, default=None, null=True)
    support_number_3 = models.CharField(max_length=13, default=None, null=True)
    email = models.CharField(max_length=20, default=None, null=True)
    website = models.CharField(max_length=20, default=None, null=True)
    info = models.TextField(max_length=500, default=None, null=True)
    signature_info = models.TextField(max_length=100, default=None, null=True)
    signature_person = models.TextField(max_length=100, default=None, null=True)
    sign = models.ImageField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = [
            'tax_code',
            'bank_name'
        ]

    def __str__(self):
        return '{} {}'.format(self.bank_name, self.tax_code)


class RBAResponse(models.Model):
    receipt_id = models.IntegerField(primary_key=True, unique=True)
    sender = models.CharField(max_length=200, default=None, null=True)
    recipient = models.CharField(max_length=200, default=None, null=True)
    amount = models.IntegerField(null=True, blank=False)
    date = models.DateTimeField()
    description = models.CharField(max_length=500, default=None, null=True)

    CURRENCY_CODES = [
        (980, 'UAH'),
        (840, 'USD'),
        (978, 'EUR'),
    ]
    currencyCode = models.IntegerField(default=None, null=True, choices=CURRENCY_CODES)
    commissionRate = models.IntegerField(null=True, blank=False)
    link_code = models.UUIDField(default=get_default_uuid(), editable=False)
    sender_bank_tax_code = models.ForeignKey(
        BankInfo,
        default=None,
        null=True,
        related_name='sender_bank_tax_code',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = [
            'receipt_id',
            'date'
        ]

    def __str__(self):
        return 'receipt {}'.format(self.receipt_id)
