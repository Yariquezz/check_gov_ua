# Generated by Django 3.1.5 on 2021-02-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210214_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rbaresponse',
            name='link_code',
            field=models.UUIDField(default='bca7949f806240d79017f5a83a2ca347', editable=False),
        ),
    ]
