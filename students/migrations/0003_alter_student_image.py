# Generated by Django 5.1.7 on 2025-03-15 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_options_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='student.jpg', upload_to='student_pictures'),
        ),
    ]
