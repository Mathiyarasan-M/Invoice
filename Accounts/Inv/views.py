from django.shortcuts import render
from Inv.models import  Users
# Create your views here.
def index(request):
    return render(request,'index.html')


