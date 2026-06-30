from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse("This page is about me!!!!!!!!!!!")


def gotoGoogle(request):
    return redirect("https://google.com")


def teams(request):
    return render(request, "teams.html")