from django.db import models

class about(models.Model):
    image=models.ImageField(upload_to='images/')
    sum=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.title
