from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == "POST":

        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname ')
        username = request.POST.get('username')
        email= request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2' )

        myuser = User.objects.create_user(username,password1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()

        return redirect('login/')
    return render(request,'register.html')

def login(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password1 = request.POST.get('password1')
        user=authenticate(username=username,password=password1)

        if user is not None:
           login(request,user)
           firstname = user.first_name
           return render(request, "index.html", {'firstname': firstname})


        else:
           return redirect('home')
    return render(request,'login.html')