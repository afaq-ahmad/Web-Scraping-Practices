
urlpage = 'http://www.goal.com/en-us/news/mexico-vs-sweden-tv-channel-live-stream-squad-news-preview/68j098zeukvb1h3m4qnt1tzh8'

import urllib
import urllib3
import requests
import json, io
from bs4 import BeautifulSoup
urllib3.disable_warnings()

headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(urlpage, headers=headers, verify=False)
data = page.content 
soup = BeautifulSoup(data, "html.parser") 
Blog = soup.find_all('div', {'class' : 'body'})
pesd=Blog[0].find_all('strong')

data1=[]
data2=[]
for i in range(len(pesd)):
    if "min" in pesd[i].text:
        time=((((pesd[i].next_element)).encode('ascii', 'ignore')).replace(": ","")).replace(":","")
        text=(((pesd[i].next_element).next_element).encode('ascii', 'ignore')).replace("\n","")
        if text[0]==' ':
            text=text[1:len(text)]
        
        print(time)
        print(text)
        data1.append(time)
        data2.append(text)
        print('++++++++++++++++++++++++++++++++++++')

jsonList = []
for i in range(0,len(data1)):
    jsonList.append({'time':data1[i],'description':data2[i]})

with io.open('result_sorted.json', 'w', encoding='utf8') as json_file:
    data3 = json.dumps(jsonList, ensure_ascii=False, encoding='utf8',indent=4, sort_keys=True)
    json_file.write(unicode(data3))