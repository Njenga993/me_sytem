from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Indicator(models.Model):
    project = models.ForeignKey(Project, related_name='indicators', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    baseline_value = models.FloatField()
    target_value = models.FloatField()
    current_value = models.FloatField(default=0.0)
    unit = models.CharField(max_length=100, default='percentage')
    gender_disaggregated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.project.name})"
