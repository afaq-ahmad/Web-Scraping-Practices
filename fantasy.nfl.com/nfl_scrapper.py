'''
Devolper Name: AFAQ AHMAD
Fiverr: https://www.fiverr.com/mrafaq1
Whatssapp: +92-3356905635
Email:afaq.ahmad100@gmail.com
'''

Initial_address="http://fantasy.nfl.com/league/4008988/history/2017/teamhome?teamId=1"

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
from random import randint
import json, io

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

#driver = webdriver.Chrome(executable_path=r'/Users/Name/Downloads/Compressed/chromedrives/chromedriver.exe')
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

driver.get("http://fantasy.nfl.com/league/4008988/history/2017/teamhome?teamId=6")
time.sleep(3)
s = BeautifulSoup(driver.page_source, 'lxml')
username = driver.find_element_by_id("fanProfileEmailUsername")
password = driver.find_element_by_id("fanProfilePassword")
username.send_keys("bazlla")
password.send_keys("Mrafaq1")
login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()

time.sleep(30)

driver.get(Initial_address)
time.sleep(3)
s = BeautifulSoup(driver.page_source, 'lxml')

team_selector=s.find_all("span", class_="selecter-item")


def saving_function(Excelname,data):
    data[4]=(data[4]).encode('ascii', 'ignore')
    data[3]=(data[3]).encode('ascii', 'ignore')
    afaq=[data]
    #print(afaq)
    csvfile = open(Excelname, 'a')
    for row in afaq:
        #line = ','.join(row)
        values = ','.join(str(v) for v in row)
        csvfile.write(values + '\n')


def savetable(Excelname):
    aaa=s.find_all("div", class_="tableWrap")

    #--------For headlines---------------

    tit=aaa[2].find_all('tr', class_="first")
    titt=tit[0].find_all('th')
    
    data=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    saving_function(Excelname,data)
    data=['-','-','-','-','-','-','-','=','Offense','Team','=','-','-','-','-','-','-','-','-']
    saving_function(Excelname,data)
    data=[' ',' ',' ',' ',' ','Passing',' ',' ','Rushing',' ','Receiving',' ',' ','Return',' ','Misc',' ','Fum','Fantasy']
    saving_function(Excelname,data)
    data=[]
    trr= aaa[0].find_all('tr')
    tit2=aaa[0].find_all('tr', class_="last")
    titt2 = tit2[0].find_all('th')
    for k in range(0,len(titt2)):
        #print(titt2[k].text)
        data.append((titt2[k].text).replace(',',' '))
    saving_function(Excelname,data)
    data=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    saving_function(Excelname,data)

    data=[]
    #print("----------------------")
    for g in range(2,len(trr)):
        trrr=trr[g].find_all('td')
        if len(trrr) > 1:
            for i in range(0,len(trrr)):
                #print(trrr[i].text)=(trrr[i].text).encode('ascii', 'ignore')
                #(trrr[i].text)=(trrr[i].text).encode('ascii', 'ignore')
                #print((trrr[i].text).replace(',',' '))
                data.append((trrr[i].text).replace(',',' '))
            saving_function(Excelname,data)
            data=[]
            #print("------")

    data=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    saving_function(Excelname,data)
    data=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    saving_function(Excelname,data)
    data=['-','-','-','-','-','-','-','=','Kicker','Team','=','-','-','-','-','-','-','-']
    saving_function(Excelname,data)
    data=[' ',' ',' ',' ',' ','PAT',' ','FG Made',' ',' ',' ',' ','FG Miss',' ',' ',' ',' ','Fantasy']
    saving_function(Excelname,data)
    data=[]
    trr= aaa[1].find_all('tr')
    tit2=aaa[1].find_all('tr', class_="last")
    titt2 = tit2[0].find_all('th')
    for k in range(0,len(titt2)):
        #print(titt2[k].text)
        data.append((titt2[k].text).replace(',',' '))
    saving_function(Excelname,data)
    data=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    saving_function(Excelname,data)

    data=[]
    #print("----------------------")
    for g in range(2,len(trr)):
        trrr=trr[g].find_all('td')
        if len(trrr) > 1:
            for i in range(0,len(trrr)):
                #print(trrr[i].text)
                data.append((trrr[i].text).replace(',',' '))
            saving_function(Excelname,data)
            data=[]
            #print("------")

    data=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    saving_function(Excelname,data)
    data=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    saving_function(Excelname,data)
    data=['-','-','-','-','-','=','Defense','Team','=','-','-','-','-','-','-']
    saving_function(Excelname,data)
    data=[' ',' ',' ',' ',' ','Tackles','Turnover',' ','Score',' ',' ','Return',' ','Points','Fantasy']
    saving_function(Excelname,data)
    data=[]
    trr= aaa[2].find_all('tr')
    tit2=aaa[2].find_all('tr', class_="last")
    titt2 = tit2[0].find_all('th')
    for k in range(0,len(titt2)):
        #print(titt2[k].text)
        data.append((titt2[k].text).replace(',',' '))
    saving_function(Excelname,data)
    data=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    saving_function(Excelname,data)

    data=[]
    #print("----------------------")
    for g in range(2,len(trr)):
        trrr=trr[g].find_all('td')
        if len(trrr) > 1:
            for i in range(0,len(trrr)):
                #print(trrr[i].text)
                data.append((trrr[i].text).replace(',',' '))
            saving_function(Excelname,data)
            data=[]
            #print("------")

            
            
