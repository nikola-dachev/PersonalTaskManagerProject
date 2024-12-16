from django.contrib.auth import get_user_model
from django.db import models

CustomUser = get_user_model()
# Create your models here.
class Dashboard(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='dashboards')
    total_tasks = models.IntegerField(default=0)
    completed_tasks = models.IntegerField(default=0)
    pending_tasks = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)


class Progress(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='progress')
    tasks_completed_today = models.PositiveIntegerField(default=0)
    tasks_completed_this_week = models.PositiveIntegerField(default=0)
    completion_rate = models.FloatField(default=0.0)


class Widget(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='widgets')
    title = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveIntegerField()



