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
    #path('fig5/api5' , views.ChartData5.as_view()),
]
