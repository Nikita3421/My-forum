# Generated by Django 4.2.2 on 2023-08-26 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='rating',
        ),
    ]