from django.shortcuts import render
from Razorpay.models import Transactions,Subscription
from rest_framework.generics import ListAPIView,GenericAPIView
from rest_framework.response import Response
from .serializers import Userserializer,TransactionSerializer,SubscriptionSerializer
from wsgiref.util import FileWrapper
from fpdf import FPDF
from django.http import HttpResponse
from generate_certificate.extras import indian_currency_format
from datetime import datetime
import xlsxwriter , os
class admin_transactions_view(GenericAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
    def get(self,request):
        transactions = Transactions.objects.all()
        data = []
        action = "Failed"
        for t in transactions:
            action = "Success"
            amt = indian_currency_format(int(t.amount))
            amt = str(amt)+" "+t.currency
            obj = {
                "date" : t.date.strftime("%d-%b-%Y"),
                "cause" : t.cause,
                "donation_id":t.id,
                "ammount": amt,
                "action":action,
            }
            data.append(obj)
        return Response(data)        
class admin_subscription_view(GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    
    def get(self,request):
        subscriptions = Subscription.objects.all()
        data = []
        for s in subscriptions:
            amt = indian_currency_format(int(s.amount))
            amt = str(amt)+" "+s.currency
            obj = {
                "date" : s.date.strftime("%d-%b-%Y"),
                "cause" : s.cause,
                "donation_id":s.id,
                "ammount": amt,
                "period" : s.period,
                "status":s.status,
                }
            data.append(obj)
        return Response(data)        
                
            
    
    
class Donwnload_Donations(GenericAPIView):
    serializer_class= TransactionSerializer
    queryset = Transactions.objects.all()
    
    def get(self,request):
        file_name = 'Donation_history_'+datetime.now().strftime('%b-%d-%Y')
        data = Transactions.objects.all()
        excel_file = xlsxwriter.Workbook(file_name+".xlsx")

        sheet_1 = excel_file.add_worksheet('Donation')

        bold = excel_file.add_format({'bold': True})

        sheet_1.set_column('A:A', 15)
        sheet_1.set_column('B:B', 20)
        sheet_1.set_column('C:C', 19)
        sheet_1.set_column('D:D', 20)
        sheet_1.set_column('E:E', 10)
        sheet_1.set_column('F:F', 10)

        sheet_1.write("A1",'DATE',bold)
        sheet_1.write('B1','NAME',bold)
        sheet_1.write('C1','CAUSE',bold)
        sheet_1.write('D1','TRANSACTION ID',bold)
        sheet_1.write('E1','AMOUNT',bold)
        sheet_1.write('F1','STATUS',bold)

        for index , item in enumerate(data):
            name = item.user.first_name+" "+item.user.last_name
            date = item.date.strftime('%d-%b-%Y')
            cause = item.cause
            id = item.id
            amt = item.amount+" "+item.currency
            sts = "Failed"
            if item.is_paid:
                sts = 'Success'
            
            sheet_1.write('A'+str(index+2),date)
            sheet_1.write('B'+str(index+2),name)
            sheet_1.write('C'+str(index+2),cause)
            sheet_1.write('D'+str(index+2),id)
            sheet_1.write('E'+str(index+2),amt)
            sheet_1.write('F'+str(index+2),sts)
        excel_file.close()
        res = open(file_name+".xlsx",'rb')
        
        response = HttpResponse(FileWrapper(res), content_type='application/xlsx')
        response['Content-Disposition'] = f'attachment; filename={file_name+".xlsx"}'
        res.close()
        try:
            os.remove(file_name+".xlsx")
        except:
            pass
        return response

        
class Donwnload_Subscriptions(GenericAPIView):
    serializer_class= SubscriptionSerializer()
    queryset = Subscription.objects.all()
    
    def get(self,request):
        file_name = 'Subscription_history_'+datetime.now().strftime('%b-%d-%Y')
        data = Subscription.objects.all()
        excel_file = xlsxwriter.Workbook(file_name+".xlsx")

        sheet_1 = excel_file.add_worksheet('Subscription')

        bold = excel_file.add_format({'bold': True})

        sheet_1.set_column('A:A', 15)
        sheet_1.set_column('B:B', 20)
        sheet_1.set_column('C:C', 19)
        sheet_1.set_column('D:D', 20)
        sheet_1.set_column('E:E', 10)
        sheet_1.set_column('F:F', 10)

        sheet_1.write("A1",'DATE',bold)
        sheet_1.write('B1','NAME',bold)
        sheet_1.write('C1','CAUSE',bold)
        sheet_1.write('D1','TRANSACTION ID',bold)
        sheet_1.write('E1','AMOUNT',bold)
        sheet_1.write('F1','STATUS',bold)

        for index , item in enumerate(data):
            name = item.user.first_name+" "+item.user.last_name
            date = item.date.strftime('%d-%b-%Y')
            cause = item.cause
            id = item.id
            amt = item.amount+" "+item.currency
            sts = item.status
            sheet_1.write('A'+str(index+2),date)
            sheet_1.write('B'+str(index+2),name)
            sheet_1.write('C'+str(index+2),cause)
            sheet_1.write('D'+str(index+2),id)
            sheet_1.write('E'+str(index+2),amt)
            sheet_1.write('F'+str(index+2),sts)
        excel_file.close()
        res = open(file_name+".xlsx",'rb')
        
        response = HttpResponse(FileWrapper(res), content_type='application/xlsx')
        response['Content-Disposition'] = f'attachment; filename={file_name+".xlsx"}'
        res.close()
        try:
            os.remove(file_name+".xlsx")
        except:
            pass
        return response