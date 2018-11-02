from django.db import models

# Create your models here.


class Todo (models.Model):

    URGENT_IMPORTANT = 'UI'
    NOT_URGENT_IMPORTANT = 'NI'
    URGENT_NOT_IMPORTANT = 'UN'
    NOT_URGENT_NOT_IMPORTANT = 'NN'

    PRIORITY_CHOICES = (
        (URGENT_IMPORTANT, 'urgent&important'),
        (NOT_URGENT_IMPORTANT, 'not urgent&important'),
        (URGENT_NOT_IMPORTANT, 'urgent&not important'),
        (NOT_URGENT_NOT_IMPORTANT, 'not urgent&not important'),
    )

    title = models.CharField(max_length=50)
    content = models.TextField()
    dueDate = models.DateTimeField(
        blank=True,
        null = True
    )
    priority = models.CharField(
        max_length=2,
        choices=PRIORITY_CHOICES,
        default=NOT_URGENT_NOT_IMPORTANT,
    )
    done = models.BooleanField(default=False)