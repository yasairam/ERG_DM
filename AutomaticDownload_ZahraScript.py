#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import sys
import datetime
import requests
import time

def automatic_download(directory):
    
    CurrentDate=now = datetime.datetime.now()
    CurrentYear=CurrentDate.year
    CurrentMonth=CurrentDate.month
    CurrentDay=CurrentDate.day
    today = str(CurrentYear) + str(CurrentMonth) + str(CurrentDay) # Today's date in format of YEARMONTHDAY
    
    dir_files = [] # List all files in folder where .nc files are currently being saved

    for root, directories, files in os.walk(directory): # Loop to walk through path given to find files in folder
        for filename in files:
            filepath = os.path.join(root, filename)
            dir_files.append(filepath)
    
    formatted_fn = [] # List container for .nc files such that only date is present in format YEARMONTHDAY
    
    for f in dir_files:
        formatted_fn.append(f[-16:-8])
    
    formatted_fn.remove('Script/.') # When run on MACOS, remove the extra file that is present
    formatted_fn.sort(reverse=True) # Sort the values in descending order (i.e. most current date at 1st position)
    
    if (len(formatted_fn)) == 0: # If there are no previous files, run the code
        DayNumber= input('Please Specify Number of Days To Download Data.')
        CurrentDate=now = datetime.datetime.now()
        CurrentYear=CurrentDate.year
        CurrentMonth=CurrentDate.month
        CurrentDay=CurrentDate.day
        url1='https://opendap.co-ops.nos.noaa.gov/thredds/fileServer/NOAA/LEOFS/MODELS/'
        url2=url1+str(CurrentYear)+"/"
        url3=url2+str(CurrentMonth)+"/"
        url4=url3+str(CurrentDay)+"/nos.leofs.regulargrid.n00"
        n=0
        while n<=6:
            flag1=1
            flag2=1
            flag3=1
            flag4=1
            finalurl1=url4+str(n)+"."+str(CurrentYear)+str(CurrentMonth)+str(CurrentDay)+".t00z.nc"
            finalurl2=url4+str(n)+"."+str(CurrentYear)+str(CurrentMonth)+str(CurrentDay)+".t06z.nc"
            finalurl3=url4+str(n)+"."+str(CurrentYear)+str(CurrentMonth)+str(CurrentDay)+".t12z.nc"
            finalurl4=url4+str(n)+"."+str(CurrentYear)+str(CurrentMonth)+str(CurrentDay)+".t18z.nc"
            print(finalurl1)
            print(finalurl2)
            print(finalurl3)
            print(finalurl4)
        
            filename1="/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00"+str(n)+"."+str(CurrentYear)+str(CurrentMonth)+str(CurrentDay)+".t00z.nc"
            filename2 = "/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00" + str(n) + "." + str(CurrentYear) + str(CurrentMonth) + str(
            CurrentDay) + ".t06z.nc"
            filename3 = "/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00" + str(n) + "." + str(CurrentYear) + str(CurrentMonth) + str(
            CurrentDay) + ".t12z.nc"
            filename4 = "/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00" + str(n) + "." + str(CurrentYear) + str(CurrentMonth) + str(
            CurrentDay) + ".t18z.nc"
            h1 = requests.head(finalurl1, allow_redirects=True)
            header1 = h1.headers
            content_type1 = header1.get('content-type')
            if 'html' in content_type1.lower():
                flag1=0
            if flag1==1:
                r1 = requests.get(finalurl1, allow_redirects=True)
                open(filename1, 'wb').write(r1.content)
            h2 = requests.head(finalurl2, allow_redirects=True)
            header2 = h2.headers
            content_type2 = header2.get('content-type')
            if 'html' in content_type2.lower():
                flag2 = 0
            if flag2==1:
                r2 = requests.get(finalurl2, allow_redirects=True)
                open(filename2, 'wb').write(r2.content)
            h3 = requests.head(finalurl3, allow_redirects=True)
            header3 = h3.headers
            content_type3 = header3.get('content-type')
            if 'html' in content_type3.lower():
                flag3 = 0
            if flag3 == 1:
                r3 = requests.get(finalurl3, allow_redirects=True)
                open(filename3, 'wb').write(r3.content)
            h4 = requests.head(finalurl4, allow_redirects=True)
            header4 = h4.headers
            content_type4 = header4.get('content-type')
            if 'html' in content_type4.lower():
                flag4 = 0
            if flag4 == 1:
                r4 = requests.get(finalurl4, allow_redirects=True)
                open(filename4, 'wb').write(r4.content)
            n=n+1
        one_day = datetime.timedelta(days=1)
        Date=CurrentDate-one_day
    
        while int(DayNumber)>0:
            Year=Date.year
            Month=Date.month
            Day=Date.day
            url1 = 'https://opendap.co-ops.nos.noaa.gov/thredds/fileServer/NOAA/LEOFS/MODELS/'
            url2 = url1 + str(Year) + "/"
            url3 = url2 + str(Month) + "/"
            url4 = url3 + str(Day) + "/nos.leofs.regulargrid.n00"
            n = 0
            while n <= 6:
                finalurl1 = url4 + str(n) + "." + str(Year) + str(Month) + str(Day) + ".t00z.nc"
                finalurl2 = url4 + str(n) + "." + str(Year) + str(Month) + str(Day) + ".t06z.nc"
                finalurl3 = url4 + str(n) + "." + str(Year) + str(Month) + str(Day) + ".t12z.nc"
                finalurl4 = url4 + str(n) + "." + str(Year) + str(Month) + str(Day) + ".t18z.nc"
                # print(finalurl1)
                # print(finalurl2)
                # print(finalurl3)
                # print(finalurl4)
                filename1 = '/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00' + str(n) + "." + str(Year) + str(Month) + str(
                Day) + ".t00z.nc"
                filename2 = '/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00' + str(n) + "." + str(Year) + str(Month) + str(
                Day) + ".t06z.nc"
                filename3 = '/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00' + str(n) + "." + str(Year) + str(Month) + str(
                Day) + ".t12z.nc"
                filename4 = '/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00' + str(n) + "." + str(Year) + str(Month) + str(
                Day) + ".t18z.nc"
                r1 = requests.get(finalurl1, allow_redirects=True)
                open(filename1, 'wb').write(r1.content)
                r2 = requests.get(finalurl2, allow_redirects=True)
                open(filename2, 'wb').write(r2.content)
                r3 = requests.get(finalurl3, allow_redirects=True)
                open(filename3, 'wb').write(r3.content)
                r4 = requests.get(finalurl4, allow_redirects=True)
                open(filename4, 'wb').write(r4.content)
                n = n + 1
            (DayNumber)=int(DayNumber)-1
    else:
        for file in formatted_fn:
            if formatted_fn[0] == today: # If the latest file is today's date, break out of loop
                print("Latest File Already Downloaded")
                break
            else: # Else, run the script to download!
                DayNumber= input('Please Specify Number of Days To Download Data.')
                CurrentDate=now = datetime.datetime.now()
                CurrentYear=CurrentDate.year
                CurrentMonth=CurrentDate.month
                CurrentDay=CurrentDate.day
                url1='https://opendap.co-ops.nos.noaa.gov/thredds/fileServer/NOAA/LEOFS/MODELS/'
                url2=url1+str(CurrentYear)+"/"
                url3=url2+str(CurrentMonth)+"/"
                url4=url3+str(CurrentDay)+"/nos.leofs.regulargrid.n00"
                n=0
                while n<=6:
                    flag1=1
                    flag2=1
                    flag3=1
                    flag4=1
                    finalurl1=url4+str(n)+"."+str(CurrentYear)+str(CurrentMonth)+str(CurrentDay)+".t00z.nc"
                    finalurl2=url4+str(n)+"."+str(CurrentYear)+str(CurrentMonth)+str(CurrentDay)+".t06z.nc"
                    finalurl3=url4+str(n)+"."+str(CurrentYear)+str(CurrentMonth)+str(CurrentDay)+".t12z.nc"
                    finalurl4=url4+str(n)+"."+str(CurrentYear)+str(CurrentMonth)+str(CurrentDay)+".t18z.nc"
                    print(finalurl1)
                    print(finalurl2)
                    print(finalurl3)
                    print(finalurl4)

                    filename1="/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00"+str(n)+"."+str(CurrentYear)+str(CurrentMonth)+str(CurrentDay)+".t00z.nc"
                    filename2 = "/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00" + str(n) + "." + str(CurrentYear) + str(CurrentMonth) + str(
                CurrentDay) + ".t06z.nc"
                    filename3 = "/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00" + str(n) + "." + str(CurrentYear) + str(CurrentMonth) + str(
                CurrentDay) + ".t12z.nc"
                    filename4 = "/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00" + str(n) + "." + str(CurrentYear) + str(CurrentMonth) + str(
                CurrentDay) + ".t18z.nc"
                    h1 = requests.head(finalurl1, allow_redirects=True)
                    header1 = h1.headers
                    content_type1 = header1.get('content-type')
                    if 'html' in content_type1.lower():
                        flag1=0
                    if flag1==1:
                        r1 = requests.get(finalurl1, allow_redirects=True)
                        open(filename1, 'wb').write(r1.content)
                    h2 = requests.head(finalurl2, allow_redirects=True)
                    header2 = h2.headers
                    content_type2 = header2.get('content-type')
                    if 'html' in content_type2.lower():
                        flag2 = 0
                    if flag2==1:
                        r2 = requests.get(finalurl2, allow_redirects=True)
                        open(filename2, 'wb').write(r2.content)
                    h3 = requests.head(finalurl3, allow_redirects=True)
                    header3 = h3.headers
                    content_type3 = header3.get('content-type')
                    if 'html' in content_type3.lower():
                        flag3 = 0
                    if flag3 == 1:
                        r3 = requests.get(finalurl3, allow_redirects=True)
                        open(filename3, 'wb').write(r3.content)
                    h4 = requests.head(finalurl4, allow_redirects=True)
                    header4 = h4.headers
                    content_type4 = header4.get('content-type')
                    if 'html' in content_type4.lower():
                        flag4 = 0
                    if flag4 == 1:
                        r4 = requests.get(finalurl4, allow_redirects=True)
                        open(filename4, 'wb').write(r4.content)
                    n=n+1
                one_day = datetime.timedelta(days=1)
                Date=CurrentDate-one_day

                while int(DayNumber)>0:
                    Year=Date.year
                    Month=Date.month
                    Day=Date.day
                    url1 = 'https://opendap.co-ops.nos.noaa.gov/thredds/fileServer/NOAA/LEOFS/MODELS/'
                    url2 = url1 + str(Year) + "/"
                    url3 = url2 + str(Month) + "/"
                    url4 = url3 + str(Day) + "/nos.leofs.regulargrid.n00"
                    n = 0
                    while n <= 6:
                        finalurl1 = url4 + str(n) + "." + str(Year) + str(Month) + str(Day) + ".t00z.nc"
                        finalurl2 = url4 + str(n) + "." + str(Year) + str(Month) + str(Day) + ".t06z.nc"
                        finalurl3 = url4 + str(n) + "." + str(Year) + str(Month) + str(Day) + ".t12z.nc"
                        finalurl4 = url4 + str(n) + "." + str(Year) + str(Month) + str(Day) + ".t18z.nc"
                        # print(finalurl1)
                        # print(finalurl2)
                        # print(finalurl3)
                        # print(finalurl4)
                        filename1 = '/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00' + str(n) + "." + str(Year) + str(Month) + str(
                    Day) + ".t00z.nc"
                        filename2 = '/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00' + str(n) + "." + str(Year) + str(Month) + str(
                    Day) + ".t06z.nc"
                        filename3 = '/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00' + str(n) + "." + str(Year) + str(Month) + str(
                    Day) + ".t12z.nc"
                        filename4 = '/Users/pranav.sairam/Desktop/ERG/Data Management/Automatic Download Script/nos.leofs.regulargrid.n00' + str(n) + "." + str(Year) + str(Month) + str(
                    Day) + ".t18z.nc"
                        r1 = requests.get(finalurl1, allow_redirects=True)
                        open(filename1, 'wb').write(r1.content)
                        r2 = requests.get(finalurl2, allow_redirects=True)
                        open(filename2, 'wb').write(r2.content)
                        r3 = requests.get(finalurl3, allow_redirects=True)
                        open(filename3, 'wb').write(r3.content)
                        r4 = requests.get(finalurl4, allow_redirects=True)
                        open(filename4, 'wb').write(r4.content)
                        n = n + 1
                    (DayNumber)=int(DayNumber)-1
                break

