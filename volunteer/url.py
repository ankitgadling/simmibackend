from django.urls import path
from .views import excel_file_for_volunteer
urlpatterns = [
    path('excel_file/',excel_file_for_volunteer.as_view())
]