from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=500)
    site=models.CharField(max_length=500)
    type=models.CharField(max_length=500)#intermediate high or low
    price=models.FloatField()
    description=models.TextField(max_length=5000)
    realse_Date=models.DateField()
    AverageRating=models.FloatField(default=0)
    image=models.URLField(default=None,null=True)
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Review(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(max_length=1000)
    rating=models.FloatField(default=0)

    def __str__(self):
        return self.user.username