for Noofteams in range(1,len(team_selector)+1):
    url_address=bytearray(Initial_address)
    del url_address[-1]
    url_address=str(url_address+str(Noofteams))
    driver.get(url_address)
    time.sleep(randint(0, 9))
    s = BeautifulSoup(driver.page_source, 'lxml')
    
    Basic_save={}
    team_name=s.find("span", class_="selecter-selected")
    team_owner=s.find("ul", class_="owners")
    team_status=s.find_all("ul", class_="teamStats")
    Basic_save['team_name']=(team_name.find("span", class_="label").text)
    Basic_save['team_owner']=team_owner.text

    status_save={}
    qp=0
    for n in team_status[0]:
        #print(((n.text).split())[-1])
        if qp == 0:
            status_save['Rank']=((n.text).split())[-1]
            qp=1
            continue
        if qp == 1:
            status_save['Record']=((n.text).split())[-1]
            qp=2
            continue
        if qp == 2:
            status_save['Streak']=((n.text).split())[-1]
    for n in team_status[1]:
        #print(((n.text).split())[-2])
        status_save['season Result']=((n.text).split())[-2]

    with io.open(Basic_save['team_name']+str('.txt'), 'a', encoding='utf8') as json_file:
        data3 = json.dumps(Basic_save, ensure_ascii=False, encoding='utf8',indent=4, sort_keys=True)
        json_file.write(unicode(data3))
    
    with io.open(Basic_save['team_name']+str('.txt'), 'a', encoding='utf8') as json_file:
        data3 = json.dumps(status_save, ensure_ascii=False, encoding='utf8',indent=4, sort_keys=True)
        json_file.write(unicode(data3))
    Excelname=Basic_save['team_name']+'_Total'+str('.csv')
    savetable(Excelname)
    
    week=s.find_all('ul', class_="weekNav weekNav-full nav-bar")
    week_link_data=[]
    week_link=week[0].find_all('a')
    for k in range(0,len(week_link)-10):
        aa=week_link[k]
        link=aa['href']
        week_link_data.append(link)
        link=None
    week_urll='http://fantasy.nfl.com/'+week_link_data[0]
    week_url2=bytearray(week_urll)
    del week_url2[-1]
    del week_url2[-1]
    for p in range(1,17):
        week_url=str(week_url2+str(p))
        driver.get(week_url)
        time.sleep(randint(0, 9))
        s = BeautifulSoup(driver.page_source, 'lxml')
        Excelname=Basic_save['team_name']+'_week_'+str(p)+str('.csv')
        savetable(Excelname)
    
    week_url='http://fantasy.nfl.com/'+week_link_data[-2]
    driver.get(week_url)
    time.sleep(randint(0, 9))
    s = BeautifulSoup(driver.page_source, 'lxml')
    Excelname=Basic_save['team_name']+'_Last_2_WKS'+str('.csv')
    savetable(Excelname)
    
    week_url='http://fantasy.nfl.com/'+week_link_data[-1]
    driver.get(week_url)
    time.sleep(randint(0, 9))
    s = BeautifulSoup(driver.page_source, 'lxml')
    Excelname=Basic_save['team_name']+'_Last_4_WKS'+str('.csv')
    savetable(Excelname)