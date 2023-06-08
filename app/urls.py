
from django.urls import  path 
from app import views

urlpatterns = [ 
   path('', views.index,name='index'),
    path('login',views.handlelogin,name='handlelogin'),
    path('signup',views.handlesignup,name='handlesignup'),
]
    
   
