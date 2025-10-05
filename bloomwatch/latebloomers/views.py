from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def superbloom2022(request):
    return render(request, "superbloom2022.html")
def superbloom2023(request):
    return render(request, "superbloom2023.html")
