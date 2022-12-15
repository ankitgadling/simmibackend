from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('blog', BlogViewSet, basename='blog')
router.register('quote', QuoteViewSet, basename='quote')
router.register('timeline', TimelineViewSet, basename='timeline')
router.register('story', StoryViewSet, basename='story')
router.register('other-cause', OtherCauseViewSet, basename='other-cause')

urlpatterns = router.urls