from django.db import models
import uuid

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    age = models.CharField(max_length=2, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, max_length=10)
    cgpa = models.CharField(max_length=5, blank=True, null=True)
    dob = models.DateField()
    level = models.CharField(max_length=3, null=True, blank=True)
    department = models.CharField(max_length=150, null=True, blank=True)
    matric_no = models.CharField(max_length=12, null=True, blank=True)
    student_image = models.ImageField()
    extra_year = models.BooleanField(default=False)