from django.urls import path
from . import views
urlpatterns =[
path('', views.home, name='myApp-home'),
path('about', views.about, name='myApp-about'),
path('login', views.login, name='myApp-login'),
path('password', views.password, name='myApp-password'),
path('profile', views.profile, name='myApp-profile'),
path('reg', views.reg, name='myApp-reg'),
]
