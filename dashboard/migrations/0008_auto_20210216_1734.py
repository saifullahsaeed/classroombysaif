# Generated by Django 3.1.6 on 2021-02-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_merge_20210216_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_db',
            name='class_image',
            field=models.ImageField(default='class_banners/default.png', upload_to='class_banners'),
        ),
        migrations.AlterModelTable(
            name='class_db',
            table='Class_db',
        ),
    ]
