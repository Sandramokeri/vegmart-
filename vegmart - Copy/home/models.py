from django.db import models


# Create your models here.
class Vegitables(models.Model):
    item=models.CharField(max_length=50,unique=True)
    price=models.FloatField()
    status=models.CharField(max_length=12)
    veg_image=models.ImageField(upload_to='uploads')
    def __str__(self):
        return self.item
            

