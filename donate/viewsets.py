from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView,ListCreateAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin
from Razorpay.models import Transactions
from faq.serializer import SpendingMoneyPercentageSerializer
from faq.models import SpendingMoneyPercentage
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
        
        total_objs = Transactions.objects.all().count()
        total_education_cause_objs = Transactions.objects.filter(cause="Education").count()
        total_women_empowerment_cause_objs = Transactions.objects.filter(cause="Women Empowerment").count()
        total_Health_cause_objs = Transactions.objects.filter(cause="Livlihood").count()
        total_livelyhood_cause_objs = Transactions.objects.filter(cause="HealthCare").count() 
        total_other_cause_objs = Transactions.objects.filter(cause="Other").count()
        # for donation in models.payment_details.objects.all():
        #     if getattr(donation,"cause_for_donation") == "Education":
        #         total_education_cause_objs += 1
        #     elif getattr(donation,"cause_for_donation")== "Women Empowerment":
        #         total_women_empowerment_cause_objs += 1
        #     elif getattr(donation,"cause_for_donation") == "Livlihood":
        #         total_livelyhood_cause_objs += 1
        #     elif getattr(donation,"cause_for_donation") == "HealthCare":
        #         total_Health_cause_objs+= 1
        #     elif getattr(donation,"cause_for_donation") == "Other":
        #         total_other_cause_objs += 1
        
        education = (total_education_cause_objs/total_objs)*100
        healthcare = (total_Health_cause_objs/total_objs)*100
        livelyhood = (total_livelyhood_cause_objs/total_objs)*100
        women_empowerment = (total_women_empowerment_cause_objs/total_objs)*100
        other = (total_other_cause_objs/total_objs)*100
        
        education2 = int(education)
        healthcare2 = int(healthcare)
        livelyhood2 = int(livelyhood)
        women_empowerment2 = int(women_empowerment)
        other2 = int(other)
        total =education2+healthcare2+women_empowerment2+livelyhood2+other2
        val =100-total
        education ,healthcare,livelyhood,women_empowerment,other = education2,healthcare2,livelyhood2,women_empowerment2,other2+val
        # if total_objs==0:
        #     return Response({"Education": 0,"HealthCare":0,"Woment Empowerment": 0,"Livlihood": 0,"Other":0})
        # education_cause_percentage = (total_education_cause_objs/total_objs)*100 
        # women_empowerment_cause_percentage = (total_women_empowerment_cause_objs/total_objs)*100
        # Health_cause_percentage = (total_Health_cause_objs/total_objs)*100
        # livelyhood_cause_percentage = (total_livelyhood_cause_objs/total_objs)*100
        # other_cause_percentage = (total_other_cause_objs/total_objs)*100
        # return Response({"Education": education_cause_percentage ,"HealthCare": Health_cause_percentage,"Woment Empowerment": women_empowerment_cause_percentage,"Livlihood": livelyhood_cause_percentage,"Other":other_cause_percentage})
        return Response ([{"Content":{"Title":"Education","Value":education,"color":"#FFFF00"}},
                        {"Content":{"Title":"HealthCare","Value":healthcare,"color":"#FF0000"}},
                        {"Content":{"Title":"Livlihood","Value":livelyhood,"color":"#f5f5f5"}},
                        {"Content":{"Title":"Women Empowerment","Value":women_empowerment,"color":"#00FFFF"}} ,
                        {"Content":{"Title":"Other","Value":other,"color":"#641975"}} 
        ])


class NewPiechartPost(GenericAPIView):
    serializer_class = SpendingMoneyPercentageSerializer
    queryset = SpendingMoneyPercentage.objects.all()
    
    def get(self,request):
        try:
            latest_percantages = SpendingMoneyPercentage.objects.all().last()
            education = latest_percantages.education
            women_empowerment = latest_percantages.women_empowerment
            healthcare = latest_percantages.healthcare
            livelyhood = latest_percantages.livelyhood
            other = latest_percantages.other
            
            
            return Response ([{"Content":{"Title":"Education","Value":education,"color":"#FFFF00"}},
                            {"Content":{"Title":"HealthCare","Value":healthcare,"color":"#FF0000"}},
                            {"Content":{"Title":"Livlihood","Value":livelyhood,"color":"#f5f5f5"}},
                            {"Content":{"Title":"Women Empowerment","Value":women_empowerment,"color":"#00FFFF"}} ,
                            {"Content":{"Title":"Other","Value":other,"color":"#641975"}} 
            ])
        except AttributeError:
            return Response('There is no any latest percentages..!')
    def post(self, request):        
        education = request.data['education']
        healthcare = request.data['healthcare']
        livelyhood = request.data['livelyhood']
        women_empowerment = request.data['women_empowerment']
        other = request.data['other']
        cause_tuple = (int(education),int(healthcare),int(livelyhood),int(women_empowerment),int(other))
        if sum(cause_tuple) == 100:
            res = self.queryset.create(education=str(education),healthcare=str(healthcare),women_empowerment=str(women_empowerment),livelyhood=str(livelyhood),other=str(other))
            data = self.serializer_class(res).data
            return Response(data)
        else:
            return Response("Total percentage should be equal to 100",400)






class PaymentShortViews(GenericAPIView,ListModelMixin): 
    
    queryset=models.payment_details.objects.all()
    serializer_class=serializers.PaymentShortserializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


        