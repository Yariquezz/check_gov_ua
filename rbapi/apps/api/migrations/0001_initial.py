# Generated by Django 2.2.4 on 2020-01-31 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

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
                ('comissionRate', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default=None, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_date', models.DateTimeField(auto_now_add=True, verbose_name='Send Date')),
                ('log_field', models.TextField(blank=True, null=True, verbose_name='Log')),
                ('request', models.TextField(blank=True, null=True, verbose_name='Request')),
                ('response_status', models.CharField(default=None, max_length=100, null=True)),
                ('recipept_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='check_gov_log', to='api.RBAresponse')),
            ],
        ),
    ]
