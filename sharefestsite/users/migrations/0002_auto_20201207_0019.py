# Generated by Django 3.1.2 on 2020-12-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='current_pw',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
