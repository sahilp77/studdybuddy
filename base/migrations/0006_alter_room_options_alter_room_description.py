# Generated by Django 5.1 on 2024-09-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-create_at', '-updated_at']},
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
