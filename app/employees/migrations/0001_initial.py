# Generated by Django 3.2.2 on 2022-02-01 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=70)),
                ('last_name', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone_number', models.IntegerField(blank=True, default='')),
                ('clock_in_number', models.IntegerField(default='', unique=True)),
            ],
        ),
    ]