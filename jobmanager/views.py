from datetime import datetime
from django.shortcuts import render,HttpResponse,redirect
from jobmanager.models import JobPost,JobApplication,Skills,Author
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page(request):
    jobs = JobPost.objects.all()
    is_author = False
    if request.user.is_authenticated:
        is_author = Author.objects.filter(user=request.user).exists
    return render(request, 'jobmanager/job-list.html', {'jobs': jobs,'request':request,'is_author':is_author})

def job_list(request):
    if request.method == "GET":
        queryset = JobPost.objects.all()
        return render(request=request,template_name="jobmanager/job-list.html",context={"jobs":queryset})

def job_detail(request,id):
    if request.method == "GET":
        job = JobPost.objects.prefetch_related("skills").get(id=id)
        skills = job.skills.all()
        return render(request,template_name="jobmanager/job-detail.html",context={'job':job,'skills':skills})
    
@login_required(login_url="core:login-page")
def job_application(request,id):
    application_exists = JobApplication.objects.filter(user=request.user).exists()
    if not application_exists:
        if request.method=="POST":
            skills_data = request.POST.get("skills").split(",")
            skills = [Skills.objects.get_or_create(name=name.strip())[0] for name in skills_data]
            job_application = get_application_data(request_obj=request,id=id)
            job_application.save()
            job_application.skills.set(skills)
            return redirect("jobmanager:job-detail",id=id)
        return render(request,"jobmanager/create-application.html",{'user':request.user})
    else:
        return HttpResponse("<h1>You have already submitted your form. Go Back</h1>")


def get_application_data(request_obj,id):
    education = request_obj.POST.get('education')
    available_to_start_str = request_obj.POST.get('available_to_start')
    available_to_start = datetime.strptime(available_to_start_str, '%m-%d-%Y').date()
    job_post = JobPost.objects.get(id=id)
    resume_file = request_obj.FILES.get('resume')
    # Create JobApplication object
    job_application = JobApplication(
            user=request_obj.user,
            job_post=job_post,
            education=education,
            available_to_start=available_to_start,
            city=request_obj.POST.get('city'),
            state=request_obj.POST.get('state'),
            country=request_obj.POST.get('country'),
            resume = resume_file
        )
    return job_application