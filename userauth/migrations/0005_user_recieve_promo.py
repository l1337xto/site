# Generated by Django 3.2.8 on 2021-10-24 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_alter_shows_playing_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='recieve_promo',
            field=models.BooleanField(default=False),
        ),
    ]