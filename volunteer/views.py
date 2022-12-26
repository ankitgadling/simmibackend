from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Volunteer
from datetime import datetime
import xlsxwriter
import os
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from .serializers import VolunteerSerializers
# Create your views here.


class excel_file_for_volunteer(GenericAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializers
    
    def get(self,request):
        file_name = 'Volunteer_list'+datetime.now().strftime('%b-%d-%Y')
        volrs = Volunteer.objects.all()
        excel_file = xlsxwriter.Workbook(file_name+".xlsx")
        sheet_name = "Volunteer_list_sheet"
        sheet_1 = excel_file.add_worksheet(sheet_name)
        bold = excel_file.add_format({'bold': True})
        sheet_1.set_column('A:A', 20)
        sheet_1.set_column('B:B', 40)
        sheet_1.set_column('C:C', 15)
        sheet_1.set_column('D:D', 20)
        sheet_1.set_column('E:E', 50)
        sheet_1.set_column('F:F', 20)
        sheet_1.set_column('G:G', 15)
        
        sheet_1.write("A1",'NAME',bold)
        sheet_1.write('B1','EMAIL',bold)
        sheet_1.write('C1','MOBILE NO',bold)
        sheet_1.write('D1','ADHAR NO',bold)
        sheet_1.write('E1','ADDRESS',bold)
        sheet_1.write('F1','DOB',bold)
        sheet_1.write('G1','BLOOD GROUP',bold)
        for index,item in enumerate(volrs) : #main loop

            name = item.name
            email = item.email
            ads = item.address
            b_g = item.blood_group
            dob = item.dob.strftime('%d-%b-%Y')
            no = item.phone
            
            try:
                a_no = int(item.aadhar_no)
            except:
                a_no = "None"
            
            sheet_1.write('A'+str(index+2),name)
            sheet_1.write('B'+str(index+2),email)
            sheet_1.write('C'+str(index+2),no)
            sheet_1.write('D'+str(index+2),a_no)
            sheet_1.write('E'+str(index+2),ads)
            sheet_1.write('F'+str(index+2),dob)
            sheet_1.write('G'+str(index+2),b_g)
                    
        excel_file.close()
        res = open(file_name+".xlsx",'rb')
        
        response = HttpResponse(FileWrapper(res), content_type='application/xlsx')
        response['Content-Disposition'] = f'attachment; filename={file_name+".xlsx"}'
        try:
            os.remove(file_name+".xlsx")
        except:
            pass
        return response        