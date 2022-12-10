from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin

class DonateViewset(viewsets.ModelViewSet):
    
    queryset=models.donate_form.objects.all()
    serializer_class=serializers.DonateFormSerializer

class PaymentViewset(viewsets.ModelViewSet):
    
    queryset=models.payment_method.objects.all()
    serializer_class=serializers.PaymentFormSerializers


class PaymentDetailViewset(GenericAPIView,ListModelMixin,CreateModelMixin):
    
    queryset=models.payment_details.objects.all()
    serializer_class=serializers.PaymentDetailSerializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class Give_help_Viewset(viewsets.ModelViewSet):
    
    queryset=models.Give_Your_Help.objects.all()
    serializer_class=serializers.Give_help_serializers


class Upi_viewset(viewsets.ModelViewSet):
    
    queryset=models.upi_tran.objects.all()
    serializer_class=serializers.Upitranserializers




@api_view(['GET'])
def PaymentPiechartViewset(request):
    if request.method=="GET":
        
        total_objs = len(models.payment_details.objects.all())
        total_education_cause_objs = 0
        total_women_empowerment_cause_objs = 0
        total_Health_cause_objs = 0
        total_livelyhood_cause_objs = 0 
        total_medical_cause_objs = 0
        total_other_cause_objs = 0

        for donation in models.payment_details.objects.all():
            if getattr(donation,"cause_for_donation") == "Education":
                total_education_cause_objs += 1
            elif getattr(donation,"cause_for_donation")== "Women Empowerment":
                total_women_empowerment_cause_objs += 1
            elif getattr(donation,"cause_for_donation") == "Livlihood":
                total_livelyhood_cause_objs += 1
            elif getattr(donation,"cause_for_donation") == "HealthCare":
                total_medical_cause_objs += 1
            elif getattr(donation,"cause_for_donation") == "Other":
                total_other_cause_objs += 1
        if total_objs==0:
            return Response({"Education": 0,"Woment Empowerment": 0,"Livelihood": 0,"Medcial camps": 0,"Other":0})
        education_cause_percentage = (total_education_cause_objs/total_objs)*100 
        women_empowerment_cause_percentage = (total_women_empowerment_cause_objs/total_objs)*100
        Health_cause_percentage = (total_Health_cause_objs/total_objs)*100
        livelyhood_cause_percentage = (total_livelyhood_cause_objs/total_objs)*100
        medical_cause_percentage = (total_medical_cause_objs/total_objs)*100
        other_cause_percentage = (total_other_cause_objs/total_objs)*100
        return Response({"Education": education_cause_percentage ,"Healthcare": Health_cause_percentage,"Woment Empowerment": women_empowerment_cause_percentage,"Livelihood": livelyhood_cause_percentage,"Medcial camps": medical_cause_percentage,"Other":other_cause_percentage})
                
class PaymentShortViews(GenericAPIView,ListModelMixin):
    
    queryset=models.payment_details.objects.all()
    serializer_class=serializers.PaymentShortserializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


