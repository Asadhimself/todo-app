import datetime

from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete', 'deadline']

    @property
    def time_remain(self):
        date_str = self.deadline.ctime()
        datetime_obj = datetime.datetime.strptime(date_str,
                                                  "%a %b %d %H:%M:%S %Y")
        if datetime_obj < datetime.datetime.now():
            return 'Time is up!'
        remain = datetime_obj - datetime.datetime.now()
        remain = datetime.datetime.utcfromtimestamp(remain.total_seconds())
        return remain.strftime("%d days %H:%M")

    @property
    def deadline_color(self):
        if self.time_remain == 'Time is up!':
            return 'danger'
        date_str = self.deadline.ctime()
        datetime_obj = datetime.datetime.strptime(date_str,
                                                  "%a %b %d %H:%M:%S %Y")
        remain = datetime_obj - datetime.datetime.now()
        remain = remain.total_seconds()
        if remain <= 86400:
            return 'warning'
        return 'success'
