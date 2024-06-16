from django.shortcuts import render,HttpResponse,redirect
from jobmanager.models import JobPost

# Create your views here.
def home_page(request):
    return HttpResponse("<h1>Hello World</h1>")

def job_list(request):
    if request.method == "GET":
        queryset = JobPost.objects.all()
        return render(request=request,template_name="jobmanager/job-list.html",context={"jobs":queryset})

def job_detail(request,id):
    if request.method == "GET":
        job = JobPost.objects.get(id=id)
        return render(request,template_name="jobmanager/job-detail.html",context={'job':job})