from django.db import models

# Create your models here.
class MovieData(models.Model):
    name=models.CharField(max_length=200)
    duration=models.FloatField()
    rating=models.FloatField()
    typ=models.CharField(max_length=200,default='Action')
    image=models.ImageField(upload_to='Images/',default='Images/None/No-img.jpg')
    

    def __str__(self):
        return self.name