from django.db import models

# Create your models here.
class Event(models.Model):
    event_title=models.CharField(max_length=120)
    event_location= models.CharField(max_length=70)
    date=models.CharField(max_length=10)
    description=models.TextField()
    def _str_(self):
        return self.event_title
    
class Fillform(models.Model):
    fullname=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
    event=models.ForeignKey("Event",on_delete=models.CASCADE)
