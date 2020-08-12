

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View


def home_page(request):
    return render(request,'home.html')

@login_required
def customer(request):

    return render(request,'customer.html')

def logoutview(request):
    return render(request,'logout.html')

def signup(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/au')
    else:
        form=UserCreationForm()
    return render(request,'registration.html',{'form':form})

def myhomepage(request):
    return render(request,'myhome.html')
def a(req):
    return HttpResponse("<h1>WELCOME TO MY HOME</h1>")

def b(req):
    return HttpResponse("<h1>WELCOME TO MY messages</h1>")

def c(req):
    return HttpResponse("<h1>WELCOME TO MYprofile</h1>")





# Create your views here.
