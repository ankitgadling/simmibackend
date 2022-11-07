from django.shortcuts import render
from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import CreateModelMixin,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin
from rest_framework.response import Response
from .models import *
from .serializers import EventSerializer,ExtraImagesSerializer
# Create your views here.


class AllEvents(GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    def get(self,request,*args,**kwargs):
        event_list = []
        events = Event.objects.all()
        for event in events:
            extra_images = []
            ex_im = EventImages.objects.filter(event=event)
            for ex in ex_im:
                extra_images.append(ex.image.url)
            ev = {
                "name":event.event_name,
                "event_descriptn":event.event_description,
                "speaker_name":event.speaker_name,
                "Perk_of_attendig_event":event.Perk_of_attendig_event,
                "category":event.category,
                "time":event.time,
                "image":event.image.url,
                "extra_images":extra_images
            }
            event_list.append(ev)
        return Response(event_list)
    
#for admin

class EventCreateView(CreateModelMixin,GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EventModifyView(UpdateModelMixin,GenericAPIView,RetrieveModelMixin,DestroyModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def get(self,request,pk=None,*args,**kwargs):
        try:
            event = Event.objects.get(id=pk)
        except Event.DoesNotExist:
            return Response("Event Not Found...!",404)
        extra_images = []
        ex_im = EventImages.objects.filter(event=event)
        for ex in ex_im:
            extra_images.append(ex.image.url)
        ev = {
                "name":event.event_name,
                "event_descriptn":event.event_description,
                "speaker_name":event.speaker_name,
                "Perk_of_attendig_event":event.Perk_of_attendig_event,
                "category":event.category,
                "time":event.time,
                "image":event.image.url,
                "extra_images":extra_images
            }
        return Response(ev)
        
        
        
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
