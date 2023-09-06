from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt

from .forms import ClientQuestionForm
from django.contrib import messages


# Create your views here.
def homepage(request):
    return render(request, "home/page/home.html")


def signinpage(request):
    return render(request, "signin/page/signin.html")


def aboutpage(request):
    return render(request, "about/page/about.html")


def contactpage(request):
    form = ClientQuestionForm()
    context = {"form": form}

    return render(request, "contact/page/contact.html", context)


def contactform(request):
    if request.method == "POST":
        form = ClientQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sua mensagem foi enviada com sucesso")
            return redirect(reverse("core:contactpage"))
        else:
            messages.error(request, "Mensagem não enviada.")
            return redirect(reverse("core:contactpage"))
    else:
        messages.error(request, "Mensagem não enviada.")
        return redirect(reverse("core:contactpage"))


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
            "id": 2,
            "company": "Latam airline",
            "date": "04/08/2023",
            "route": "GRU/PNZ",
            "departure": "23:40",
            "arrival": "02:10",
            "value": "R$ 950,00",
            "quantity": "10",
        },
        {
            "id": 3,
            "company": "Latam airline",
            "date": "04/08/2023",
            "route": "GRU/PNZ",
            "departure": "23:40",
            "arrival": "02:10",
            "value": "R$ 950,00",
            "quantity": "10",
        },
        {
            "id": 4,
            "company": "Latam airline",
            "date": "04/08/2023",
            "route": "GRU/PNZ",
            "departure": "23:40",
            "arrival": "02:10",
            "value": "R$ 950,00",
            "quantity": "10",
        },
        {
            "id": 5,
            "company": "Latam airline",
            "date": "04/08/2023",
            "route": "GRU/PNZ",
            "departure": "23:40",
            "arrival": "02:10",
            "value": "R$ 950,00",
            "quantity": "10",
        },
    ]
    context = {"tickets": tickets}
    return render(request, "admin/pages/admin.html", context)


@csrf_exempt
@login_required(login_url="/signin", redirect_field_name="redirect_to")
def bookticketpage(request, slug):
    context = {
        "slug": slug,
        "ticket": {
            "id": 2,
            "company": "Latam airline",
            "date": "04/08/2023",
            "route": "GRU/PNZ",
            "departure_place": "GRU",
            "departure_time": "23:40",
            "destination_place": "PNZ",
            "destination_time": "02:10",
            "arrival_hour": "02:10",
            "arrival": "02:10",
            "value": "R$ 950,00",
            "quantity": "10",
        },
    }
    return render(request, "admin/pages/bookticket.html", context)
