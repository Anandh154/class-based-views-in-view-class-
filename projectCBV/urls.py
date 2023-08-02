"""
URL configuration for projectCBV project.

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
from app.views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv_str/',fbv_str,name='fbv_str'),
    path('CbvStr/',CbvStr.as_view(),name='CbvStr'),
    path('CbvView/',CbvView.as_view(),name='CbvView'),
    path('CbvTemp/',CbvTemp.as_view(),name='CbvTemp'),
    path('Data_render/',Data_render.as_view(),name='Data_render'),
    path('anandh/',TemplateView.as_view(template_name='anandh.html'),name='anandh'),
    path('Cbv_Mf/',Cbv_Mf.as_view(),name='Cbv_Mf'),
    path('fbv_mf/',fbv_mf,name='fbv_mf'),
]
