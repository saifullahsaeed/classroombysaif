# Generated by Django 3.1.6 on 2021-02-13 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210213_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_db',
            name='class_secretkey',
            field=models.CharField(default=None, max_length=50, unique=True),
        ),
    ]