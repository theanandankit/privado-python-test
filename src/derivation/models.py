from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import datetime

# Create your models here.
class Comment():
    post = models.ForeignKey('Post', related_name='comments')
    customerId = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    text = models.TextField()
    date_of_birth = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
