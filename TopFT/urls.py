"""
URL configuration for TopFT project.

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
from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('players/', players),
    path('clubs/', clubs),
    path('u20players/',u20players),
    path('d_c/<str:davlat>/',davlat_clublari),
    path('country_clubs/<str:club>/',c_clubs),
    path('h_m_transferlari',h_mavsum),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
