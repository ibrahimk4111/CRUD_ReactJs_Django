# Generated by Django 4.2.1 on 2023-09-20 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbnote',
            name='is_done',
        ),
    ]
