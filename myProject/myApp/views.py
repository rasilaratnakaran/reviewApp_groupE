from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'myApp/home.html')
def about(request):
    return render(request, 'myApp/about.html')
def login(request):
    return render(request, 'myApp/login.html')
def password(request):
    return render(request, 'myApp/password.html')
def profile(request):
    return render(request, 'myApp/profile.html')
def reg(request):
    return render(request, 'myApp/reg.html')

