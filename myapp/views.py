from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    name = "Nawasan Wisitsingkhon"
    age = 21
    return render(request, 'about.html', {"name":name,"age": age})

def form(request):
    return render(request, 'form.html')