from operator import truediv
from django.shortcuts import render
from .models import Contact
from rest_framework.response import Response
from .serializers import ContactSerializer
from rest_framework.decorators import api_view


@api_view(['POST', "GET"])
def contact(request):
    if request.method == "POST":
        try:
            data = request.data
            serializer = ContactSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "Status": 200,
                    "data": serializer.data
                })
            return Response({
                    "Status": False,
                    "message": "Invalid data!",
                    "data": serializer.errors
                })

        except Exception as e:
            return Response({
                "status":"something went wrong"
            })
    if request.method == "GET":
        obj = Contact.objects.all()
        serializer = ContactSerializer(obj, many=True)
        return Response(serializer.data)