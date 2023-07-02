from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from myapp.models import Person

# Create your views here.

def index(request):
    all_person = Person.objects.all()
    return render(request, "index.html", {"users": all_person})

def about(request):
    name = "Nawasan Wisitsingkhon"
    age = 21
    return render(request, 'about.html', {"name":name,"age": age})

def form(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request, "บันทึกข้อมูลเรียบร้อย")
        return redirect('/')
    else:
        return render(request, 'form.html')

def edit(request, person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request, "อัพเดทข้อมูลเรียบร้อย")
        return redirect('/')

    person = Person.objects.get(id=person_id)
    return render(request, 'edit.html', {"person": person})