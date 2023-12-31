# Generated by Django 4.2.6 on 2023-12-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0003_customuser_is_staff_customuser_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profiles',
            field=models.ManyToManyField(blank=True, to='netflixapp.profile'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
