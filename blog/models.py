from django.db import models

class Cours(models.Model):
    title= models.CharField(max_length=255)
    image=models.ImageField(upload_to="saliou/")
    body= models.FileField()


    def __str__(self):
        return self.title 

