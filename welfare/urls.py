from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('blog', BlogViewSet, basename='blog')
router.register('quote', QuoteViewSet, basename='quote')
router.register('timeline', TimelineViewSet, basename='timeline')


urlpatterns = router.urls