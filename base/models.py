from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Court(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

def now_plus_thirty():
    return timezone.now() + timedelta(days=30)

class Ticket(models.Model):
    name = models.CharField(max_length=50)
    request_stamp = models.DateTimeField(auto_now_add=True)
    served_stamp = models.DateTimeField(default=now_plus_thirty)
    message = models.TextField(max_length=5000)
    court = models.ForeignKey('Court')

    def __str__(self):
        return "Name: {}\nRequested: {}\nServed: {}\nMessage: {}\nCourt: {}".format(self.name,self.request_stamp,self.served_stamp,self.message,self.court)
