# Generated by Django 4.0.1 on 2023-01-19 19:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.CharField(blank=True, max_length=2, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('cgpa', models.CharField(blank=True, max_length=5, null=True)),
                ('dob', models.DateField()),
                ('level', models.CharField(blank=True, max_length=3, null=True)),
                ('department', models.CharField(blank=True, max_length=150, null=True)),
                ('matric_no', models.CharField(blank=True, max_length=12, null=True)),
                ('student_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
