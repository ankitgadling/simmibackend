from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from certifications.models import certfication
from .serializers import CertSerializer , Gen,GenarateDonationSerializer,DonationDataSerializer
from events.models import Event
from django.contrib.auth.models import User
from PIL import Image as Img
from PIL import ImageDraw,ImageFont
from datetime import datetime,timedelta
import io
import os
import sys
import img2pdf
import urllib.request
from django.core.files import File
from django.contrib.auth.models import User
from .extras import create_session,get_session_by_key,delete_session_by_key,indian_currency_format
from django.core.files.uploadedfile import InMemoryUploadedFile
from Razorpay.models import Transactions
from .models import DonationCetificates
        

class Genarate(GenericAPIView):
    queryset = certfication.objects.all()
    serializer_class = Gen
    
    def post(self,request,*args,**kwargs):
        event_id = request.data['event_id']
        event = Event.objects.get(id=event_id)
        user_email = request.data['user_email']
        user = User.objects.get(username=user_email)
        first_name = user.first_name
        last_name = user.last_name
        username = user.username
        #values for certificate
        name = str(first_name+" "+last_name).upper()
        if len(name) > 19:
            name = first_name.upper()
        event_name = str(event.event_name).upper()
        date = event.time.date().strftime("%d-%b-%Y")
        file_name = username+"_"+event_name
        l1 ="simmifoundation sample text for genarate certification for event of simmifoundation" 
        l2 ="genarate certification for event of simmifoundation simmifoundation sample text for " 
        l3 ="certification for event of simmifoundation sample text for genarate " 
        urllib.request.urlretrieve('https://res.cloudinary.com/dcc8pmavm/image/upload/v1669456349/media/static_files/Picsart_22-11-26_15-18-01-572_gvdunr.jpg',"certificate.jpg")
        img = Img.open("certificate.jpg")
        urllib.request.urlretrieve('https://res.cloudinary.com/dcc8pmavm/raw/upload/v1669015852/media/static_files/Arial_wwaooe.ttf',"Arial.ttf")
        font = ImageFont.truetype("Arial.ttf",70)
        font2 = ImageFont.truetype("Arial.ttf",27)
        font3 = ImageFont.truetype("Arial.ttf",24)
        draw = ImageDraw.Draw(img)
        draw.text((733,490), name.center(19),(255,165,0),font=font)
        draw.text((700,608), l1,(105,105,105),font=font3)
        draw.text((700,648), l2,(105,105,105),font=font3)
        draw.text((700,688), l3,(105,105,105),font=font3)
        draw.text((950,730), "Completed On "+date,(0,0,0),font=font2)
        draw.text((950,730), "Completed On "+date,(0,0,0),font=font2)
        #draw.text((1187,833), event_name,(0,140,0),font=font2)
        img.save(f"{file_name}.jpg")
        image = Img.open(f"{file_name}.jpg")
        pdf_file = img2pdf.convert(image.filename)
        file = open(f"{file_name}.pdf","wb")
        file.write(pdf_file)
        file.close()
        image.close()
        pdf = File(open(f"{file_name}.pdf","rb"))
        # image = file
        # output = io.BytesIO()
        # image.save(output, format='pdf', quality=85)
        # output.seek(0)
        # new_pic= InMemoryUploadedFile(output, 'FileField',
        #                                 file_name,
        #                                 'pdf/txt',
        #                                 sys.getsizeof(output), None)
        #values for create object of certificate
        event_name2 = event.event_name
        mentor_name = event.speaker_name
        date2 = event.time.date()
        
        crt = certfication.objects.create(
            event_name=event_name2,mentor_name=mentor_name,issue_date=date2,img=pdf,status="Not Completed",user=user
        )
        pdf.close()
        delete_session_by_key(key=username)
        create_session(key=str(username), value=str(crt.id),expiry_date=datetime.now()+ timedelta(minutes=240))
        create_session(key=str(username+"currentevent"), value=str(event_id),expiry_date=datetime.now()+ timedelta(minutes=240))
        os.remove(f"{file_name}.jpg")
        os.remove(f"{file_name}.pdf")
        return Response("Certificate Genarated..!",201)

