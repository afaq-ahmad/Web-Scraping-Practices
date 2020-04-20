'''
Devolper Name: AFAQ AHMAD
Fiverr: https://www.fiverr.com/mrafaq1
Whatssapp: +92-335695635
Email:afaq.ahmad100@gmail.com
'''

urlpage = ''''
Devolper Name: AFAQ AHMAD
Fiverr: https://www.fiverr.com/mrafaq1
Whatssapp: +92-335695635
Email:afaq.ahmad100@gmail.com
'''

urlpage = 'https://www.theguardian.com/football/live/2018/jun/16/croatia-v-nigeria-world-cup-2018-live'

import urllib
import urllib3
import requests
import json, io
from bs4 import BeautifulSoup
urllib3.disable_warnings()

next_link = None
data1=[]
data2=[]

while(1):
    if next_link is not None:
        urlpage = next_link
    headers = {'User-Agent':'Mozilla/5.0'}
    page = requests.get(urlpage, headers=headers, verify=False)
    data = page.content 
    soup = BeautifulSoup(data, "html.parser")
    Blog = soup.find_all('div', {'itemprop' : 'liveBlogUpdate'})
    for i in range(0,len(Blog)):
        first1 = Blog[i].find_all('p', {'class' : 'block-time published-time'})
        time=((first1[0].text).split())[-1].encode('utf-8')
        first2 = Blog[i].find_all('div', {'class' : 'block-elements block-elements--no-byline'})
        if len(first2) > 0:
            first3 = first2[0].find('p')
            if first3 is not None:
                aaaa=first3.get_text()
                Blog_text=aaaa.encode('utf-8')
                print(time)
                print(Blog_text)
                print("----------------------------------")
                data1.append(time)
                data2.append(Blog_text)
        
    For_next_link = soup.find_all('div', {'class' : 'liveblog-navigation__older'})
    if len(For_next_link) > 0:
        handles = [ a["href"] for a in For_next_link[0].find_all("a", href=True)]
        if len(handles) > 0:
            next_link2=handles[0].encode('utf-8')
            next_link= 'https://www.theguardian.com'+ next_link2
        else:
            break
    else:
        break
output_data = {}
for p in range(0,len(data2)):
    output_data[data1[p]]= data2[p]
with io.open('result.json', 'w', encoding='utf8') as json_file:
    data3 = json.dumps(output_data, ensure_ascii=False, encoding='utf8',indent=4, sort_keys=True)
    json_file.write(unicode(data3))

# ( For data loading)
# with open('result.json') as data_file:
#    data_loaded = json.load(data_file)
# for x in data_loaded:
#    print(x.encode('utf-8'),(data_loaded[x]).encode('utf-8'))
# (data_loaded['13:17']).encode('utf-8')