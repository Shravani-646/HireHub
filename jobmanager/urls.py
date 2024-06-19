from django.urls import path
from jobmanager import views

app_name = 'jobmanager'
urlpatterns = [
    path("",view=views.home_page,name="home-page"),
    path("jobs/<int:id>",view=views.job_detail,name="job-detail"),
    path("jobs/<int:id>/application/",view=views.job_application,name="job-application"),
    path("authors/<int:id>/",views.view_posted_jobs,name="posted-jobs"),
    path("authors/<int:id>/jobposts/",views.job_post,name="job-post"),
    path("profiles/<int:id>/",views.profile,name="profile-page"),
    path("jobpost/<int:id>/applications",views.view_applications,name="applications-list"),
    path("applications/<int:id>/",views.application_detail,name="application-detail"),
    path("authors/",views.author,name="author-page"),
    path('authors/<int:id>/jobpost/<int:jobpost_id>/', views.delete_job_post, name='delete-job-post'),
]