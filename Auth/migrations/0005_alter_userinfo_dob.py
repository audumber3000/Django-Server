# Generated by Django 4.0.4 on 2022-11-01 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0004_userinfo_delete_authuser_delete_personalinfo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='dob',
            field=models.CharField(max_length=30),
        ),
    ]
