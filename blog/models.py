from django.db import models
from django.utils import timezone
# Create your models here.

class Table1 (models.Model):
    sn = models.IntegerField()
    name = models.CharField(max_length=70)
    matric = models.CharField(max_length=6)

class Post (models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s created %s' %(self.author.username, self.title)
