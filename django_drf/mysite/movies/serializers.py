from rest_framework import serializers
from .models import MovieData

class MovieSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=MovieData
        fields=['id','name','duration','rating','typ','image']