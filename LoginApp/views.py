from django.shortcuts import render,redirect,HttpResponse
from .models import Regis 
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def loginpage(request):     
    if request.method == 'POST':
        email=request.POST['email']
        paswd=request.POST['password']
        try:
            l=Regis.objects.get(Email=email,Password=paswd)
            return redirect('/courses')
        except ObjectDoesNotExist:
            return HttpResponse('Invalid Username or Password')
            
        
    return render(request,"login.html")

def page(request):
    if request.method == 'POST':
        First_name = request.POST['first_name']
        Last_name = request.POST['last_name']
        email = request.POST['email']
        Pswd = request.POST['pswd']
        u=Regis(fname=First_name,lname=Last_name,Email=email,Password=Pswd)
        u.save()
        return redirect('/login')
    return render(request,"register.html")

def bstrap(request):
    return render(request,"index.html")

def secpage(request):
    return render(request,"Content.html")
