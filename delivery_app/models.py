from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class Letter(models.Model):
    title = models.CharField(max_length=200)
    send_date = models.DateTimeField()
    text = models.TextField()
    users_read = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.title

    def number_of_readers(self):
        return self.users_read.count()