# Generated by Django 3.0.2 on 2020-03-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0002_auto_20200222_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
