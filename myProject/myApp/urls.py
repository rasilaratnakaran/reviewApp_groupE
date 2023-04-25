from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
  
urlpatterns =[
path('', views.home, name='myApp-home'),
path('about', views.about, name='myApp-about'),
path('contact', views.contact, name='myApp-contact'),
path('login', views.login, name='myApp-login'),
path('password', views.password, name='myApp-password'),
path('profile', views.profile, name='myApp-profile'),
path('reg', views.reg, name='myApp-reg'),
 ]
 
urlpatterns += staticfiles_urlpatterns()
