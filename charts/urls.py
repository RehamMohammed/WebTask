from django.contrib import admin
from django.urls import path
from charts import  views

urlpatterns = [
   
    path('', views.get_page1),

    path('fig2/', views.get_page2),
    path('fig3/', views.get_page3),
    path('fig4/', views.get_page4),
    path('api' , views.ChartData.as_view()),
    path('fig2' , views.get_fig2), 
    path('fig3' , views.get_fig3),
    path('fig4' , views.get_fig4),
    #path('api2' , views.ChartData2.as_view() ),
    
]
