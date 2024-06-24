from django.db import models

from utils.models import CommonInfo
from user.models import UserAccount


class Semester(CommonInfo, models.Model):
    semester_no = models.PositiveSmallIntegerField()
    session = models.CharField(max_length=15)
    department = models.CharField(max_length=15)
    teachers = models.ManyToManyField(UserAccount, related_name='semester_teacher')
    students = models.ManyToManyField(UserAccount, related_name='semester_students')
    courses = models.CharField(max_length=255, null=True, blank=True)
    total_courses = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.semester_no}"
    
    class Meta:
        verbose_name = "Semester"
        verbose_name_plural = "Semesters"
        db_table = "semester"
