from datetime import date
from django.shortcuts import render
import pandas as pd
import csv
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from collections import OrderedDict

# Create your views here.
#users_df = pd.read_csv('train_users_2.csv')
#print (users_df.head(5))

'''def readfile(filepath):
    global rows , columns , data , my_file ,missing_values

    my_file = pd.read_csv(filepath , sep=',', engine= 'python') 
    data = pd.DataFrame(data = my_file, index=None)
    print(data)
    rows = len(data.axes[0])
    columns = len(data.axes[1])
    missing_signs = ['?','0','--','-unknown-']
    null_data = data[data.isnull().any(axis=1)]
    missing_values = len(null_data)'''



datafile = pd.read_csv(r"C:\Users\Reham\interviewtask\charts\train_users_2.csv")
dataf = pd.DataFrame(data = datafile, index=None)

dict = {}
def get_data(col):
    affCol = set(dataf[col].values)
    for i in affCol:
        dict[i] = (dataf[col].value_counts()[i]/len(dataf[col].values)) * 100

    return dict


def get_page1(request):
    return render(request, 'index.html')

def get_page2(request):
    return render(request, 'figure2.html')

def get_page3(request):
    return render(request, 'figure3.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self,request , format = None):
        dict = get_data('affiliate_channel')
        d_descending = OrderedDict(sorted(dict.items(), key=lambda kv: kv[1], reverse=True))
        keys = []
        values = []
        keys.append(d_descending.keys())
        values.append(d_descending.values())
        labels = keys[0]
        chartLabel = "affiliate_channel"
        chartdata = values[0]
        data ={
                        "labels":labels,
                        "chartLabel":chartLabel,
                        "chartdata":chartdata,
                }
        return Response(data)
'''class ChartData2(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self,request , format = None):
        dict = get_data('affiliate_provider')
        d_descending = OrderedDict(sorted(dict.items(), key=lambda kv: kv[1], reverse=True))
        keys = []
        values = []
        keys.append(d_descending.keys())
        values.append(d_descending.values())
        labels = keys[0]
        chartLabel = "affiliate_provider"
        chartdata = values[0]
        data2 ={
                        "labels":labels,
                        "chartLabel":chartLabel,
                        "chartdata":chartdata,
                }
        return Response(data2)'''
def get_fig2(request):
        dict = get_data('affiliate_provider')
        d_descending = OrderedDict(sorted(dict.items(), key=lambda kv: kv[1], reverse=True))
        keys = []
        values = []
        keys.append(d_descending.keys())
        values.append(d_descending.values())
        labels = keys[0]
        chartLabel = "affiliate_provider"
        chartdata = values[0]
        data ={
                        "labels":labels,
                        "chartLabel":chartLabel,
                        "chartdata":chartdata,
                }
        return Response(data)

def get_fig3(request):
        dict = get_data('country_destination')
        sortednames=sorted(dict.keys(), key=lambda x:x.lower())
        keys = []
        values = []
        for i in sortednames:
           keys.append(i)
           values.append(dict[i])
        
        labels = keys[0]
        chartLabel = "country_destination"
        chartdata = values[0]
        data ={
                        "labels":labels,
                        "chartLabel":chartLabel,
                        "chartdata":chartdata,
                }
        return Response(data)

def get_fig4(request):
        dict = get_data('country_destination')
        sortednames=sorted(dict.keys(), key=lambda x:x.lower())
        keys = []
        values = []
        for i in sortednames:
           keys.append(i)
           values.append(dict[i])
        
        labels = keys[0]
        chartLabel = "country_destination"
        chartdata = values[0]
        data ={
                        "labels":labels,
                        "chartLabel":chartLabel,
                        "chartdata":chartdata,
                }
        return Response(data)