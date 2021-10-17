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

def get_page4(request):
    return render(request, 'figure4.html')

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
    dff = set(dataf["signup_app"].values)
  
    new_df = dataf[['signup_app','age']].dropna()
    #print(new_df.groupby('signup_app')['age'].apply(list))
    Web = []
    Android = []
    Moweb = []
    Ios = []

    Android = new_df.groupby('signup_app')['age'].apply(list)[0]
    Moweb = new_df.groupby('signup_app')['age'].apply(list)[1]
    Web = new_df.groupby('signup_app')['age'].apply(list)[2]
    Ios = new_df.groupby('signup_app')['age'].apply(list)[3]
    def no_of_users(Web):
        l1 = []
        range1 = 0
        range2 = 0
        range3 = 0
        range4 = 0
        range5 = 0
        range6 = 0
        range7 = 0
        for i in Web:
            if i >= 18 and i< 20:
                range1 += 1
            elif i >= 20 and i <30:
                range2 += 1
            elif i >= 30 and i <40:
                range3 += 1
            elif i >= 40 and i <50:
                range4 += 1
            elif i >= 50 and i <60:
                range5 += 1
            elif i >= 60 and i <70:
                range6 += 1
            elif i >= 70: 
                range7 += 1
        l1.append(range1)
        l1.append(range2)
        l1.append(range3)
        l1.append(range4)
        l1.append(range5)
        l1.append(range6)
        l1.append(range7)
        return l1

    dict2 = {}

    dict2['Android'] = no_of_users(Android)
    dict2['Moweb'] = no_of_users(Moweb)
    dict2['Web'] = no_of_users(Web)
    dict2['iOS'] = no_of_users(Ios)
    keys2 = []
    keys2.append(dict2.keys())
    values2 = []
    values2.append(dict2.values())
    
    labels = keys2[0]
    chartLabel = "signup app"
    chartdata = values2[0]
    data ={
            "labels":labels,
            "chartLabel":chartLabel,
            "chartdata":chartdata,
        }
    return Response(data)