# Generated by Django 3.1.5 on 2021-02-24 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210222_1906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rbaresponse',
            options={'ordering': ['receipt_id', 'date']},
        ),
        migrations.RenameField(
            model_name='rbaresponse',
            old_name='reciept_id',
            new_name='receipt_id',
        ),
        migrations.AlterField(
            model_name='rbaresponse',
            name='link_code',
            field=models.UUIDField(default='d690d15ecff848d983fadc858595d685', editable=False),
        ),
    ]
