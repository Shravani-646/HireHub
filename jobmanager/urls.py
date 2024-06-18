from django.urls import path
from jobmanager import views

app_name = 'jobmanager'
urlpatterns = [
    path("",view=views.home_page,name="home-page"),
    path("jobs/<int:id>",view=views.job_detail,name="job-detail"),
    path("jobs/<int:id>/application/",view=views.job_application,name="job-application")
]