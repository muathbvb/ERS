# Generated by Django 3.0.8 on 2020-12-05 11:10

import Student.models
import Student.storage
import datetime
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_unique_email', '0003_auto_20201124_0305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('image', models.ImageField(default='courses/course.png', storage=Student.storage.OverwriteStorage(), upload_to=Student.models.Course.upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('docs', 'Documents'), ('image', 'Images'), ('file', 'File'), ('link', 'URL LINK'), ('zip', 'Archive')], default='image', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('accept', models.BooleanField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('user_unique_email.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.CharField(max_length=500)),
                ('file', models.FileField(upload_to=Student.models.Post.upload_to, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'png', 'xlsx', 'xls', 'zip', '7z', 'rar', 'mp4', 'avi', 'mp3'], message='These extension not allowed sorry')])),
                ('publish_date', models.DateTimeField(default=datetime.datetime(2020, 12, 5, 11, 10, 34, 53621, tzinfo=utc), verbose_name='publish_date')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Course')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='post_dislikes', to='Student.Student')),
                ('file_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.FileType')),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to='Student.Student')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Student')),
            ],
        ),
    ]
