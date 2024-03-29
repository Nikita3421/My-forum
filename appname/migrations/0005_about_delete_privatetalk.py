# Generated by Django 4.2.2 on 2023-10-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0004_alter_artwork_description_alter_artwork_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(unique=True)),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='PrivateTalk',
        ),
    ]
