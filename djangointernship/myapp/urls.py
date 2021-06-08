from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepageview, name="home"),
    path("about", views.aboutpageview, name="about"),
    path("contact", views.contactpageview, name="contact"),
    path("form", views.formpageview, name="form"),
    path("process", views.processpageview, name="process"),
    path("signup", views.signuppageview, name="signup"),
    path("Udata", views.userdataview, name="userdata"),
    path("slist", views.student_list.as_view(), name="slist"),
]
