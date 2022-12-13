from django.shortcuts import render
from Razorpay.models import Transactions,Subscription
from rest_framework.generics import ListAPIView,GenericAPIView
from rest_framework.response import Response
from .serializers import Userserializer,TransactionSerializer,SubscriptionSerializer
from wsgiref.util import FileWrapper
from fpdf import FPDF
from django.http import HttpResponse
from datetime import datetime
class admin_transactions_view(ListAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
        
class admin_subscription_view(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    
    
class Donwnload_Donations(GenericAPIView):
    serializer_class= TransactionSerializer
    queryset = Transactions.objects.all()
    
    def get(self,request):
        date_list = []
        cause_list = []
        donation_id_list = []
        ammount_list = []
        action_list = []
        for i in self.get_queryset():
            if i.is_paid:
                action = "Donated"
            else:
                action = "Not Donated"
            date_list.append(i.date)
            cause_list.append(i.cause)
            donation_id_list.append(i.id)
            ammount_list.append(i.amount)
            action_list.append(action)
        text_file_name = "Donation List_"+datetime.now().strftime("%d-%b-%y %I:%M")
        file_name = str(text_file_name)
        text = open("donation.txt","w+")
        text.write(f"Date                              Cause                       Donation_ID                          ammount             action\n")
        d = "_-"*65
        d2 = "-"*130
        text.write(d+"\n")
        for i in range(len(ammount_list)):
            text.write(f"{date_list[i].strftime('%d-%b-%y %I:%M')}               {cause_list[i].center(17)}               {donation_id_list[i]}               {ammount_list[i].center(7)}               {action_list[i].center(10)}\n")
            text.write(d2+"\n")
        text.close()
        d_file = open("donation.txt","rb")    
        # pdf = FPDF()
        # pdf.add_page()
        # pdf.set_font("Arial", size = 10)
        # for x in text:
        #     pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
        # pdf.output("mygfg.pdf")        
        response = HttpResponse(FileWrapper(d_file), content_type='application/text')
        response['Content-Disposition'] = f'attachment; filename={file_name+".txt"}'
        return response

        
class Donwnload_Subscriptions(GenericAPIView):
    serializer_class= SubscriptionSerializer()
    queryset = Subscription.objects.all()
    
    def get(self,request):
        date_list = []
        cause_list = []
        donation_id_list = []
        ammount_list = []
        period_list = []
        status_list = []
        for i in self.get_queryset():
            date_list.append(i.date)
            cause_list.append(i.cause)
            donation_id_list.append(i.id)
            ammount_list.append(i.amount)
            period_list.append(i.period)
            status_list.append(i.status)
        text_file_name = "Subscription List_"+datetime.now().strftime("%d-%b-%y %I:%M")
        file_name = str(text_file_name)
        text = open("subscription.txt","w+")
        text.write(f"Date                              Cause                       Donation_ID                        ammount              period                  status\n")
        d = "_-"*75
        d2 = "-"*150
        text.write(d+"\n")
        for i in range(len(ammount_list)):
            text.write(f"{date_list[i].strftime('%d-%b-%y %I:%M')}               {cause_list[i].center(17)}               {donation_id_list[i]}               {ammount_list[i].center(7)}               {period_list[i].center(10)}               {status_list[i]}\n")
            text.write(d2+"\n")
        text.close()
        d_file = open("subscription.txt","rb")    
        # pdf = FPDF()
        # pdf.add_page()
        # pdf.set_font("Arial", size = 10)
        # for x in text:
        #     pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
        # pdf.output("mygfg.pdf")        
        response = HttpResponse(FileWrapper(d_file), content_type='application/text')
        response['Content-Disposition'] = f'attachment; filename={file_name+".txt"}'
        return response