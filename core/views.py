from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, "home/page/home.html")


def signinpage(request):
    return render(request, "signin/page/signin.html")
