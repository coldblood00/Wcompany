from django.shortcuts import render

from .models import about

def aboutus(request):
    waboutus=about.objects
    return render(request,'aboutus.html',{'waboutus':waboutus})
