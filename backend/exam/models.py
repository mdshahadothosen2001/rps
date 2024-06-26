from django.db import models

from utils.models import TimeStamp
from user.models import UserAccount
from semester.models import Semester


class Examination(TimeStamp, models.Model):
    name = models.CharField(max_length=55)
    course = models.CharField(max_length=55, null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    deadline = models.DateTimeField()
    question = models.URLField()

    def __str__(self):
        return f"{self.name} {self.course}"


    class Meta:
        verbose_name = "Examination"
        verbose_name_plural = "Examinations"
        db_table = "examination"
