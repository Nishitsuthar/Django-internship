from myapp.models import Student
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Student


def homepageview(request):
    return render(request, "home.html")


def aboutpageview(request):
    return render(request, "about.html")


def contactpageview(request):
    return render(request, "contact.html")


def formpageview(request):
    return render(request, "form.html")


def processpageview(request):
    print("welcome")
    print(request.method)
    print(request.POST)
    a = int(request.POST["num1"])
    b = int(request.POST["num2"])
    c = a + b
    print(c)
    return render(request, "sum.html", {"mya": a, "myb": b, "mysum": c})


def signuppageview(request):
    return render(request, "signup.html")


def userdataview(request):
    print("user fulfilled form")
    print(request.method)
    print(request.POST)
    fname = request.POST["first_name"]
    lname = request.POST["last_name"]
    email = request.POST["email"]
    sub = request.POST["subject"]
    mobile = int(request.POST["phone"])
    return render(
        request,
        "userdata.html",
        {
            "my_fname": fname,
            "my_lname": lname,
            "myemail": email,
            "sub": sub,
            "my_mobile": mobile,
        },
    )


class student_list(ListView):
    model = Student
    template_name = "slist.html"


# Create your views here.
