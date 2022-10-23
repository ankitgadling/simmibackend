from django.shortcuts import render
from .models import LatestNews
from .serializer import LatestNewsSerializer
from rest_framework import generics


# GET, POST
class NewsView(generics.ListCreateAPIView):
    queryset = LatestNews.objects.all()
    serializer_class = LatestNewsSerializer


# GET, PUT, PATCH, DELETE
class DetailNewsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LatestNews.objects.all()
    serializer_class = LatestNewsSerializer
    lookup_field = 'id'

