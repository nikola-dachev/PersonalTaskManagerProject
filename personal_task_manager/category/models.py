from django.db import models

# Create your models here.
class Category(models.Model):
    CATEGORY_CHOICES = (
        ('Chores', 'Chores'),
        ('Work', 'Work'),
        ('Hobbies', 'Hobbies'),
        ('Sports', 'Sports'),
        ('Study', 'Study'),
    )

    name = models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True,editable=False)
    updated_date = models.DateTimeField(auto_now=True,editable=False)


