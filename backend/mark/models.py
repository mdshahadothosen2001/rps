from django.db import models

from utils.models import TimeStamp
from user.models import UserAccount
from exam.models import Examination


class Mark(TimeStamp, models.Model):
    examination = models.ForeignKey(Examination, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    mark = models.PositiveSmallIntegerField()


    class Meta:
        verbose_name = "Mark"
        verbose_name_plural = "Marks"
        db_table = "mark"
