from django.shortcuts import render,HttpResponse
from .models import Kidsform, Adultform
# Create your views here.

def home(request):
    # return HttpResponse("Welcome")
    return render(request,'app/home.html')

def home(request):
    if request.method == "POST" and "below18" in request.POST:
        item = Kidsform()
        item.Name = request.POST['Name']
        item.Email = request.POST['Email']
        item.Hobbies = request.POST['Hobbies']
        item.DOB = request.POST['DOB']
        item.save()
        return HttpResponse("Submitted in Kids Record")
    if request.method == "POST" and "above18" in request.POST:
        item = Adultform()
        item.Name = request.POST['Name']
        item.Email = request.POST['Email']
        item.Hobbies = request.POST['Hobbies']
        item.DOB = request.POST['DOB']
        item.save()
        return HttpResponse("Submitted in Adultform Record")


    else:
        addrec_path='app/form.html'
        return render(request, addrec_path)