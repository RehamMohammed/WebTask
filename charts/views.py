from datetime import date
from django.shortcuts import render
import pandas as pd
import csv
from django.views.generic import View
from pandas.core import series
from rest_framework.views import APIView
from rest_framework.response import Response
from collections import OrderedDict


# Create your views here.


datafile = pd.read_csv(r"C:\Users\Reham\interviewtask\charts\train_users_2.csv")
dataf = pd.DataFrame(data = datafile, index=None)

def get_affiliate_channel_percentage(col):
    dict = {}
    affCol = set(dataf[col].values)
    for i in affCol:
        dict[i] = (dataf[col].value_counts()[i]/len(dataf[col].values)) * 100

    return dict
def get_samples_per_class(col):
    dict = {}
    country = set(dataf[col].values)
    for i in country:
        dict[i]  = dataf[col].value_counts()[i]
    return dict

def get_dates(col):

    dataf['date_account_created'] = pd.to_datetime(dataf.date_account_created, infer_datetime_format = True)
    dataf.sort_values(by = 'date_account_created', ascending = True, inplace = True)

    TimeStamps = dataf['date_account_created'].unique()
    dates = []
    for i in TimeStamps:
        t = str(pd.to_datetime(i).date())
        dates.append(t)

    return dates

def get_page1(request):
    return render(request, 'index.html')

def get_page2(request):
    return render(request, 'figure2.html')

def get_page3(request):
    return render(request, 'figure3.html')

def get_page4(request):
    return render(request, 'figure4.html')

def get_page5(request):
    return render(request, 'figure5.html')  

def get_page6(request):
    return render(request, 'figure6.html')  

def get_page7(request):
    return render(request, 'figure7.html')   

#Affiliate channel percentage
class ChartData1(APIView):
   
    def get(self,request , format = None):
        dict = get_affiliate_channel_percentage('affiliate_channel')
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

#Affiliate channel provider percentage
class ChartData2(APIView):
    def get(self,request , format = None):
        dict = get_affiliate_channel_percentage('affiliate_provider')
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

#Samples per class 
class ChartData3(APIView):
    def get(self,request , format = None):
            dict = get_samples_per_class('country_destination')
            
            sortednames=sorted(dict.keys(), key=lambda x:x.lower())
            keyss = []
            valuess = []
            for i in sortednames:
                keyss.append(i)
                valuess.append(dict[i])
            
            labels = keyss
            chartLabel = "country_destination"
            chartdata = valuess
            data ={
                            "labels":labels,
                            "chartLabel":chartLabel,
                            "chartdata":chartdata,
                    }
            return Response(data)

#Sign up dist per page
class ChartData4(APIView):
    def get(self,request , format = None):
        #dff = set(dataf["signup_app"].values)
    
        new_df = dataf[['signup_app','age']].dropna()
        #print(new_df.groupby('signup_app')['age'].apply(list))
        Web = []
        Android = []
        Moweb = []
        Ios = []

        #get all ages for each app in list
        Android = new_df.groupby('signup_app')['age'].apply(list)[0]
        Moweb = new_df.groupby('signup_app')['age'].apply(list)[1]
        Web = new_df.groupby('signup_app')['age'].apply(list)[2]
        Ios = new_df.groupby('signup_app')['age'].apply(list)[3]
        
        #categorize each list based on age ranges and add all in list for each app
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
            l1 = [range1,range2,range3,range4,range5,range6,range7]
            return l1

        apps_dict = {}
        
        apps_dict['Android'] = no_of_users(Android)
        apps_dict['Moweb'] = no_of_users(Moweb)
        apps_dict['Web'] = no_of_users(Web)
        apps_dict['iOS'] = no_of_users(Ios)
        keys2 = []
        keys2.append(apps_dict.keys())
        values2 = []
        A = no_of_users(Android)
        M = no_of_users(Moweb)
        W = no_of_users(Web)
        I = no_of_users(Ios)
 
        #each list contains number of users with specific range of age who use the 4 apps
        l =  [A[0],M[0],W[0],I[0]]
        l2 = [A[1],M[1],W[1],I[1]]
        l3 = [A[2],M[2],W[2],I[2]]
        l4 = [A[3],M[3],W[3],I[3]]
        l5 = [A[4],M[4],W[4],I[4]]
        l6 = [A[5],M[5],W[5],I[5]]
        l7 = [A[6],M[6],W[6],I[6]]

        
        labels = keys2[0]
        chartLabel = ["(id, 18-20)" , "(id, 20-30)", "(id, 30-40)", "(id, 40-50)", "(id, 50-60)", "(id, 60-70)", "(id, 70+)"]
        chartdata = [l,l2,l3,l4,l5,l6,l7]
         
        #[[27, 864, 915, 306, 119, 43, 38],[35, 895, 950, 298, 93, 42, 76],[1604, 30329, 41760, 18402, 9902, 4920, 3785],[105, 3961, 3945, 1204, 407, 126, 152]]
        #[[27,35,1604,105],[864,895,30329,3961],[915,950,41760,3945],[306,298,18402,1204],[119,93,9902,407],[43,42,4920,126],[38,76,3785,152]]
        # 2312 , 2389 , 110702 , 9900
        data = {
                "labels":labels,
                "chartLabel0":chartLabel[0],"chartLabel1":chartLabel[1],"chartLabel2":chartLabel[2],"chartLabel3":chartLabel[3],
                "chartLabel4":chartLabel[4],"chartLabel5":chartLabel[5],"chartLabel6":chartLabel[6],
                "chartdata0":l,"chartdata1":l2,
                "chartdata2":l3, "chartdata3":l4,
                "chartdata4":l5,"chartdata5":l6,"chartdata6":l7,
        }
        return Response(data)


