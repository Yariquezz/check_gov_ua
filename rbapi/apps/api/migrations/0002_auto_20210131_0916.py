# Generated by Django 3.1.5 on 2021-01-31 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rbaresponse',
            name='link_code',
            field=models.UUIDField(default='aa7b45eb2a3d4e11a7800f64a0ebe257', editable=False),
        ),
    ]
