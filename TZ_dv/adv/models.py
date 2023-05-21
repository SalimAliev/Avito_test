from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    data_create = models.DateTimeField(auto_now_add=True)


class Photo(models.Model):
    image_path = models.CharField(max_length=127, unique=True)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='photo')



