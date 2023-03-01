from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=1024)
    date_created = models.DateTimeField(default=now, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
