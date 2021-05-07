# Generated by Django 3.1.6 on 2021-02-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210213_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_db',
            name='class_createdby',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='class_db',
            name='class_image',
            field=models.ImageField(upload_to='class_banners'),
        ),
        migrations.AlterField(
            model_name='class_db',
            name='class_secretkey',
            field=models.CharField(default='be1679-6ae28652eb-fa7cd6-de96-a8cc', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='class_db',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='class_db',
            table='Class_db',
        ),
    ]
