# Generated by Django 3.0 on 2020-01-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0003_remove_tutor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
