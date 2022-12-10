from django.urls import path


from .viewsets import *
urlpatterns = [
    path('peoplemessage/',PaymentShortViews.as_view()),
    path('payment_details/',PaymentDetailViewset.as_view()),
    path('piechart/',PaymentPiechartViewset),
    
    ]
