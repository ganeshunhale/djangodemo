"""
URL configuration for Djangonew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import *
from Djangonew import views

urlpatterns = [
    path('admin/', admin.site.urls ,name="admin"),
    path('', views.homepage,name="home"),
    path('about-us/', views.aboutUs , name="about" ),
    path('contact-us/', views.conatctUs , name="contact" ),
    # path('pages/custom_bingo.html', views.custom_bingo),
    path('get_custom_bingo', views.get_custom_bingo, name='get_custom_bingo'),
    path ('Conversion_FileUpload/',Conversion_FileUploadviews.as_view(),name='Conversion_FileUpload'),
]
