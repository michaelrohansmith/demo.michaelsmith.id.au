from django.db import models

# Simple model for step 2 of Nothing But Web demo
class Task(models.Model):

    STATUS_CHOICES = (
        (u'A', 'Active'),
        (u'I', 'Inactive'),
    )
    
    def get_status_value(self, symbol):
        for choice in self.STATUS_CHOICES:
            if symbol == choice[0]:
                return choice[1]
        return None
        
    name = models.CharField(max_length=20)
    next = models.ForeignKey('self', null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactive')
    start_here = models.BooleanField()
    
    def __unicode__(self):
        return '%s -> %s' % (self.name, self.next.name)
