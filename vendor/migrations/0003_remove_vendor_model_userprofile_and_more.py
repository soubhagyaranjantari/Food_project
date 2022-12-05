# Generated by Django 4.0.6 on 2022-11-30 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0002_alter_vendor_model_is_approved_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor_model',
            name='userProfile',
        ),
        migrations.AlterField(
            model_name='vendor_model',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
