from django.db import models
from django.utils import timezone

class try_carousel(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.FileField(upload_to='./app1/static/app1/')
    link_url = models.CharField(max_length=256)
    sort = models.IntegerField(default=0)
    type = models.PositiveSmallIntegerField(default=0)
    state = models.BooleanField(default=0)
    createdate = models.DateTimeField(default=timezone.now())
    modifydate = models.DateTimeField(default=timezone.now())


