"""Wcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import whome.views
import wwork.views
import wservice.views
import waboutus.views
import wcontact.views
import wlaws.views

urlpatterns = [
    path('wdevnetadmin/', admin.site.urls),
    path('',whome.views.home,name='home'),
    path('aboutus/',waboutus.views.aboutus,name='aboutus'),
    path('workwithus/',wwork.views.work,name='workwithus'),
    path('services/',wservice.views.services,name='service'),
    path('contactus/',wcontact.views.contact,name='contactus'),
    path('privacy/',wlaws.views.privacy,name='privacy'),
    path('disclaimer/',wlaws.views.disclaimer,name='disclaimer'),
    path('termsofservice/',wlaws.views.terms,name='terms'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
