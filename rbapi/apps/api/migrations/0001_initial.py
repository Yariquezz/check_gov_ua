# Generated by Django 3.1.5 on 2021-02-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(

            name='RBAresponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciept_id', models.IntegerField()),
                ('sender', models.CharField(default=None, max_length=200, null=True)),
                ('recipient', models.CharField(default=None, max_length=200, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('date', models.DateTimeField()),
                ('description', models.CharField(default=None, max_length=500, null=True)),
                ('currencyCode', models.IntegerField(default=None, null=True)),
                ('commissionRate', models.IntegerField(null=True)),
                ('link_code', models.UUIDField(default='a241307dd8d74a02996c7735ae258d9f', editable=False)),
            ],
            options={
                'ordering': ['reciept_id'],
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default=None, max_length=500, null=True)),
            ],
        ),
    ]
