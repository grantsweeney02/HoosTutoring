# Generated by Django 4.1.6 on 2023-05-01 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crse_id', models.CharField(max_length=6)),
                ('subject', models.CharField(max_length=6)),
                ('catalog_nbr', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_student', models.BooleanField(default=True)),
                ('exists', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.CharField(blank=True, max_length=200)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.profile')),
                ('requests', models.ManyToManyField(related_name='requests_by_student', to='login.request')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_rate', models.IntegerField()),
                ('about_me', models.CharField(blank=True, max_length=200)),
                ('courses', models.ManyToManyField(related_name='tutors', to='login.course')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.profile')),
                ('requests', models.ManyToManyField(related_name='requests_for_tutor', to='login.request')),
                ('students', models.ManyToManyField(related_name='students', to='login.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='tutors',
            field=models.ManyToManyField(related_name='tutors', to='login.tutor'),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.student')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.tutor')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.student'),
        ),
        migrations.AddField(
            model_name='request',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.tutor'),
        ),
    ]
