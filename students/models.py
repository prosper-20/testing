from django.db import models
from django.core.exceptions import ValidationError


GRADE_CHOICES = (
    ("P1", "Primary One"),
    ("P2", "Primary Two")
)

GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other")
)

def validate_image_size(value):
    # 1MB = 1024 * 1024 bytes
    max_size = 1024 * 1024
    if value.size > max_size:
        raise ValidationError(f"The image size should not exceed {max_size} bytes (1MB).")


class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(choices=GRADE_CHOICES, max_length=100)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    image = models.ImageField(default="student.jpg", upload_to="student_pictures", validators=[validate_image_size])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): # It formats the display on the admin panel
        return self.name

    # dunder str method
    # special method

    class Meta:
        verbose_name_plural = "Students"
