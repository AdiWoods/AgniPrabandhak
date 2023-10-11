from django.shortcuts import render
from reportedfire.models import ForestDepartmentData,ReportData
from datetime import date
from reportedfire.utils import messagetodepartment,validationandmessage
from datetime import datetime
from django.http import HttpResponse

# for the firms api
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os


# base directory for the firms datapath
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent





from django.core.files.uploadedfile import InMemoryUploadedFile

# open
import requests
import json
API_KEY='3004c5291e1921e68fa6761dd1893d2f'
MAP_KEY="9a189fed19460652d05ea27293b3cb38"




# Create your views here.


# inputing the data from the user

# def reportdata(request):
#     if request.method=="POST":
#         location=request.POST['location']
#         contactnumber=request.POST['phoneno']
#         imagefile=request.FILES['file']
        
#         #fetch the longitude and lattitude data using location from open weather
        
#         # checkfirst data is valid or not (Model for checking the data is valid or not)
        
        
#         today = date.today()
        
#         # changing the date into the string
#         today=str(today)
        
#         # fetch the phone no from the particular department by using the location
#         forestdata=ForestDepartmentData.objects.get(location=location)
#         # contact number
#         # print(forestdata.phone_no)
        
#         messagetodepartment(forestdata.phone_no,location)
        
        
        
        
        
    
#     # save data to the database
#         userreport=Report(location=location,date=today,phone_no=contactnumber,fireimage=imagefile)
#         userreport.save()
        
        
        
      
        
  
        
    
    
#     return render(request,"inputdata.html")



# this section is to report the fire in the certain area

# landing page
def homePage(request):
    
    
    
    return render(request,"landing.html")
    




def reportdata(request):
    wronginformation=""
    
    if request.method=="POST":
        print("Post request")
        lattitude=request.POST['latitude']
        longitude=request.POST['longitude']
        image=request.FILES['image']
        
        lat=float(lattitude)
        lat=int(lat)
        
        lon=float(longitude)
        lon=int(lon)
        
        validate=validationandmessage(image,lat,lon)
        # date=datetime.datetime.now()
        # print(date)
        
        if validate=="fire":
            ReportData(longitude=lon,lattitude=lat,fireimage=image,date=date).save()
            
        
        else:
            wronginformation = "Invalid information provided. Please provide accurate data or additional images."
            print(wronginformation)
        
            
    
    
    return render(request,"inputform.html",{"wrong_information":wronginformation})



# this section is for the alert


def alertinfo(request):
    warn=''
    if request.method=="POST":
        phone_no=request.POST['phoneNumber']
        city=request.POST['cityName']
        # longitude and the lattitude from city name
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3004c5291e1921e68fa6761dd1893d2f'
        response=requests.get(url=url)
        if response.status_code!=200:
            return HttpResponse("Inavlid city name")
        
        
        
        
        
        # print("Response from the api",response)
        data=json.dumps(response.json())
        
        data=response.json()
        # data=json.dumps(data)
        print("Longitude and the lattide of the location")
        # print(data)
        # # print(data)
        print(int(data['coord']['lon']))
        print(int(data['coord']['lat']))
        
        if  ForestDepartmentData.objects.filter(location=city).exists():
            pass
            # print("Your location data is present on the database")
            
            
        else:
            forestdepartmentdata=ForestDepartmentData(phone_no=phone_no,location=city,lattitude=int(data['coord']['lat']),longitude=int(data['coord']['lon']))
            forestdepartmentdata.save()
            
            
        # second api response
        date=datetime.datetime.now()
        date=date.date()
        url2=f"https://firms.modaps.eosdis.nasa.gov/api/area/html/9a189fed19460652d05ea27293b3cb38/VIIRS_NOAA20_NRT/world/1/{date}"
        
        
        # if the check file is there or not 
        # path="/Users/khumapokharel/Desktop/Hackathon/backendforreport/fire_report/firmsdata"
        
        path=os.path.join(BASE_DIR,"firmsdata")+f"/{date}.csv"
        # print(path)
        
        if not os.path.exists(path):
            response1=requests.get(url=url2)
            print(response1.content)
            soup = BeautifulSoup(response1.content, 'html.parser')
            element=soup.find(id='result')
            print("Element data",element)
            
            with open(path, 'w') as f:
                f.write(element.text)
                df=pd.read_csv(path)
                df['latutude']=df['latutude'].astype(int)
                df['longitude']=df['longitude'].astype(int)
                print(df[df['latitude']==2.75851])
                # print(df)
        
        else:
            df=pd.read_csv(path)
            print("Latitude is")
            
            df['latitude']=df['latitude'].astype(int)
            df['longitude']=df['longitude'].astype(int)
            
            firedetectedarea=df[(df['latitude']==int(data['coord']['lat'])) & (df['longitude']==int(data['coord']['lon']))]
            
            if firedetectedarea.empty:
                warn="there is no fire on your area"
            
            else:
                warn=f"Fire found in your area latitude={data['coord']['lat']} longitude={data['coord']['lon']}"
            
            
                
        
            
       
            
               
        
        
        
        
       
    
    return render(request,"alert.html",{"warn":warn})