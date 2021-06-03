# Generated by Django 3.2.3 on 2021-06-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='images')),
                ('description', models.TextField()),
                ('available', models.BooleanField(default=True)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(verbose_name=100)),
            ],
        ),
    ]