class Certify(GenericAPIView):
    queryset = certfication.objects.all()
    serializer_class = Gen
        
        
    def post(self,request):
        user_email = request.data['user_email']
        user = User.objects.get(username=user_email)
        username = user.username
        certificate_id = get_session_by_key(key=username)    
        event_id = get_session_by_key(key=username+"currentevent")    
        if certificate_id is None:
            return Response("Certificate already Certifyed...!",200)    
        crt = certfication.objects.get(id=certificate_id)
        crt.status="Completed"
        crt.save()
        delete_session_by_key(key=username)
        event = Event.objects.get(id=event_id)
        event.attendence += 1
        event.save()
        delete_session_by_key(key=username+"currentevent")
        return Response("Certificate Certifyed...!",200)
    
    
    
class Genarate_Donation_Certificate(GenericAPIView):
    queryset = Transactions.objects.all()
    serializer_class = GenarateDonationSerializer
    
    def post(self,request):
        email = request.data['email']
        for obj in self.get_queryset():
            trance_id = obj.id
            try:
                trance =DonationCetificates.objects.get(transactions_id=trance_id)
                pass
            except DonationCetificates.DoesNotExist:
                transaction = Transactions.objects.get(id=trance_id)
                date = transaction.date
                donar_name = transaction.user.first_name+transaction.user.last_name
                donar_name = str(donar_name).upper()
                donar_cause = transaction.cause
                cuases = ["Education","Livlihood","HealthCare","Women Empowerment"]
                if donar_cause not in cuases:
                    donar_cause = "To Simmifoundation"
                donar_ammount = indian_currency_format(int(transaction.amount))+" INR"
                file_name = transaction.user.username+str(trance_id)
                l2 ="genarate certification for event of simmifoundation simmifoundation sample text forgenarate certification for event " 
                l3 ="certification for event of simmifoundation sample text for genarate simmifoundation " 
                
                urllib.request.urlretrieve("https://res.cloudinary.com/dcc8pmavm/image/upload/v1669456371/media/static_files/Picsart_22-11-26_15-13-08-069_mlhepv.jpg","donation.jpg")
                img = Img.open("donation.jpg")
                #urllib.request.urlretrieve('https://res.cloudinary.com/dcc8pmavm/raw/upload/v1669015852/media/static_files/Arial_wwaooe.ttf',"Arial.ttf")
                font = ImageFont.truetype("Arial.ttf",27)
                font2 = ImageFont.truetype("Arial.ttf",25)
                draw = ImageDraw.Draw(img)
                draw.text((237,418), l2,(105,105,105),font=font2)
                draw.text((200,450), l3,(105,105,105),font=font2)
                draw.text((1418,168), str(trance_id)[7:len(str(trance_id))],(80,80,80),font=font2)
                draw.text((1460,547), date.strftime("%d-%b-%Y"),(80,80,80),font=font)
                draw.text((174,700), donar_name,(80,80,80),font=font)
                draw.text((174,825), donar_cause,(80,80,80),font=font)
                draw.text((174,960), donar_ammount,(80,80,80),font=font)
                img.save(f"{file_name}.jpg")
                
                image = Img.open(f"{file_name}.jpg")
                pdf_file = img2pdf.convert(image.filename)
                file = open(f"{file_name}.pdf","wb")
                file.write(pdf_file)
                file.close()
                image.close()
                pdf = File(open(f"{file_name}.pdf","rb"))
                
                trance = DonationCetificates.objects.create(transactions_id=trance_id,user=transaction.user,certificate=pdf)
                pdf.close()
                os.remove(f"{file_name}.jpg")
                os.remove(f"{file_name}.pdf")
        user = User.objects.get(username=email)
        data = DonationCetificates.objects.filter(user=user)
        if data is None:
            return Response(None,200)        
            
            
        
        