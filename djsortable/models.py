from django.db import models
from django.forms import ModelForm

# Create your models here.
class Entry(models.Model):
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "entries"

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=50)
    data = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = "__all__"
