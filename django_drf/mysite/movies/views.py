from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import MovieData
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset=MovieData.objects.all()
    serializer_class=MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    # queryset=MovieData.objects.filter(typ='Action')
    def get_queryset(self):
        return MovieData.objects.filter(typ='Action')

    serializer_class=MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    # queryset=MovieData.objects.filter(typ='Comedy')
    def get_queryset(self):
    # queryset=MovieData.objects.filter(typ='Comedy')
        return MovieData.objects.filter(typ='Comedy')
    serializer_class=MovieSerializer