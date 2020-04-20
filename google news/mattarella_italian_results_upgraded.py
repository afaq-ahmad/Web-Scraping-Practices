# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 23:44:58 2018

@author: Afaq Ahmad
@whatsapp:+923356905635
@Email:afaq.ahmad100@gmail.com
"""

start_date='2018-05-26'  #start date of search results
end_date='2018-05-28'    #end date of search results
search_word='mattarella' #keyword search of google news

print ('Please wait your program is running')

##-------------------Libraries required------------------###
import requests
import json
import warnings
from time import sleep
from openpyxl import Workbook
import time
from datetime import date, timedelta
##------------------------------------------------------###
dataset=[]  #---Array For results saving


search_word=search_word.replace(' ','+') # if multiple words in search keywords then seperate them with + symbol


##---------------------------json seperate extraction of function-----------------------------------##
def work():
    for i in range(0,len(j['articles'])):
        data=['-']*6
        author=j['articles'][i]['author']
        data[0]=author
        description=j['articles'][i]['description']  #-all parameters accessing from jason file 'j' from google request
        data[1]=description
        publishedAt=j['articles'][i]['publishedAt']
        data[2]=publishedAt
        source_name=j['articles'][i]['source']['name']
        data[3]=source_name
        title=j['articles'][i]['title']
        data[4]=title
        url=j['articles'][i]['url']
        data[5]=url
        dataset.append(data)
        print (len(dataset),'>>>>>>',data)  # for printing the results

##------------------------------------------------------------------------------------------------##

##------------input date splition for input getting between the different dates for search results-----------##
d1 = date(int(start_date.split('-')[0]),int(start_date.split('-')[1]),int(start_date.split('-')[2]))  
d2 = date(int(end_date.split('-')[0]),int(end_date.split('-')[1]),int(end_date.split('-')[2]))
delta = d2 - d1         # timedelta

##-----------------------------------------------------------------------------------------------------------##



##-------<<core prgram>> where different results are fetched using google api and its key in which we first make-------##
##-------a request to google with searh term,date,language and special google news api key, made on my personal--------##
##-------developer account.--------------------------------------------------------------------------------------------##

for i in range(delta.days + 1):        
    
    datesearch=d1 + timedelta(i)
    print('Scraping this date results: ',datesearch)
    
    url = 'https://newsapi.org/v2/everything?q='+search_word+'&from='+str(datesearch)+'&to='+str(datesearch)+'&sortBy=popularity&language=it&page='+str(1)+'&apiKey=c1fd3da039c54b54b9f6d8900d56a728'
    print (url) # url which use for accesing specific page
    
    response = requests.get(url) # request library make request on this url, for accesing the page from google
    j=json.loads(response.text)  # the output of request converted to json so that we can easily extract the data.
    total_result=float(response.text.split('totalResults')[1].split(',')[0].replace('":','')) # this line show total number of result of that specific date
    print ('Total number of results found: ',int(total_result))
    
    work()  # upper defined function that extract the information from json j variable
    sleep(10) # 10 sec time for sleep so that google not block us, increase it if some how results are not comming.
    p=2
    while True:
        url = 'https://newsapi.org/v2/everything?q='+search_word+'&from='+str(datesearch)+'&to='+str(datesearch)+'&sortBy=popularity&language=it&page='+str(p)+'&apiKey=c1fd3da039c54b54b9f6d8900d56a728'
        print (url)
        response = requests.get(url) ##----- Requesting the other pages of google results next pages on the same date
        j=json.loads(response.text)
        work()
        sleep(10)
        if (p >total_result/20) or (p>100): 
            break  ## break the current loop if the all the results are fetched
        p=p+1
        
        
##--------------------------------------------------------------------------------------------------------------------##

        
wb = Workbook(write_only=True) #Workbook library for excel saving
ws = wb.create_sheet()

# now we'll fill it with results that are stored in dataset
for irow in dataset:
    ws.append(irow)
# save the file
wb.save('mattarella_italian_results_upgraded.xlsx')   # saving file name