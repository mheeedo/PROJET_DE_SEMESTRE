# Generated by Django 3.2.3 on 2021-06-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='adresse',
            field=models.CharField(default='not defined', max_length=100),
        ),
    ]
