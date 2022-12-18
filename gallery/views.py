from gallery.serializers import Galleryserializers, AdminSerializer
from gallery.models import Gallerytable
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from django.contrib.auth.models import User
# get api for website without permissions
class Galleryapi(GenericAPIView,ListModelMixin):
    queryset =Gallerytable.objects.all()
    serializer_class = Galleryserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
        
#for admins
class Galleryapidetail(RetrieveUpdateDestroyAPIView):
    queryset =Gallerytable.objects.all()
    serializer_class = Galleryserializers

    def get(self,request,*args,**kwargs):
     return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class GalleryAdmin(CreateAPIView):
    queryset =Gallerytable.objects.all()
    serializer_class = AdminSerializer

    def post(self,request, *args, **kwargs):
        title = request.data['title']
        admin = "admin@gmail.com"
        photo = request.data['photo']
        photo2 = request.data['photo2']
        photo3 = request.data['photo3']
        date = request.data['date']
        content = request.data['content']
        category = request.data['category']
        user = User.objects.get(username=admin)
        admin = user.first_name
        Gallerytable.objects.create(title=title, photo=photo, photo2=photo2, photo3=photo3,admin=admin, date=date, content=content, category=category)
        print(admin)
        return Response("Objects created!!")

