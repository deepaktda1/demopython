from django.db import models
class mobile(models.Model):
    mobname=models.CharField(max_length=250)
    des=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='gallery')
    def __str__(self):
        return self.mobname
# Create your models here.
