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
import xlsxwriter
from wsgiref.util import FileWrapper
from datetime import datetime
import os
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



#new api
class excel_file_for_job_respones(GenericAPIView):
    queryset = jobappliedbyuse.objects.all()
    serializer_class = Jobapplyserializer
    
    def get(self,request):
        file_name = 'Jobsapplieds_'+datetime.now().strftime('%b-%d-%Y')
        jobs = Jobs.objects.all()
        excel_file = xlsxwriter.Workbook(file_name+".xlsx")
        for job in jobs: #main loop
            sheet_name = job.title+"_"+str(job.id)
            bold = excel_file.add_format({'bold': True})
            applies = jobappliedbyuse.objects.filter(job=job)
            if len(applies) > 0 :
                data = applies
                sheet_1 = excel_file.add_worksheet(sheet_name)

                sheet_1.set_column('A:A', 15)
                sheet_1.set_column('B:B', 15)
                sheet_1.set_column('C:C', 30)
                sheet_1.set_column('D:D', 15)
                sheet_1.set_column('E:E', 15)
                sheet_1.set_column('F:F', 15)
                sheet_1.set_column('G:G', 15)
                sheet_1.set_column('H:H', 80)

                sheet_1.write("A1",'FIRST NAME',bold)
                sheet_1.write('B1','LAST NAME',bold)
                sheet_1.write('C1','EMAIL',bold)
                sheet_1.write('D1','COUNTRY',bold)
                sheet_1.write('E1','CITY',bold)
                sheet_1.write('F1','APPLIED ON',bold)
                sheet_1.write('G1','MOBILE NO',bold)
                sheet_1.write('H1','RESUME LINK',bold)

                for index , item in enumerate(data):
                    fn = item.first_name
                    ln = item.last_name
                    email = item.email
                    country = item.country
                    city = item.city
                    applied_on = item.applied_on.strftime('%d-%b-%Y')
                    try:
                        no = int(item.mobile_number)
                    except:
                        no = "None"
                    #link = "http://localhost:8000"+item.resume.url
                    link = "https://simmibackend.pythonanywhere.com"+item.resume.url
                    
                    sheet_1.write('A'+str(index+2),fn)
                    sheet_1.write('B'+str(index+2),ln)
                    sheet_1.write('C'+str(index+2),email)
                    sheet_1.write('D'+str(index+2),country)
                    sheet_1.write('E'+str(index+2),city)
                    sheet_1.write('F'+str(index+2),applied_on)
                    sheet_1.write('G'+str(index+2),no)
                    sheet_1.write('H'+str(index+2),link)
                    
        
        excel_file.close()
        res = open(file_name+".xlsx",'rb')
        
        response = HttpResponse(FileWrapper(res), content_type='application/xlsx')
        response['Content-Disposition'] = f'attachment; filename={file_name+".xlsx"}'
        try:
            os.remove(file_name+".xlsx")
        except:
            pass
        return response        