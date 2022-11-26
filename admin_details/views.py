from django.shortcuts import render
from datetime import datetime
from rest_framework.generics import GenericAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from .serializers import AdminSerializer,AdminAddSerializer,EmailSendSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from account.models import SimmiUserDetails
#from knox.auth import TokenAuthentication
from admin_logs.custome_auth import AdminIsInTheSession
from admin_logs.custome_permissions import SuperAdminPermission
from admin_logs.password_genarate import genarate_password,get_name_from_email
from django.core.mail import EmailMessage
from datetime import datetime,timedelta
from django.conf import settings
from generate_certificate.extras import create_session,get_session_by_key,delete_session_by_key
#from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.

class AdmimDetailsView(GenericAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminSerializer
    # authentication_classes = [AdminIsInTheSession]
    # permission_classes = [SuperAdminPermission]
    def get(self,request,*args,**kwargs):
        listadmins = []
        Admins = User.objects.filter(is_staff=True,is_superuser=False)    
        for admin in Admins:
            try:
                admindetails = SimmiUserDetails.objects.get(user=admin)
                try:
                    adminprofile = admindetails.profile.url
                except ValueError:
                    adminprofile = "https://tse4.mm.bing.net/th?id=OIP.nFy1XtLSOTDIfte9BdtvQwHaHa&pid=Api&P=0"
                if adminprofile is None:
                    adminprofile = "https://tse4.mm.bing.net/th?id=OIP.nFy1XtLSOTDIfte9BdtvQwHaHa&pid=Api&P=0"
            except SimmiUserDetails.DoesNotExist:
                adminprofile = "https://tse4.mm.bing.net/th?id=OIP.nFy1XtLSOTDIfte9BdtvQwHaHa&pid=Api&P=0"
            listadmins.append({"admin_id":admin.id,"name":str(admin.first_name)+" "+str(admin.last_name),"email":admin.username})
        return Response(listadmins)
        
class InviteAdminView(GenericAPIView):
    serializer_class = AdminAddSerializer
    queryset = User.objects.all()
    def post(self,request):
        invite_email = request.data['email']
        try:
            user = User.objects.get(username=invite_email)
            return Response("Sorry this email was used in client/admin side..!",404)
        except User.DoesNotExist :
            pass
        name = get_name_from_email(invite_email)
        html = f"""
        <html>
    <head>
        <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css' integrity='sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi' crossorigin='anonymous'>
    
    <style>
        
        </style>
    </head>
    <body style="font-size: 20px">
        <h2 style="color: orange;font-family:inherit;text-align:center">Admin Invitation From SimmiFoundation</h2>
    <center>
        <p style="color: gray">
            Hello  {name}, we are inviting you as admin for our admin panel<br> site you can accept by clicking below button
        </p>
        </center>
        <center>
        <br><br>
        <a style="background-color: orange;
            box-shadow:3px 3px 2px 2px grey;
            border-radius: 10px;
            font-family:'arial';
            text-decoration-line: none;
            color: lightcyan;
            padding: 0.5%" href="https://simmibackendtest.herokuapp.com/api/admin_details/add_admin/{name}" class="mybtn">Accept Invitation</a>
        </center>
        <br><br>
    </body>
</html>

        """
        email = EmailMessage("Invitation",html,settings.EMAIL_HOST_USER,[invite_email])
        email.content_subtype = "html"
        res =  email.send()
        key = name+"_email"
        now = datetime.now()
        if res:
            session = create_session(key=key, value=invite_email, created_date=now, expiry_date=now+timedelta(days=2))    
        else:
            return Response("Something went wrong..!",400)
        return Response({"data":"Invitation was sent to this email "+"'"+invite_email+"'"})


class AddAdminView(GenericAPIView):
    serializer_class = AdminAddSerializer
    queryset = User.objects.all()
    
    def get(self,request,url_path=None):
        email = get_session_by_key(key=url_path+"_email")
        if email is None:
            return Response("I am sorry you are soo late...!",200)
            
        password = genarate_password()
        name = get_name_from_email(email=email)
            
        html = f"""
                <html>
    <head>
        <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css' integrity='sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi' crossorigin='anonymous'>
    
    <style>
        
        </style>
    </head>
    <body style="font-size: 20px">
        <h2 style="color: orange;font-family:inherit;text-align:center">Admin Invitation From SimmiFoundation</h2>
    <center>
        <p style="color: gray">
            Hello {name} , Thanks for accepting our invitation you can log in 
            by using below credentials 
        </p>
        </center>
        <h5 style="margin-left: 36%;color: black;display:block">Username : <span style="color:orange" >{email}</span></h5>
        <h5 style="margin-left: 36%;color: black;display:block">Password : {password}</h5>
        <center>
        <br>
        <p style="color: gray"><a href="https://simmireactjsadmin.netlify.app/" target="_blank" style="color: orange" >Click here</a> to open our Admin panel.</p><br><br>
        <span style="float: right;font-size: 15px;margin-right: 1%">Thank you..</span> 
        </center>
    </body>
</html>            
            """
        admin = User.objects.create_user(username=email,password=password,is_staff=True)
        email = EmailMessage("Invited..!",html,settings.EMAIL_HOST_USER,[email])
        email.content_subtype = "html"
        res =  email.send()
        delete_session_by_key(key=url_path+"_email")
        return Response("Thanks for accepting our invitation, Now you are our admin. Your credentials was sent to your email, Thank you..!")
            
        
        
class AdmimDetailsView2(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = AdminSerializer

    def get(self,request,pk=None,*args,**kwargs):
        try:
            admin = User.objects.get(id=pk,is_staff=True,is_superuser=False)    
            return Response({"admin_id":admin.id,"name":str(admin.first_name)+" "+str(admin.last_name)})
        except User.DoesNotExist:
            return Response({"msg":"Admin Not Found....!"},404)
    def delete(self,request,pk=None,*args,**kwargs):
        try:
            admin = User.objects.get(id=pk)
            admin.is_staff = False
            admin.save()    
            return Response("Admin removed..!")
        except User.DoesNotExist:
            return Response({"msg":"Admin permission removed to this user..!"})
        
        
class EmailSendView(GenericAPIView):
    serializer_class = EmailSendSerializer
    queryset = User.objects.all()
    
    def post(self,request):
        email = request.data['email']
        subject = request.data['subject']
        message = request.data['message']
        file_var = request.data['file']
        html = f"<p style='text-align: center;color: gray;font-size: 20px'>{message}</p>"
        email = EmailMessage(subject, html, settings.EMAIL_HOST_USER, [email])
        email.content_subtype = "html"
        email.attach(file_var.name, file_var.read(), file_var.content_type)
        try:
            res = email.send()
        except:
            return Response("That attached file size is soo big..!",401)
        if res:
            return Response("Email was sent successfully!",201)
        else:
            return Response("something wrong!",401)
    
    
    
    
        
        
        
        
