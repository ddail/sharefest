# Generated by Django 3.1.2 on 2020-12-07 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allpages', '0002_auto_20201206_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserID', models.IntegerField(max_length=255, primary_key=True, serialize=False, verbose_name='User ID')),
                ('UserName', models.CharField(blank=True, max_length=254, null=True, verbose_name='User Name')),
                ('Email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('Phone', models.CharField(blank=True, max_length=254, null=True, verbose_name='Phone Number')),
            ],
        ),
    ]
