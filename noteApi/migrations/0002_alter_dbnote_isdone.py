# Generated by Django 4.2.1 on 2023-09-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbnote',
            name='isDone',
            field=models.BooleanField(),
        ),
    ]
