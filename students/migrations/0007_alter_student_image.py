# Generated by Django 5.1.7 on 2025-03-16 04:39

import students.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_student_created_at_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='student.jpg', upload_to='student_pictures', validators=[students.models.validate_image_size]),
        ),
    ]
