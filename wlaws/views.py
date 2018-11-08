from django.shortcuts import render

def privacy(request):
    return render(request,'privacy.html')

def terms(request):
    return render(request,'terms.html')

def disclaimer(request):
    return render(request,'disclaimer.html')
