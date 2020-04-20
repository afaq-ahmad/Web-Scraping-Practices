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

driver = webdriver.Chrome(executable_path=r'/Users/Name/Downloads/Compressed/chromedrives/chromedriver.exe')

driver.get("https://www.theguardian.com/football/ng-interactive/2018/jun/05/world-cup-2018-complete-guide-players-ratings-goals-caps")
wait = WebDriverWait(driver, 10)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")
teams_d = soup.find("div", class_="gv-teams")

team_players = soup.find_all("div", class_="gv-player-details-inner")
teams=['russia','saudi-arabia','egypt','uruguay','portugal','spain','morocco','iran','france','australia','peru',
 'denmark','argentina','iceland','croatia','nigeria','brazil','switzerland','costa-rica',
 'serbia','germany','mexico','sweden','south-korea',
'belgium','panama','tunisia','england','poland','senegal','colombia','japan']

player_stor={}
data1={}
one_player={}

for t_n in range(0,32):
    id1="gv-team-details-block_"+str(teams[t_n])
    russian_team=team_players[0].find("div", id=id1)
    for pln in range(1,24):
        player_dec="gv-player-details-block_"+str(teams[t_n])+"_"+str(pln)
        player=team_players[0].find_all("div", id=player_dec)
        a1=player[0].find_all("div", class_="gv-player-details-wrapper")
        
        player_name=a1[0].find_all("h2")
        data1['name']=player_name[0].text
        print(player_name[0].text)
        
        No1_goal_kepper=a1[0].find_all("h4")
        data1['No1_goal_kepper']=No1_goal_kepper[0].text
        print(No1_goal_kepper[0].text)

        club=a1[0].find_all("div", class_="gv-table-cell gv-team-info-coach")
        data1['club']=club[0].text
        print(club[0].text)

        caps=a1[0].find_all("div", class_="gv-table-cell gv-team-info-group")
        data1['caps']=caps[0].text
        print(caps[0].text)

        Goals=a1[0].find_all("div", class_="gv-table-cell gv-team-info-rank")
        data1['Goals']=Goals[0].text
        print(Goals[0].text)

        age=a1[0].find_all("div", class_="gv-table-cell gv-team-info-age")
        data1['age']=age[0].text
        print(age[0].text)
        player_bio=player[0].find_all("p")
        print(player_bio[0].text)
        data1['Playe_Bio']=player_bio[0].text
        one_player[pln]=data1
        data1={}
        print('+++++++++++++++++++++++++++++')
    player_stor[teams[t_n]]=one_player
    one_player={}
    
    playing_status={}
playing_status0={}

playing_status1={}
players_info = teams_d.find_all("div", class_="gv-cell-block-players gv-main-column")
ptts=0
for steps in range(0,128,4):
    
    Goal_kepers = players_info[steps].find_all("div", class_="gv-player-number gv-team-base-background")
    for plnn1 in range(0,len(Goal_kepers)):
        Goal_kepper_no=(Goal_kepers[plnn1].find_all("span"))[0].text
        print(Goal_kepper_no)
        playing_status0[plnn1]=player_stor[teams[ptts]][int(Goal_kepper_no.encode('ascii', 'ignore'))]
    playing_status1['Goal kepper']=playing_status0
    playing_status0={}

    Defenders = players_info[steps+1].find_all("div", class_="gv-player-number gv-team-base-background")
    for plnn2 in range(0,len(Defenders)):
        Defenders_no=(Defenders[plnn2].find_all("span"))[0].text
        print(Defenders_no)
        playing_status0[plnn2]=player_stor[teams[ptts]][int(Defenders_no.encode('ascii', 'ignore'))]
    playing_status1['Defenders']=playing_status0
    playing_status0={}


    Midfielders = players_info[steps+2].find_all("div", class_="gv-player-number gv-team-base-background")
    for plnn3 in range(0,len(Midfielders)):
        Midfielders_no=(Midfielders[plnn3].find_all("span"))[0].text
        print(Midfielders_no)
        playing_status0[plnn3]=player_stor[teams[ptts]][int(Midfielders_no.encode('ascii', 'ignore'))]
    playing_status1['Midfielders']=playing_status0
    playing_status0={}

    Forwards = players_info[steps+3].find_all("div", class_="gv-player-number gv-team-base-background")
    for plnn4 in range(0,len(Forwards)):
        Forwards_no=(Forwards[plnn4].find_all("span"))[0].text
        print(Forwards_no)
        playing_status0[plnn4]=player_stor[teams[ptts]][int(Forwards_no.encode('ascii', 'ignore'))]
    playing_status1['Forwards']=playing_status0
    playing_status0={}
    
    playing_status[teams[ptts]]=playing_status1
    playing_status1={}
    ptts=ptts+1

    print('++++++++++++++++++')
    
    with io.open('result.json', 'w', encoding='utf8') as json_file:
    data3 = json.dumps(playing_status, ensure_ascii=False, encoding='utf8',indent=4, sort_keys=True)
    json_file.write(unicode(data3))
    
    team_info = teams_d.find_all("div", class_="gv-team-info")
for ted in range(0,32):
    coach_name=team_info[ted].find("div", class_="gv-table-cell gv-team-info-coach").text
    print(coach_name)
    group=team_info[ted].find("div", class_="gv-table-cell gv-team-info-group").text
    print(group)
    fifa_rank=team_info[ted].find("div", class_="gv-table-cell gv-team-info-rank").text
    print(fifa_rank)
    team_bio=team_info[ted].find("p", class_="gv-team-info-bio").text
    print(team_bio)
    print
    team_strengths=team_info[ted].find("p", class_="gv-team-info-strengths").text
    print(team_strengths)
    print
    team_weakness=team_info[ted].find("p", class_="gv-team-info-weaknesses").text
    print(team_weakness)