
from donate.models import STATUS
from institutional_aliance.serializers import Allianceserializers, ShortAlliance, copartnerserializers, copatnerlong, copatnershort
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view

class Alliance(GenericAPIView,ListModelMixin):
    queryset =alliance.objects.all()
    serializer_class = ShortAlliance
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


class DetailedAlliance(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset =alliance.objects.all()
    serializer_class = Allianceserializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


class AdminAlliance(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset =alliance.objects.all()
    serializer_class = Allianceserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class AdmineditAlliance(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset =alliance.objects.all()
    serializer_class = Allianceserializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class Copatnerapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Coparate.objects.all()
    serializer_class=copartnerserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


class AdminCopatnerapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Coparate.objects.all()
    serializer_class=copartnerserializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class AdmineditCopatnerapi(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=Coparate.objects.all()
    serializer_class=copatnerlong
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

# class upload():
#     @api_view(('POST',))
#     def post(request):
#         if request.method == "POST":
#             images = request.FILES.getlist('imgs')
#             for img in images:
#                 multi.objects.create(imgs = img)
#         images = multi.objects.all() 
#         return Response({"Object created"})

#     @api_view(('GET',))
#     def get(request,pk):

#         if request.method == "GET":
#             # try:
#                 image_objs = multi.objects.get(id=pk)
#                 images = []
#                 for img in image_objs:
#                     images.append("https://api.simmifoundation.tech"+img.image.url)
#                 print(images)