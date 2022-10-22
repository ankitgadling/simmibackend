from django.urls import path, include
from carrers.views import GetJobs , GetJobsdetail
urlpatterns = [
    path('',GetJobs.as_view()),
    path('filterjobs', GetJobs.as_view()),
    path('<pk>',GetJobsdetail.as_view())
]
