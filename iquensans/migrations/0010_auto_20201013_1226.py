# Generated by Django 3.1 on 2020-10-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iquensans', '0009_auto_20201013_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
