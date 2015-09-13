from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Court(models.Model):
    name = models.CharField(max_length=500)
    key = models.CharField(max_length=100, default="This Is The Default Password 123")

    def __str__(self):
        return self.name

def now_plus_thirty():
    return timezone.now() + timedelta(days=30)

class Ticket(models.Model):
    name = models.CharField(max_length=40)
    request_stamp = models.DateTimeField(default=timezone.now)
    served_stamp = models.DateTimeField(default=now_plus_thirty)
    message = models.TextField(max_length=5000)
    email = models.EmailField()
    court = models.ForeignKey('Court')

    def __str__(self):
        return "Name: {}\nEmail: {}\nRequested: {}\nServed: {}\nMessage: {}\nCourt: {}".format(self.name,self.email,self.request_stamp,self.served_stamp,self.message,self.court)
