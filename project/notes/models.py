from django.db import models
from django.utils.timezone import now
# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=1024)
    date_created = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title
