from django.urls import path
from jobmanager import views
urlpatterns = [
    path("",view=views.home_page,name="home-page"),
    path("jobs/",view=views.job_list,name="job-list"),
    path("jobs/<int:id>",view=views.job_detail,name="job-detail")
]