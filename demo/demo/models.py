from django.db import models

# Simple model for step 2 of Nothing But Web demo
class Task(models.Model):

    name = models.CharField(max_length=20)
    next = models.ForeignKey('self', null=True, default=None, blank=True)
    is_active = models.BooleanField(default=False)
    start_here = models.BooleanField(default=False)
    
    def __unicode__(self):
        return '%s' % (self.name)
