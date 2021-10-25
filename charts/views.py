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

dict = {}
dictt = {}
def get_data(col):
    affCol = set(dataf[col].values)
    for i in affCol:
        dict[i] = (dataf[col].value_counts()[i]/len(dataf[col].values)) * 100

    return dict
def get_samples(col):
    country = set(dataf[col].values)
    for i in country:
        dictt[i]  = dataf[col].value_counts()[i]
    return dictt

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

#Affiliate channel percentage
class ChartData1(APIView):
   
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

#Affiliate channel provider percentage
class ChartData2(APIView):
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
        data ={
                        "labels":labels,
                        "chartLabel":chartLabel,
                        "chartdata":chartdata,
                }
        return Response(data)

#Samples per class 
class ChartData3(APIView):
    def get(self,request , format = None):
            dict3 = get_samples('country_destination')
            
            sortednames=sorted(dict3.keys(), key=lambda x:x.lower())
            keyss = []
            valuess = []
            for i in sortednames:
                keyss.append(i)
                valuess.append(dict3[i])
            
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
        dff = set(dataf["signup_app"].values)
    
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

        dict2 = {}
        
        dict2['Android'] = no_of_users(Android)
        dict2['Moweb'] = no_of_users(Moweb)
        dict2['Web'] = no_of_users(Web)
        dict2['iOS'] = no_of_users(Ios)
        keys2 = []
        keys2.append(dict2.keys())
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

'''new_df2 = dataf['date_account_created']
df_list = new_df2.value_counts()
x_values = df_list.index
y_values = []
for i in range(len(df_list)):
    y_values.append(df_list[i])

output_file("figure5.html")

# create a new plot with a title and axis labels
p = figure(title="Respiration rate class", x_axis_label= "Patient ID 123", y_axis_label= "Respiration rates", plot_width = 1000)

# add a line renderer with legend and line thickness
p.line(x_values, y_values, legend="Respiration rate", line_width=2)


# show the results
show(p)'''
'''class ChartData(APIView):
    def get(self,request , format = None):
        new_df2 = dataf['date_account_created']
        df_list = new_df2.value_counts()
        x_values = df_list.index
        y_values = []
        for i in range(len(df_list)):
            y_values.append(df_list[i])
        
        labels = ["01-2010","07-2010","01-2011","07-2011","01-2012","07-2012","01-2013","07-2013","01-2014","07-2014"]
        chartLabel = "date_account_created"
        chartdata = date
        data ={
                "labels":labels,
                "chartLabel":chartLabel,
                "chartdata":chartdata,
            }
        return Response(data)'''