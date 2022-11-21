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
import urllib.request
from django.core.files.uploadedfile import InMemoryUploadedFile
        

class Genarate(GenericAPIView):
    queryset = certfication.objects.all()
    serializer_class = Gen
    
    def post(self,request,*args,**kwargs):
        event_id = request.data['event_id']
        event = Event.objects.get(id=event_id)
        user_id = request.session['current_user']
        user = User.objects.get(id=user_id)
        first_name = user.first_name
        last_name = user.last_name
        username = user.username
        #values for certificate
        name = str(first_name+" "+last_name).upper()
        event_name = str(event.event_name).upper()
        date = event.time.date().strftime("%d/%b/%Y")
        file_name = username+"_"+event_name
        
        urllib.request.urlretrieve('https://res.cloudinary.com/dcc8pmavm/image/upload/v1669013499/media/static_files/Certificate_template_uz1pc1.jpg',"certificate.jpg")
        img = Img.open("certificate.jpg")
        urllib.request.urlretrieve('https://res.cloudinary.com/dcc8pmavm/raw/upload/v1669015852/media/static_files/Arial_wwaooe.ttf',"Arial.ttf")
        font = ImageFont.truetype("Arial.ttf",70)
        #urllib.request.urlretrieve('https://res.cloudinary.com/dcc8pmavm/image/upload/v1669013499/media/static_files/Certificate_template_uz1pc1.jpg',"certificate.jpg")
        font2 = ImageFont.truetype("Arial.ttf",35)
        draw = ImageDraw.Draw(img)
        draw.text((740,700), name,(255,165,0),font=font)
        draw.text((375,1046), date,(0,0,0),font=font2)
        draw.text((1187,833), event_name,(0,140,0),font=font2)
        img.save("gg.jpg")
        image = img
        output = io.BytesIO()
        image.save(output, format='JPEG', quality=85)
        output.seek(0)
        new_pic= InMemoryUploadedFile(output, 'ImageField',
                                        file_name,
                                        'image/jpeg',
                                        sys.getsizeof(output), None)
        #values for create object of certificate
        event_name2 = event.event_name
        mentor_name = event.speaker_name
        date2 = event.time.date()
        
        crt = certfication.objects.create(
            event_name=event_name2,mentor_name=mentor_name,issue_date=date2,img=new_pic,status="Not Completed",user=user
        )
        try:
            os.remove(f"generate_certificate\\new certificates\\{file_name}.jpg")
        except FileNotFoundError:
            pass
        try:
            del request.session[str(username)]
        except KeyError:
            pass
        request.session[str(username)] = crt.id
        return Response("Certificate Genarated..!",201)
    
        
class Certify(GenericAPIView):
    queryset = certfication.objects.all()
    serializer_class = Gen
        
        
    def post(self,request):
        print(request.session)
        user_id = request.session['current_user']
        username = User.objects.get(id=user_id).username
        try:
            certificate_id = request.session[str(username)]    
        except KeyError:
            return Response("Certificate already Certifyed...!",200)    
        crt = certfication.objects.get(id=certificate_id)
        crt.status="Completed"
        crt.save()
        del request.session[str(username)]
        return Response("Certificate Certifyed...!",200)
        
        
