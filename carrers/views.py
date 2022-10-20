from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from carrers.models import Jobs
from .serializers import Jobserializer
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