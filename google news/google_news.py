# -*- coding: utf-8 -*-
"""
Created on Fri Aug  31 11:06:29 2018

@author: Afaq Ahmad
@whatsapp:+923356905635
@Email:afaq.ahmad100@gmail.com
"""


print ('Please wait your program is running')
import requests
import json
import warnings
from time import sleep
from openpyxl import Workbook
import time
from tqdm import tqdm
from datetime import date, timedelta
dataset=[]

# start_date='2018-05-26'
# end_date='2018-05-28'
# search_word='mattarella'

start_date=str(input('Enter the start date in this formate (2018-05-26):'))
end_date=str(input('Enter the end date in this formate (2018-05-28):'))
search_word=str(input('Enter the words you want to search in this formate (mattarella):'))

search_word=search_word.replace(' ','+')

def work():    
    for i in range(0,len(j['articles'])):
        data=['-']*6
        author=j['articles'][i]['author']
        data[0]=author
        description=j['articles'][i]['description']
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

d1 = date(int(start_date.split('-')[0]),int(start_date.split('-')[1]),int(start_date.split('-')[2]))
d2 = date(int(end_date.split('-')[0]),int(end_date.split('-')[1]),int(end_date.split('-')[2]))
delta = d2 - d1         # timedelta

datesearch=d1 + timedelta(0)
print('Scraping this date results: ',datesearch)
pbar1 = tqdm(total=100, position=0)

for i in range(delta.days + 1):        
    url = 'https://newsapi.org/v2/everything?q='+search_word+'&from='+str(datesearch)+'&to='+str(datesearch)+'&sortBy=popularity&language=it&page='+str(1)+'&apiKey=c1fd3da039c54b54b9f6d8900d56a728'
    if i>0:
        datesearch=d1 + timedelta(i)
        print('Scraping this date results: ',datesearch)
        pbar1.clear()
        pbar1 = tqdm(total=100, position=0)
    
    response = requests.get(url)
    j=json.loads(response.text)
    total_result=float(response.text.split('totalResults')[1].split(',')[0].replace('":',''))
    p=2
    
    work()
#    print ('Total number of results found: ',len(dataset), end="\r")
    sleep(10)
    strupd=int(100/(total_result/20))
    pbar1.update(strupd)

    while True:
        url = 'https://newsapi.org/v2/everything?q='+search_word+'&from='+str(datesearch)+'&to='+str(datesearch)+'&sortBy=popularity&language=it&page='+str(p)+'&apiKey=c1fd3da039c54b54b9f6d8900d56a728'

        response = requests.get(url)
        j=json.loads(response.text)
        work()
        strupd=int(100/(total_result/20))
        pbar1.update(strupd)
#         print ('Total number of results found: ',len(dataset), end="\r")
        sleep(10)
        if (p >total_result/20) or (p>100):
            break
        p=p+1
        
wb = Workbook(write_only=True)
ws = wb.create_sheet()

# now we'll fill it with 100 rows x 200 columns
for irow in dataset:
    ws.append(irow)
# save the file
wb.save('mattarella_italian_results.xlsx')
