# Generated by Django 4.2.13 on 2024-06-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_alter_subscriber_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='subscribe_type',
            field=models.CharField(choices=[('W', 'Subscribe Weekly'), ('M', 'Subscribe Monthly')], default='Subscribe Weekly', max_length=1),
        ),
    ]