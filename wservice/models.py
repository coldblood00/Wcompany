from django.db import models

class service(models.Model):
    image=models.ImageField(upload_to='images/')
    productDetail=models.CharField(max_length=200)
