# Generated by Django 3.1.5 on 2021-02-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210213_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rbaresponse',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rbaresponse',
            name='link_code',
            field=models.UUIDField(default='0d41e93358e441f5b08abd2ecd0b6b6b', editable=False),
        ),
    ]
