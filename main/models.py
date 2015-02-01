from django.db import models

# Create your models here.
class WritingSample(models.Model):
    title = models.CharField(max_length=500, blank=False, default='')
    text = models.TextField()
    static_img_location = models.CharField(max_length=500, blank=True, default=None)
    archived = models.BooleanField(default=True)
    writing_type = models.CharField(max_length=100, blank=False, default='')

    def __str__(self):
        return self.title

class MusicSample(models.Model):
    title = models.CharField(max_length=500, blank=False, default='')
    text = models.CharField(max_length=2000, blank=False)
    embed_html = models.CharField(max_length=600, blank=False, default='')
    archived = models.BooleanField(default=True)

    def __str__(self):
        return self.title

