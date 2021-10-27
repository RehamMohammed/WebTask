"""interviewtask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from charts import  views

urlpatterns = [
    #path('', views.get_page1),
    #path('fig2/', views.get_page2),
    #path('fig3/', views.get_page3),
    #path('fig4/', views.get_page4),
    
    #path('api' , views.ChartData1.as_view()),
    #path('fig2/api2' , views.ChartData2.as_view()),
    #path('fig3/api3' , views.ChartData3.as_view()), 
    #path('fig4/api4' , views.ChartData4.as_view()),
    path('', views.get_page5),
    path('api5' , views.ChartData5.as_view()),
    #path('api5' , views.ChartData5.as_view()),
]
