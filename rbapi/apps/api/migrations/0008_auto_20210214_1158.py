# Generated by Django 3.1.5 on 2021-02-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210214_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rbaresponse',
            name='link_code',
            field=models.UUIDField(default='0b40d2f3c11947c58019b428fb0cbd93', editable=False),
        ),
    ]