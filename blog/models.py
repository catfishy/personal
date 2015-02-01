from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    text = models.TextField()
    post_title = models.CharField(max_length=500, blank=False, default='')
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.post_title

class BlogComment(models.Model):
    blogpost = models.ForeignKey(BlogPost)
    text = models.TextField()
    comment_title = models.CharField(max_length=500, blank=False, default='')
    comment_user = models.CharField(max_length=500, blank=False)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.comment_title