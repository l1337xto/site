# Generated by Django 3.2.8 on 2021-10-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0006_user_billing_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', upload_to='user_pics/'),
        ),
    ]
