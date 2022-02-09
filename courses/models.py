from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
    )

    course_location = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    course_content = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    teacher_id = models.IntegerField(
        null=False,
        blank=False,
    )
    # Foriegn key
    # related_name 是M2M关系里面反向通过user来获取courses
    user = models.ManyToManyField(User, related_name="courses") #反向连接外键 User.courses