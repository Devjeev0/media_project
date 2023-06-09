from django.db import models
from datetime import datetime, timedelta

class room_model(models.Model):
    room = models.CharField(max_length=30,default="")


class timing_model(models.Model):
    starting_time = models.DateTimeField()
    ending_time = models.DateTimeField()

    def duration(self):
        return self.ending_time - self.starting_time


class team_model(models.Model):
    team_name = models.CharField(max_length=30,default="")
    name = models.CharField(max_length=30,default="")
    work_description = models.TextField(default="")
    Room = models.ForeignKey(room_model,on_delete=models.CASCADE)
    Time = models.ForeignKey(timing_model,on_delete=models.CASCADE)