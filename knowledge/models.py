from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from django.conf import settings

class KPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    upload = models.FileField(
        upload_to='uploadsKnowledge/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('kpost-detail', kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.kcomments.filter(approved_comment=True)


class KComment(models.Model):
    post = models.ForeignKey(KPost, on_delete=models.CASCADE, related_name='kcomments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    commentfile = models.FileField(upload_to='uploadsknowledgecomment/%Y/%m/%d/', blank=True, null=True)


    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('kpost-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.text
