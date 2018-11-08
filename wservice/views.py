from django.shortcuts import render
from .models import service

def services(request):
    wservice=service.objects
    return render(request,'service.html',{'wservice':wservice})
