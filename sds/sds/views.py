from django.http import HttpResponse
from django.shortcuts import render
# from django.db import models
# from filter.models import tvshows 
import requests
import json


# def filters():

     

def home(request):
   return render(request,'home.html')
   
def results(request):
   country_param=(request.GET.get('country'))
   date_param=(request.GET['tvdate'])
   show_rating=((request.GET['show_rating']))
   language=((request.GET['Language']))
   Genre=((request.GET['Genre']))
   parameters={'country':country_param,'date':date_param}
   sort=((request.GET['Sort']))

   
      


   print(parameters)
   res=requests.get('https://api.tvmaze.com/schedule',params=parameters)
   r=res.json()
   list1=[]
   list2=[]
   list3=[]
   mylist=[]
   sortdict={}
   if len(r)!=0:
      if (language=='0' and Genre=='0' and show_rating=='0'):
         for i in range(0,len(r)):
            mylist.append(r[i]['show']['name'])
            # if (r[i]['show']['name']['rating']['average']!=None):
            #    sortdict[r[i]['show']['name']]=r[i]['show']['name']['rating']['average']
         if sort=="0":
             mylist.sort()
         elif sort=="1":
             mylist.sort(reverse=True ,key=str.lower)
         # elif sort=='2':
            
         params2={'list':mylist}
         return render(request,'page2.html',params2)
   else:
      return render(request,'alert.html')
   
   
   if len(r)!=0:
      for i in range(len(r)):
         if show_rating!='0':
            if r[i]['show']['rating']['average']!=None and r[i]['show']['rating']['average']>int(show_rating):
               list1.append(r[i]['show']['name'])
         else:
               list1.append(r[i]['show']['name'])
              

         if language!="0":
            if r[i]['show']['language']==language:
               list2.append(r[i]['show']['name'])
               
         else:
            list2.append(r[i]['show']['name'])
            
         if Genre!="0":
            if Genre in r[i]['show']['genres']:
               list3.append(r[i]['show']['name'])
         else:
            list3.append(r[i]['show']['name'])
            
     
      mylist=list(set.intersection(set(list1),set(list2),set(list3)))
      if sort=="0":
            mylist.sort()
      elif sort=="1":
            print("hello")
            mylist.sort(reverse=True,key=str.lower)
      print(mylist)
      params2={'list':mylist}
      # print(mylist)
      return render(request,'page2.html',params2)
   else:
      return render(request,'alert.html')