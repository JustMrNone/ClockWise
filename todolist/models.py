from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tasks(models.Model):
    PRIORITY = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    due_time = models.TimeField(blank=True, null=True)
    starred = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY, default="medium")
    notes = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    overdue = models.BooleanField(default=False)
    category = models.CharField(max_length=255, blank=True, null=True)
    recurrence = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    
    