class ChartData5(APIView):
    def get(self,request , format = None):
        dataf['date_account_created'] = pd.to_datetime(dataf.date_account_created, infer_datetime_format = True)
        dataf.sort_values(by = 'date_account_created', ascending = True, inplace = True)
        df_list = [dataf['date_account_created']]
        headers = ["Date"]
        new_df = pd.concat(df_list, axis=1, keys=headers)
        y_values = []
        df_list2 = new_df['Date'].value_counts().sort_index(ascending=True)
        for i in range(len(df_list2)) :
            y_values.append(df_list2[i])

        dates = get_dates('date_account_created')

        labels = dates
        chartLabel = "date_account_created"
        chartdata = y_values
        data ={
                "labels":labels,
                "chartLabel":chartLabel,
                "chartdata":chartdata,
            }
        return Response(data)

class ChartData6(APIView):
    def get(self,request , format = None):
        dataf['range1'] = [1 if (x>=18 and x<=20) else 0 for x in dataf['age']]
        dataf['range2'] = [1 if (x>20 and x<=30) else 0 for x in dataf['age']]
        dataf['range3'] = [1 if (x>30 and x<=40) else 0 for x in dataf['age']]
        dataf['range4'] = [1 if (x>40 and x<=50) else 0 for x in dataf['age']]
        dataf['range5'] = [1 if (x>50 and x<=60) else 0 for x in dataf['age']]
        dataf['range6'] = [1 if (x>60 and x<=70) else 0 for x in dataf['age']]
        dataf['range7'] = [1 if (x>70 and x<=80) else 0 for x in dataf['age']]
        range1_df = dataf.groupby(['date_account_created','range1']).size().unstack(fill_value=0)
        age1 = range1_df[1].tolist()
        range2_df = dataf.groupby(['date_account_created','range2']).size().unstack(fill_value=0)
        age2 = range2_df[1].tolist()
        range3_df = dataf.groupby(['date_account_created','range3']).size().unstack(fill_value=0)
        age3 = range3_df[1].tolist()
        range4_df = dataf.groupby(['date_account_created','range4']).size().unstack(fill_value=0)
        age4 = range4_df[1].tolist()
        range5_df = dataf.groupby(['date_account_created','range5']).size().unstack(fill_value=0)
        age5 = range5_df[1].tolist()
        range6_df = dataf.groupby(['date_account_created','range6']).size().unstack(fill_value=0)
        age6 = range6_df[1].tolist()
        range7_df = dataf.groupby(['date_account_created','range7']).size().unstack(fill_value=0)
        age7 = range7_df[1].tolist()

        dates = get_dates('date_account_created')
        labels = dates
        chartLabel = ["(id, 18-20)" , "(id, 20-30)", "(id, 30-40)", "(id, 40-50)", "(id, 50-60)", "(id, 60-70)", "(id, 70+)"]
        chartdata = [age1,age2,age3,age4,age5,age6,age7]
        data ={
                "labels":labels,
                "chartLabel0":chartLabel[0],"chartLabel1":chartLabel[1],"chartLabel2":chartLabel[2],"chartLabel3":chartLabel[3],
                "chartLabel4":chartLabel[4],"chartLabel5":chartLabel[5],"chartLabel6":chartLabel[6],
                "chartdata0":age1,"chartdata1":age2,
                "chartdata2":age3, "chartdata3":age4,
                "chartdata4":age5,"chartdata5":age6,"chartdata6":age7,
            }
        return Response(data)

class ChartData7(APIView):
    def get(self,request , format = None):
        df_apps = dataf.groupby(['date_account_created','signup_app']).size().unstack(fill_value=0)
        Android = df_apps['Android'].values.tolist()
        Moweb = df_apps['Moweb'].values.tolist()
        Web = df_apps['Web'].values.tolist()
        Ios = df_apps['iOS'].values.tolist()
        #x_values (dates)
        dates = get_dates('date_account_created')
        labels = dates
        chartLabel = ['Android', 'Moweb', 'Web', 'iOS']
        chartdata = [Android,Moweb,Web,Ios]
        data ={
                "labels":labels,
                "chartLabel0":chartLabel[0],"chartLabel1":chartLabel[1],
                "chartLabel2":chartLabel[2],"chartLabel3":chartLabel[3],
            
                "chartdata0":Android,"chartdata1":Moweb,
                "chartdata2":Web, "chartdata3":Ios,

            }
        return Response(data)

        