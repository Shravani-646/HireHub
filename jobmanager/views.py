from datetime import datetime
from django.shortcuts import render,HttpResponse,redirect
from jobmanager.forms import AuthorForm, JobPostForm
from jobmanager.models import JobPost,JobApplication,Skills,Author,Location
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def home_page(request):
    jobs = JobPost.objects.order_by('-date')
    author = None
    if request.user.is_authenticated:
        author = Author.objects.filter(user=request.user).first()
    if request.method == "POST":
        keyword = request.POST.get("search-keywords")
        jobs = JobPost.objects.select_related("location").filter(location__city__icontains=keyword).all()
        print(jobs)
        if not jobs.exists():
            jobs = JobPost.objects.filter(title__icontains=keyword)
        return render(request, 'jobmanager/job-list.html', {'jobs': jobs, 'search_keyword': keyword, 'author': author})
    return render(request, 'jobmanager/job-list.html', {'jobs': jobs,'request':request,'author':author})

def job_list(request):
    if request.method == "GET":
        queryset = JobPost.objects.all().order_by("-date")
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
    job_application.save()
    return job_application

@login_required(login_url="core:login-page")
def job_post(request,id):
    author = Author.objects.filter(pk=id).first()
    print(author)
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            skills_data = request.POST.get("skills").split(",")
            skills = [Skills.objects.get_or_create(name=name.strip())[0] for name in skills_data]
            location = get_location(request_obj=request)
            
            job_post = form.save(commit=False)
            job_post.author = author
            job_post.company = author.company
            job_post.location = location
            job_post.save()
            job_post.skills.set(skills)
            return redirect('/')  # Replace with your redirect URL
    form = JobPostForm()
    return render(request, 'jobmanager/create-jobpost.html', {'form': form})

def get_location(request_obj):
     city = request_obj.POST.get("city")
     state = request_obj.POST.get("state")
     country = request_obj.POST.get("country")
     zipcode = request_obj.POST.get("zipcode")
            
     # Create or get Location object
     location, created = Location.objects.get_or_create(
     city=city,
     state=state,
     country=country,
     zipcode=zipcode
            )
     return location

@login_required(login_url="core:login-page")
def profile(request,id):
    author = Author.objects.filter(user=request.user).first()
    user = request.user
    if request.method == "POST":
        user_form_data = {
            'first_name': request.POST.get("first_name"),
            'last_name': request.POST.get("last_name"),
            'username': request.POST.get("username"),
        }
        for key, value in user_form_data.items():
            setattr(user, key, value)
        
        user.save()

        if author is not None:
            author_form_data = {
                'company': request.POST.get("company"),
                'designation': request.POST.get("designation"),
            }

            for key, value in author_form_data.items():
                setattr(author, key, value)
            
            author.save()

        return redirect('jobmanager:profile-page', id=id)  
    
    return render(request,"jobmanager/profile.html",{'user':request.user,'author':author})

@login_required(login_url="core:login-page")
def view_posted_jobs(request,id):
    author = Author.objects.get(id=id)
    job_posts = author.jobpost_set.all()
    return render(request,"jobmanager/posted-jobs.html",{'posts':job_posts,'author':author})

@login_required(login_url="core:login-page")
def view_applications(request,id):
    print(id)
    job_post = JobPost.objects.get(id=id)
    applications = JobApplication.objects.filter(job_post=job_post)
    return render(request,"jobmanager/applications-list.html",{"applications":applications})

@login_required(login_url="core:login-page")
def application_detail(request,id):
    job_application = JobApplication.objects.get(id=id)
    skills = job_application.skills.all()
    return render(request,"jobmanager/application-detail.html",{'application':job_application,"skills":skills})


def author(request):
    is_author = Author.objects.filter(user=request.user).exists()
    if not is_author:
        form = AuthorForm()
        if request.method == "POST":
            form = AuthorForm(request.POST)
            if form.is_valid():
                author = form.save(commit=False)
                author.user = request.user
                author.save()
                return redirect("jobmanager:job-post",id=author.id)
        return render(request,"jobmanager/author.html",{'form':form})
    else:
        return redirect("/")