# Generated by Django 3.1.2 on 2020-12-07 03:46

from django.db import migrations, models
import multi_email_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('allpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emails', multi_email_field.fields.MultiEmailField(default=[])),
            ],
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]
