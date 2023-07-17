from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about/", views.aboutpage, name="aboutpage"),
    path("contact/", views.contactpage, name="contactpage"),
    path("signin/", views.signinpage, name="signin"),
    path("login/", views.loginview, name="login"),
    path("logout/", views.logoutuser, name="logout"),
    path("admin-management-page/", views.adminpage, name="adminpage"),
]
