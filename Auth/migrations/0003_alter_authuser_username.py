# Generated by Django 4.0.4 on 2022-11-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_authuser_personalinfo_professionalinfo_delete_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
