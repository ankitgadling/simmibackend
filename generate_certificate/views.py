from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from certifications.models import certfication
from .serializers import CertSerializer , Gen
from events.models import Event
from django.contrib.auth.models import User
#import cv2
from PIL import Image as Img
import io
import os
import sys
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
        cert = cv2.imread('generate_certificate\\certificate.jpg')
        cv2.putText(cert,name,(770,750),cv2.FONT_HERSHEY_COMPLEX,2.0,(0,165,255),2,cv2.LINE_AA)
        cv2.putText(cert,date,(375,1076),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,0,0),1,cv2.LINE_AA)
        cv2.putText(cert,event_name,(1187,863),cv2.FONT_HERSHEY_COMPLEX,1.0,(255,140,0),1,cv2.LINE_AA)
        cv2.imwrite(f"generate_certificate\\new certificates\\{file_name}.jpg",cert)
        
        image = Img.open(f"generate_certificate\\new certificates\\{file_name}.jpg")
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
        print(dict(request.session))
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
        
        
