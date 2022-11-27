from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from certifications.models import certfication
from .serializers import CertSerializer , Gen
from events.models import Event
from django.contrib.auth.models import User
from PIL import Image as Img
from PIL import ImageDraw,ImageFont
import io
import os
import sys
import img2pdf
import urllib.request
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
        

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
        image = Img.open("certificate.jpg")
        pdf_file = img2pdf.convert(image.filename)
        file = open(f"{file_name}.pdf","wb")
        file.write(pdf_file)
        file.close()
        
        pdf = File(open(f"{file_name}.pdf"))
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
        print(type(pdf))
        print(pdf.name)
        return Response("DOne")
        
        crt = certfication.objects.create(
            event_name=event_name2,mentor_name=mentor_name,issue_date=date2,img=pdf,status="Not Completed",user=user
        )
        try:
            del request.session[str(username)]
        except KeyError:
            pass
        request.session[str(username)] = crt.id
        #request.session.session.set_expiry(10)
        return Response("Certificate Genarated..!",201)

class Certify(GenericAPIView):
    queryset = certfication.objects.all()
    serializer_class = Gen
        
        
    def post(self,request):
        print(request.session)
        user_email = request.data['user_email']
        username = User.objects.get(username=user_email).username
        try:
            certificate_id = request.session[str(username)]    
        except KeyError:
            return Response("Certificate already Certifyed...!",200)    
        crt = certfication.objects.get(id=certificate_id)
        crt.status="Completed"
        crt.save()
        del request.session[str(username)]
        return Response("Certificate Certifyed...!",200)
        
        
