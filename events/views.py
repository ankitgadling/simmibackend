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
                    print("cccccccccccccc",c_c2,e_c2)
                    status = "Ongoing"
                else:
                    status = "Upcoming"
            ev = {
                "id":event.id,
                "name":event.event_name,
                "event_descriptn":event.event_description,
                "speaker_name":event.speaker_name,
                "Perk_of_attendig_event":event.Perk_of_attendig_event,
                "category":event.category,
                "time":event.time.strftime('%d-%b-%Y %I:%M %p'),
                "duration":event.duration,
                "status":status,
                "image_1":event.image_1.url,
                "image_2":event.image_2.url,
                "image_3":event.image_3.url,
            }
            event_list.append(ev)
        return Response(event_list)
#for admin

class EventCreateView(CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Event.objects.all()
    serializer_class = EventSerializer2
    
    
    # def post(self,request,*args,**kwargs):
    #     return self.create(request,*args,**kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
        # event_name = request.data['event_name']
        # try:
        #     event = Event.objects.get(event_name=event_name)
        #     return Response("Event is already exists with this name.. ",401)
        # except Event.DoesNotExist:
        #     pass
        # speaker_name = request.data.get('speaker_name')
        # event_description = request.data['event_description']
        # Perk_of_attendig_event = request.data['perk of attending event']
        # category = request.data['category']
        # time = request.data['time']
        # image_1 = request.data['image_1']
        # place = request.data['place']
        # image_2 = request.data['image_2']
        # image_3 = request.data['image_3']
        
        # Event.objects.create(event_name=event_name,event_description=event_description,speaker_name=speaker_name,Perk_of_attendig_event=Perk_of_attendig_event
        #                     ,category=category,time=time,image_1=image_1,image_2=image_2,image_3=image_3,place=place)
        # if speaker_name is not None:
        #     try:
        #         speaker = Speaker.objects.get(name=speaker_name)
        #         speaker.event = event_name
        #         speaker.save()
        #     except Speaker.DoesNotExist:
        #         pass            


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
            
        ev = {
                "id":event.id,
                "name":event.event_name,
                "event_descriptn":event.event_description,
                "speaker_name":event.speaker_name,
                "Perk_of_attendig_event":event.Perk_of_attendig_event,
                "category":event.category,
                "time":event.time.strftime('%d-%b-%Y %I:%M %p'),
                "duration":event.duration,
                "status":status,
                "image_1":event.image_1.url,
                "image_2":event.image_2.url,
                "image_3":event.image_3.url,
            }
        return Response(ev)
        
        
        
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


