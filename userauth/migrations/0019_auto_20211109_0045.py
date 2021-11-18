# Generated by Django 3.2.8 on 2021-11-09 00:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0018_alter_movieshowtime_showtimes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedulemovie',
            name='movieDate',
        ),
        migrations.AddField(
            model_name='schedulemovie',
            name='PlayingTill',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]