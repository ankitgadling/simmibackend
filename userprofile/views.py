from rest_framework import status
from .models import userprofile
from .serializers import userprofileserializers
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class List_users_pisc(generics.ListCreateAPIView):
    queryset = userprofile.objects.all()
    serializer_class = userprofileserializers


class profileDetail(generics.GenericAPIView):
    serializer_class = userprofileserializers

    def get_object(self, pk):
        try:
            return userprofile.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        detail = self.get_object(pk)
        serializer = userprofileserializers(detail)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        detail,_ = userprofile.objects.get_or_create(user=User.objects.get(pk=pk))
        serializer = userprofileserializers(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        detail = self.get_object(pk)
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
