from django.urls import path
from . import views

app_name = "core"


urlpatterns = [
    path("signup/",view=views.register_page,name="signup-page"),
    path("login/",view=views.login_page,name="login-page"),
    path("logout/",view=views.logout_user,name="logout-page"),

]