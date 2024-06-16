from django.urls import path
from . import views
urlpatterns = [
    path("subscribe/",view=views.subscribe,name="subscribe")
]
