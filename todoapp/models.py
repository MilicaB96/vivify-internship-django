from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=255)
    PRIORITY_CHOICES = [
        ('CRITICAL','critical'),
        ('IMPORTANT','important'),
        ('NORMAL','normal'),
        ('LOW','low'),

    ]
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='LOW',
    )
