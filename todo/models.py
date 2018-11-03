from django.db import models

# Create your models here.


class Todo (models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    dueDate = models.DateField(
        blank= True,
        null = True
    )
    importance = done = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
