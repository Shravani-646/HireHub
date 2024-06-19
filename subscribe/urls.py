from django.urls import path
from . import views

app_name = "subscribe"
urlpatterns = [
    path("subscribe/",view=views.subscribe,name="subscribe"),
]
