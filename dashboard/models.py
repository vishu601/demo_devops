from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title


class Task(models.Model):
  STATUS_CHOICES = [
      ('TODO', 'To Do'),
      ('IN_PROGRESS', 'In Progress'),
      ('DONE', 'Done'),
  ]

  title = models.CharField(max_length=200)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  status = models.CharField(
      max_length=20, choices=STATUS_CHOICES, default='TODO'
  )
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title