from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home, name = ''), # Doesn't matter ki ky naam de rhe ho bas views.home aur aur views m function ka naam same hona chiye  
    path('add' , views.add , name = 'add')                                  
                                    
]
