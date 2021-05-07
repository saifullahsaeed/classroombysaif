# Generated by Django 3.1.7 on 2021-04-11 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0008_auto_20210216_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='class_lacture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lacture_id', models.CharField(max_length=50, verbose_name='lacture ID')),
                ('title', models.CharField(default='Lacture Title', max_length=100)),
                ('Discription', models.CharField(default='There Is No Discription About This Lacture', max_length=100)),
                ('lacture_video', models.URLField(max_length=100)),
                ('Related', models.CharField(default='There Is No Related Links for This Lacture Till Now', max_length=100)),
                ('meterial', models.URLField(max_length=100)),
                ('Upload_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date uploaded')),
                ('for_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_lacture_class_secretkey', to='dashboard.class_db')),
            ],
        ),
        migrations.CreateModel(
            name='views',
            fields=[
                ('view_id', models.UUIDField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='view uploaded')),
                ('for_lacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class_lacture')),
                ('viewed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(default='Class Name', max_length=100)),
                ('date_of_join', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rollno', models.CharField(default='Rool No', max_length=100)),
                ('is_cr', models.BooleanField(default=False)),
                ('class_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_class_secretkey', to='dashboard.class_db')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='quiz Title', max_length=100)),
                ('quiz_id', models.UUIDField()),
                ('Start_Date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start date')),
                ('Expires_Date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Due date')),
                ('for_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_class_secretkey', to='dashboard.class_db')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('comment_id', models.UUIDField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Post Date')),
                ('comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lacture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_class_secretkey', to='classes.class_lacture')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start date')),
                ('Expires_Date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Due date')),
                ('Upload_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date uploaded')),
                ('title', models.CharField(default='Assignment Title', max_length=100)),
                ('uid', models.CharField(default='Uid', max_length=100)),
                ('assignment_file', models.FileField(blank=True, upload_to='assignments')),
                ('for_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments_class_secretkey', to='dashboard.class_db')),
            ],
        ),
        migrations.CreateModel(
            name='assignment_submit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_id', models.CharField(default='Uid', max_length=100)),
                ('assignment_file', models.FileField(blank=True, upload_to='assignments')),
                ('Upload_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date uploaded')),
                ('for_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_submit_class_secretkey', to='dashboard.class_db')),
                ('submited_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]