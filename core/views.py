from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def homepage(request):
    return render(request, "home/page/home.html")


def signinpage(request):
    return render(request, "signin/page/signin.html")


def aboutpage(request):
    return render(request, "about/page/about.html")


def contactpage(request):
    return render(request, "contact/page/contact.html")


@csrf_exempt
def loginview(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # check if the user is in the database
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # if the user is in the database
            login(request, user)
            user = User.objects.get(username=username)
            if user.is_staff:
                # if the user is staff
                messages.success(request, "Welcome, " + username)
                return redirect(reverse("core:adminpage"))
            # redirect to the admin page
            return redirect(reverse("core:homepage"))
        else:
            # if the user is not in the database
            messages.error(request, "Invalid username or password")
            return redirect(reverse("core:signin"))


def logoutuser(request):
    logout(request)
    return redirect(reverse("core:homepage"))


# Create a view to admin page with security and safety
@login_required(login_url="/signin", redirect_field_name="redirect_to")
@staff_member_required(login_url="/signin", redirect_field_name="redirect_to")
def adminpage(request):
    tickets = [
        {
            "company": "Company 1",
            "date": "01/01/2020",
            "route": "Route 1",
            "departure": "Departure 1",
            "arrival": "Arrival 1",
            "value": "Value 1",
            "quantity": "Quantity 1",
        },
        {
            "company": "Company 1",
            "date": "01/01/2020",
            "route": "Route 1",
            "departure": "Departure 1",
            "arrival": "Arrival 1",
            "value": "Value 1",
            "quantity": "Quantity 1",
        },
        {
            "company": "Company 1",
            "date": "01/01/2020",
            "route": "Route 1",
            "departure": "Departure 1",
            "arrival": "Arrival 1",
            "value": "Value 1",
            "quantity": "Quantity 1",
        },
        {
            "company": "Company 1",
            "date": "01/01/2020",
            "route": "Route 1",
            "departure": "Departure 1",
            "arrival": "Arrival 1",
            "value": "Value 1",
            "quantity": "Quantity 1",
        },
    ]
    return render(request, "admin/page/admin.html", context={"tickets": tickets})
