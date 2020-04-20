'''
Devolper Name: AFAQ AHMAD
Fiverr: https://www.fiverr.com/mrafaq1
Whatssapp: +92-335695635
Email:afaq.ahmad100@gmail.com
'''

urlpage = 'http://www.goal.com/en-gb/match/russia-v-croatia/commentary-result/ew1rtwpaw88s0xwe3q77erca1'

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
data1=[]
data2=[]
Blog = soup.find_all('div',class_='comment-desc')
for m in range(len(Blog)-1,-1,-1):
    time=Blog[m].find('span',class_='time')
    if time is None:
        text0=Blog[m].find('span',class_='text')
        text1=text0.text
        time='nonmatch'
        data1.append(time)
        data2.append(text1)
        
    else:
        time1=time.text
        text0=Blog[m].find('span',class_='text')
        text1=text0.text
        data1.append(time1)
        data2.append(text1)
        
jsonList = []
for i in range(0,len(data1)):
    jsonList.append({i:{'time':data1[i],'description':data2[i]}})

with io.open('result_sorted.json', 'w', encoding='utf8') as json_file:
    data3 = json.dumps(jsonList, ensure_ascii=False, encoding='utf8',indent=4, sort_keys=True)
    json_file.write(unicode(data3))