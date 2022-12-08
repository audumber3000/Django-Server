# Generated by Django 4.0.4 on 2022-11-01 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Auth', '0003_alter_authuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('dob', models.DateField()),
                ('city', models.CharField(max_length=255)),
                ('State', models.CharField(max_length=255)),
                ('college', models.CharField(max_length=255)),
                ('clg_email', models.CharField(max_length=255, unique=True)),
                ('clg_city', models.CharField(max_length=255)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='PersonalInfo',
        ),
        migrations.DeleteModel(
            name='ProfessionalInfo',
        ),
    ]
