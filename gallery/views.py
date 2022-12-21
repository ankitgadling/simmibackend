from gallery.serializers import Galleryserializers, AdminSerializer
from gallery.models import *
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

# class GalleryAdmin(CreateAPIView):
#     queryset =Gallerytable.objects.all()
#     serializer_class = AdminSerializer

#     def post(self,request, *args, **kwargs):
#         title = request.data['title']
#         admin = "admin@gmail.com"
#         date = request.data['date']
#         content = request.data['content']
#         category = request.data['category']
#         user = User.objects.get(username=admin)
#         admin = user.first_name
#         Gallerytable.objects.create(title=title, photo=photo, photo2=photo2, photo3=photo3,admin=admin, date=date, content=content, category=category)
#         print(admin)
#         return Response("Objects created!!")



class GalleryView(GenericAPIView):
    queryset =Gallerytable.objects.all()
    serializer_class = Galleryserializers

    def get(self, request):
        gallery_objs = Gallerytable.objects.all()
        print(gallery_objs)
        result = []
        for obj in gallery_objs:
            galler_image = GalleryImages.objects.filter(gallery_id=obj.id)
            print(galler_image, type(galler_image))
            images =[]
            for img in galler_image:
                images.append("https://simmibackend.pythonanywhere.com"+img.image.url)
                
            data = {
                "id": obj.id,
                "title": obj.title,
                "admin": obj.admin,
                "date": obj.date.strftime('%d-%b-%Y'),
                "content": obj.content,
                "category": obj.category,
                "images": images
            }
            result.append(data)

        return Response(result)

    def post(self, request):
        images_obj = request.data.getlist('images')
        title = request.data['title']
        admin = "admin@gmail.com"
        date = request.data['date']
        content = request.data['content']
        category = request.data['category']
        # user = User.objects.get(username=admin)
        # admin = "harsh"
        gallery_table_obj = Gallerytable.objects.create(title=title,admin=admin, date=date, content=content, category=category)
        print(admin)

        id = gallery_table_obj.id
        
        for img in images_obj:
            GalleryImages.objects.create(gallery_id=id, image=img, title=title)
        
        return Response("Success!!", 200)

class GalleryDetailView(GenericAPIView):
    queryset =Gallerytable.objects.all()
    serializer_class = Galleryserializers


    def get(self, request, pk):
        try:
            gallery_obj = Gallerytable.objects.get(id=pk)
            gallery_images = GalleryImages.objects.filter(gallery_id=gallery_obj.id)
            images=[]
            for img in gallery_images:
                images.append("https://simmibackend.pythonanywhere.com"+img.image.url)
            print(gallery_images)
            print(images)
            data = {
                "id": gallery_obj.id,
                "title": gallery_obj.title,
                "admin": gallery_obj.admin,
                "date": gallery_obj.date.strftime('%d-%b-%Y'),
                "content": gallery_obj.content,
                "category": gallery_obj.category,
                "images": images
                }
            return Response(data)
        except Exception as e:
            return Response({"error": "Detail Not Found!"})

    def put(self, request, pk=None):
        gallery_obj = Gallerytable.objects.get(id=pk)
        images_obj = request.data.getlist('images')
        title = request.data['title']
        admin = "admin@gmail.com"
        date = request.data['date']
        content = request.data['content']
        category = request.data['category']

        gallery_obj.title = title
        gallery_obj.date = date
        gallery_obj.content = content
        gallery_obj.category = category
        gallery_obj.save()

        images_old = GalleryImages.objects.filter(gallery_id=pk)
        images_old.delete()

        for img in images_obj:
            GalleryImages.objects.create(gallery_id=pk, image=img, title=title)

        return Response("Details Updated!!!")

    def delete(self, request, pk):
        gallery_obj = Gallerytable.objects.get(id=pk)
        gallery_images = GalleryImages.objects.filter(gallery_id=pk)

        gallery_obj.delete()
        gallery_images.delete()

        return Response("Deleted!!")