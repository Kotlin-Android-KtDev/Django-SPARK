# Generated by Django 3.0.2 on 2020-02-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom_message',
            name='author',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='chatroom_message',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='chatroom_message',
            name='room_name',
            field=models.TextField(blank=True),
        ),
    ]