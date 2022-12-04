from .models import *
from rest_framework import viewsets
from .serializers import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class TimelineViewSet(viewsets.ModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer