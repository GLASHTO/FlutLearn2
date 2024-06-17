from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Discussion(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE
    )
    title = models.CharField(
        max_length = 100
    )
    description = models.TextField()
    created_date = models.DateTimeField(
        auto_now_add = True
    )

    def __str__(self):
        return self.title

class Comments(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE
    )
    discussion = models.ForeignKey(
        Discussion,
        on_delete = models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(
        auto_now_add = True
    )

    def __str__(self):
        return f'{self.user} --> {self.discussion}'
