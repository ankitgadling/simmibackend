from django.shortcuts import render
# from .models import donate_form
# from rest_framework.response import Response
# from .serializers import ContactSerializer, DonateFormSerializer
# from rest_framework.decorators import api_view

# # Create your views here.



# @api_view(['POST', "GET"])
# def donate(request):
#     if request.method == "POST":
#         try:
#             data = request.data
#             serializer = donate_form(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({
#                     "Status": 200,
#                     "data": serializer.data
#                 })
#             return Response({
#                     "Status": False,
#                     "message": "Invalid data!",
#                     "data": serializer.errors
#                 })

#         except Exception as e:
#             return Response({
#                 "status":"something went wrong"
#             })
#     if request.method == "GET":
#         obj = donate_form.objects.all()
#         serializer = DonateFormSerializer(obj, many=True)
#         return Response(serializer.data)