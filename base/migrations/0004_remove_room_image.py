# Generated by Django 5.1 on 2024-09-06 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_room_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='image',
        ),
    ]
