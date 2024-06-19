from django.shortcuts import render,HttpResponse,redirect
from core.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_page(request):
    if request.user.is_authenticated:
        return redirect("jobmanager:home-page")
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Account was created for {form.cleaned_data.get('username')}")
            return redirect("core:login-page")
    context = {'form':form}
    return render(request,template_name="core/register.html",context=context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect("jobmanager:home-page")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('jobmanager:home-page')
        else:
            messages.info(request,"Username or password is incorrect")
    return render(request,template_name="core/login.html")

def logout_user(request):
    logout(request)
    return redirect('core:login-page')