from telnetlib import STATUS
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from carrers.models import *
from .serializers import Job, Jobserializer,Jobapplyserializer,ShortJobapplyserializer,newjobapplyserializer
from rest_framework.response import Response
# Create your views here. 


# carrers apis to get the data of jobs
class GetJobs(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Jobs.objects.all()
    serializer_class = Jobserializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs) 
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs) 
        
class GetJobsdetail(GenericAPIView,DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin):
    queryset = Jobs.objects.all()
    serializer_class = Jobserializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs) 
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs) 
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs) 


class Jobapplyapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = jobappliedbyuse.objects.all()
    serializer_class = Jobapplyserializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs) 
class newjobapplyapi(GenericAPIView):
    queryset=jobappliedbyuse.objects.all()
    serializer_class=newjobapplyserializer
    def post(self,request,*args,**kwargs):
        how_you_heared_us= request.data["how_you_heared_us"]
        jobid=request.data["jobid"]
        country=request.data["country"]
        first_name=request.data["first_name"]
        last_name=request.data["last_name"]
        adhar_no=request.data["adhar_no"]
        applied_on=request.data["applied_on"]
        address_lane=request.data["address_lane"]
        city=request.data["city"]
        postal_code=request.data["postal_code"]
        email=request.data["email"]
        country_code=request.data["country_code"]
        mobile_number=request.data["mobile_number"]
        jobid=request.data["jobid"]
        resume=request.data["resume"]
        job=Jobs.objects.get(id=jobid)
        jobappliedbyuse.objects.create(how_you_heared_us=how_you_heared_us,jobid=jobid,country=country,first_name=first_name,last_name=last_name,adhar_no=adhar_no,applied_on=applied_on,address_lane=address_lane,city=city,postal_code=postal_code,email=email,country_code=country_code,mobile_number=mobile_number,resume=resume,job=job)
        return Response("object created",200)



class ShortJobapplyviewapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=jobappliedbyuse.objects.all()
    serializer_class = ShortJobapplyserializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs) 



class Jobapplyviewapi(GenericAPIView,DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin):
    queryset = jobappliedbyuse.objects.all()
    serializer_class = Jobapplyserializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs) 
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)