# Generated by Django 4.2.6 on 2023-12-12 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0002_remove_movie_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genretwo',
            new_name='genre',
        ),
    ]
