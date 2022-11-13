from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('press-media',PressMediaView, basename='press-media')
router.register('electronic-media',ElectronicMediaView, basename='electronic-media')
router.register('eminent-personality',EminentPersonalityView, basename='eminent-personality')


urlpatterns = router.urls