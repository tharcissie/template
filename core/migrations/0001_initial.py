# Generated by Django 3.1.3 on 2022-01-13 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('certificate_number', models.CharField(max_length=255)),
                ('issued_date', models.DateField()),
                ('expiration_date', models.CharField(max_length=100)),
                ('attachment', models.FileField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('field_of_study', models.CharField(max_length=255)),
                ('_from', models.DateField()),
                ('_to', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('_from', models.DateField()),
                ('_to', models.DateField()),
                ('current', models.BooleanField(default=True)),
            ],
        ),
    ]
