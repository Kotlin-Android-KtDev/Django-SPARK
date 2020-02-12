# Generated by Django 2.2 on 2020-02-12 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='city',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='tutor',
            name='gender',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='tutor',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='expert',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='name',
            field=models.TextField(blank=True, default=''),
        ),
    ]