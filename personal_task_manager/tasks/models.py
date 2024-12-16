from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from personal_task_manager.category.models import Category

UserModel = get_user_model()

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
        ('critical', 'critical')
    )


    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True,editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


