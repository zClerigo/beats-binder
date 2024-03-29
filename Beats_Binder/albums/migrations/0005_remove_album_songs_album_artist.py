# Generated by Django 5.0.1 on 2024-01-16 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_remove_album_artists'),
        ('artists', '0004_remove_artist_albums_remove_artist_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ManyToManyField(to='artists.artist'),
        ),
    ]
