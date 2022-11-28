from django.urls import path, include
from carrers.views import GetJobs , GetJobsdetail,Jobapplyviewapi,ShortJobapplyviewapi,Jobapplyapi
urlpatterns = [
    path('',GetJobs.as_view()),
    path('filterjobs', GetJobs.as_view()),
    path('<pk>',GetJobsdetail.as_view()),
    path('apply/',Jobapplyapi.as_view()),
    path('admin_apply_view/',ShortJobapplyviewapi.as_view()),
    path('admin_apply_view/<pk>',Jobapplyviewapi.as_view()),
]
