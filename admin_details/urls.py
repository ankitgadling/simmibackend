from django.urls import path
from admin_details.views import *




urlpatterns = [
    path('details',AdmimDetailsView.as_view()),
    path('details/<pk>',AdmimDetailsView2.as_view()),
    path('invite_admin',InviteAdminView.as_view()),
    path('add_admin/<str:url_path>',AddAdminView.as_view()),
    path('send_email',EmailSendView.as_view()),
]
