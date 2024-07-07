from django.db import models

from utils.models import TimeStamp
from user.models import UserAccount
from exam.models import Examination


class Mark(TimeStamp, models.Model):
    examination = models.ForeignKey(Examination, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    mark = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if 94 <= self.mark <= 100:
            self.mark = 4.0
        elif 90 <= self.mark <= 93:
            self.mark = 3.7
        elif 87 <= self.mark <= 89:
            self.mark = 3.3
        elif 83 <= self.mark <= 86:
            self.mark = 3.0
        elif 80 <= self.mark <= 82:
            self.mark = 2.7
        elif 77 <= self.mark <= 79:
            self.mark = 2.3
        elif 73 <= self.mark <= 76:
            self.mark = 2.0
        elif 70 <= self.mark <= 72:
            self.mark = 1.7
        elif 67 <= self.mark <= 69:
            self.mark = 1.3
        elif 60 <= self.mark <= 66:
            self.mark = 1.0
        elif 0 <= self.mark <= 59:
            self.mark = 0.0
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Mark"
        verbose_name_plural = "Marks"
        db_table = "mark"
