# Generated by Django 3.2.8 on 2021-10-24 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_user_recieve_promo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='billing_address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
