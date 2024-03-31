from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Registration(models.Model):
    OPTION_CHOICES = (
        ('offline', 'Offline'),
        ('online', 'Online'),
    )
    option = models.CharField(max_length=10, choices=OPTION_CHOICES)
    employee_id = models.CharField(max_length=100)
    filled_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations', default=None, null=True)
    timestamp = models.DateTimeField(default=timezone.now) 
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.employee_id
