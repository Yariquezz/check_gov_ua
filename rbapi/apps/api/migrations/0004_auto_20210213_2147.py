# Generated by Django 3.1.5 on 2021-02-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210213_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rbaresponse',
            options={'ordering': ['reciept_id', 'date']},
        ),
        migrations.AlterField(
            model_name='rbaresponse',
            name='link_code',
            field=models.UUIDField(default='8fd143b4e2484eefb8c04cbed781ac80', editable=False),
        ),
    ]
