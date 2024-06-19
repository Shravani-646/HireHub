from django.shortcuts import render,redirect,HttpResponse
from subscribe.forms import SubscriberForm
from subscribe.models import Subscriber

# Create your views here.
def subscribe(request):
    subscriber_form = SubscriberForm()
    if request.method == "POST":
        subscriber_form = SubscriberForm(request.POST)
        if subscriber_form.is_valid():
            subscriber_form.save()
            return HttpResponse("<h1>Details are saved and you will receive our newsletters</h1><p>Go Back to <a href='http://127.0.0.1:8000/'>Home Page</a></p>")
        else:
            return render(request,template_name="subscribe/subscribe.html",context={'form':subscriber_form})
    return render(request,template_name="subscribe/subscribe.html",context={'form':subscriber_form}) 