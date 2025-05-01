from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class ChatRoom(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args,**kwargs)

class ChatMessage(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
    message_content=models.TextField()
    date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=("date",)