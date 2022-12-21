from django.shortcuts import render
from rest_framework.generics import GenericAPIView,CreateAPIView
from rest_framework.mixins import CreateModelMixin,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.response import Response
from .models import *
from datetime import date
from .serializers import EventSerializer,EventSerializer2
from speaker.models import Speaker
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.


class AllEvents(GenericAPIView,ListModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    def get(self,request,*args,**kwargs):
        event_list = []
        events = Event.objects.all()
        for event in events:
            status = "Upcoming"
            formatt = ('%d/%b/%Y')
            formatt2 = ('%I:%M')
            current_time =datetime.now().date().strftime(formatt)
            event_time = event.time.date().strftime(formatt)
            
            current_time2 =datetime.now().time().strftime(formatt2)
            event_time2 = event.time.time().strftime(formatt2)
            
            c_c = datetime.strptime(current_time, formatt)
            e_c = datetime.strptime(event_time, formatt)
            
            c_c2 = datetime.strptime(current_time2, formatt2)
            e_c2 = datetime.strptime(event_time2, formatt2)
            
            if c_c > e_c:
                status = "Ended"
            elif c_c == e_c:
                if c_c2 >= e_c2:
                    status = "Ongoing"
                else:
                    status = "Upcoming"
            try:
                ev = {
                    "id":event.id,
                    "name":event.event_name,
                    "event_descriptn":event.event_description,
                    "speaker_name":event.speaker_name,
                    "Perk_of_attendig_event":event.Perk_of_attendig_event,
                    "category":event.category,
                    "time":event.time.strftime('%d-%b-%Y %I:%M %p'),
                    "duration":event.duration,
                    'venue':event.venue,
                    'online_link':event.online_link,
                    "status":status,
                    # "image_1":event.image_1.url,
                    # "image_2":event.image_2.url,
                    # "image_3":event.image_3.url,
                    "image_1":"https://simmibackend.pythonanywhere.com"+event.image_1.url,
                    }
            except ValueError:
                ev = {
                    "id":event.id,
                    "name":event.event_name,
                    "event_descriptn":event.event_description,
                    "speaker_name":event.speaker_name,
                    "Perk_of_attendig_event":event.Perk_of_attendig_event,
                    "category":event.category,
                    "time":event.time.strftime('%d-%b-%Y %I:%M %p'),
                    "duration":event.duration,
                    'venue':event.venue,
                    'online_link':event.online_link,
                    "status":status,
                    "image_1":None,
                    # "image_2":None,
                    # "image_3":None,
                }
            
            event_list.append(ev)
        return Response(event_list)
#for admin

class EventCreateView(CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Event.objects.all()
    serializer_class = EventSerializer2
    
class EventModifyView(UpdateModelMixin,GenericAPIView,RetrieveModelMixin,DestroyModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def get(self,request,pk=None,*args,**kwargs):
        try:
            event = Event.objects.get(id=pk)
        except Event.DoesNotExist:
            return Response("Event Not Found...!",404)
        status = "Upcoming"
        formatt = ('%d/%b/%Y')
        current_time =datetime.now().date().strftime(formatt)
        event_time = event.time.date().strftime(formatt)
        c_c = datetime.strptime(current_time, formatt)
        e_c = datetime.strptime(event_time, formatt)
        if c_c > e_c:
            status = "Ended"
        elif c_c == e_c:
            status = "Ongoing"
        
        try:    
            ev = {
                    "id":event.id,
                    "name":event.event_name,
                    "event_descriptn":event.event_description,
                    "speaker_name":event.speaker_name,
                    "Perk_of_attendig_event":event.Perk_of_attendig_event,
                    "category":event.category,
                    "time":event.time.strftime('%d-%b-%Y %I:%M %p'),
                    "duration":event.duration,
                    'venue':event.venue,
                    "status":status,
                    # "image_1":event.image_1.url,
                    # "image_2":event.image_2.url,
                    # "image_3":event.image_3.url,
                    "image_1":"https://simmibackend.pythonanywhere.com"+event.image_1.url,
                    # "image_2":"https://simmibackend.pythonanywhere.com"+event.image_2.url,
                    # "image_3":"https://simmibackend.pythonanywhere.com"+event.image_3.url,
                }
        except:
            ev = {
                    "id":event.id,
                    "name":event.event_name,
                    "event_descriptn":event.event_description,
                    "speaker_name":event.speaker_name,
                    "Perk_of_attendig_event":event.Perk_of_attendig_event,
                    "category":event.category,
                    "time":event.time.strftime('%d-%b-%Y %I:%M %p'),
                    "duration":event.duration,
                    'venue':event.venue,
                    "status":status,
                    "image_1":None,
                    # "image_2":None,
                    # "image_3":None,
            }
        return Response(ev)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


