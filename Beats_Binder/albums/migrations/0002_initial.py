# Generated by Django 5.0.1 on 2024-01-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('albums', '0001_initial'),
        ('artists', '0001_initial'),
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(to='artists.artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(to='songs.song'),
        ),
    ]
