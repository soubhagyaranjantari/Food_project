# Generated by Django 4.0.6 on 2022-12-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_remove_vendor_model_userprofile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_model',
            name='vendor_license',
            field=models.ImageField(blank=True, upload_to='up_load'),
        ),
    ]
