# Generated by Django 4.2.2 on 2023-09-28 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_delete_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
