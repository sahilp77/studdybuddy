# Generated by Django 5.1 on 2024-09-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_room_options_alter_room_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
