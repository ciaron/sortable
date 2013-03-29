from django.db import models

# Create your models here.
class Entry(models.Model):
    
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=50)
    data = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
