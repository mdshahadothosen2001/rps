from django.db import models

from utils.models import TimeStamp
from user.models import UserAccount
from semester.models import Semester


class GPA(TimeStamp, models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    point = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.student.username


    class Meta:
        verbose_name = "GPA"
        verbose_name_plural = "GPAs"
        db_table = "gpa"
