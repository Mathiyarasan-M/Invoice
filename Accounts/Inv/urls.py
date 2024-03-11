from django.urls import path
from Inv import views

urlpatterns=[
    path('',views.index,name="index"),
    
]