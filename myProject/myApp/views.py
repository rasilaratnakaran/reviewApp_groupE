from django.shortcuts import render
from django.http import HttpResponse
from .models import user
 
from django.template import loader
 
# Create your views here.
def home(request):
        return render(request, 'myApp/home.html')
def about(request):
        return render(request, 'myApp/about.html')
def contact(request):
        return render(request, 'myApp/contact.html')
def login(request):
        return render(request, 'myApp/login.html')
def password(request):
        return render(request, 'myApp/password.html')
def profile(request):
        return render(request, 'myApp/profile.html')
def reg(request):
        return render(request, 'myApp/reg.html')
def reg(request):
            if request.method == 'POST':
             if request.POST.get('FirstName') and request.POST.get('LastName'):
                post=user()
                post.FirstName= request.POST.get('FirstName')
                post.LastName= request.POST.get('LastName')
                post.DOB= request.POST.get('DOB')
                post.Phone= request.POST.get('Phone')
                post.email= request.POST.get('email')
                post.Address= request.POST.get('Address')
                post.City= request.POST.get('City')
                post.Country= request.POST.get('Country')
                post.ZipCode= request.POST.get('ZipCode')
                post.Password= request.POST.get('Password')
                    
                post.save()
                return render(request, 'myApp/reg.html')
            else:
                return render(request,'myApp/reg.html')

       

               
        



