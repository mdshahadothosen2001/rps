from django.db import models

from utils.models import TimeStamp
from user.models import UserAccount
from exam.models import Examination


class Answer(TimeStamp, models.Model):
    examination = models.ForeignKey(Examination, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    answer = models.URLField(null=True, blank=True)


    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        db_table = "answer"
