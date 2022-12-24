from django.urls import path, include
from carrers.views import GetJobs , GetJobsdetail,Jobapplyviewapi,ShortJobapplyviewapi,Jobapplyapi,newjobapplyapi,excel_file_for_job_respones
urlpatterns = [
    path('',GetJobs.as_view()),
    path('filterjobs', GetJobs.as_view()),
    path('<pk>',GetJobsdetail.as_view()),
    path('apply/',Jobapplyapi.as_view()),
    path('create/',newjobapplyapi.as_view()),
    path('admin_apply_view/',ShortJobapplyviewapi.as_view()),
    path('admin_apply_view/<pk>',Jobapplyviewapi.as_view()),
    path('excel_file_for_job_respones/',excel_file_for_job_respones.as_view()),
]
