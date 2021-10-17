from django.contrib import admin
from django.urls import path
from charts import  views

urlpatterns = [
   
    path('', views.get_page1),
   
    path('fig2/', views.get_page2),
    path('fig3/', views.get_page3),
    path('api' , views.ChartData.as_view()),
    path('api2' , views.get_fig2),
    path('api3' , views.get_fig3),
    #path('api2' , views.ChartData2.as_view() ),
    
]
