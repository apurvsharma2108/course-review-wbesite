from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=500)
    site=models.CharField(max_length=500)
    type=models.CharField(max_length=500)#intermediate high or low
    price=models.FloatField()
    description=models.TextField(max_length=5000)
    realse_Date=models.DateField()
    rating=models.FloatField(default=0)
    image=models.URLField(default=None,null=True)
    def __str__(self):
        return self.name
