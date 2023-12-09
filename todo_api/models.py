from datetime import time
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    title = models.CharField(max_length = 180)
    description = models.TextField(blank = True, null = True)
    due_date = models.DateField(blank = True, null = True, default = time)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    status = models.CharField(max_length = 180, choices = STATUS_CHOICES, default = 'Pending')
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.title