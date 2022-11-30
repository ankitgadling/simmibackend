from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('blog', BlogViewSet, basename='blog')


urlpatterns = router.urls