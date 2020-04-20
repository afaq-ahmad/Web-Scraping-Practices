import requests
import datetime
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from dbModel import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
targetURL = 'https://play.google.com/store/apps/category/BOOKS_AND_REFERENCE/collection/topselling_new_free'
head = 'https://play.google.com'


def setbrower():
    ## Firefox
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True
    driver = webdriver.Firefox(firefox_profile=profile)

    ## Chrome
    # options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # driver = webdriver.Chrome(chrome_options=options)

    driver.get(targetURL)
    target = 0
    while target != 540:
        print('parsing 540 count......')
        ## Simulate the behavior of human browsing
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("document.getElementById('show-more-button').click();")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(2, 22);")
        time.sleep(0.5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        data_list = soup.select('.id-card-list .card')
        index = len(data_list)
        target = int(data_list[index - 1].select('.title')[0].text.split('.')[0])
        print("target count:", target)
    driver.close()
    driver.quit()
    return data_list


def getAppLink(data_list):
    item_head = "data"
    app_item = []
    for data in data_list:
        app_data = {
            "itemhead": item_head,
            "link": head + data.find('a')['href']
        }
        app_item.append(app_data)
    return app_item


def getAppInformation(app):
    all_information = []
    for index, item in enumerate(app, 1):
        rs = requests.session()
        res = rs.get(item['link'], verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        for data in soup.select('.main-content'):
            ## rate
            try:
                rate = data.select('.score')[0].text
            except:
                rate = 0
            ## datePublished, numDownloads
            datePublished, numDownloads = "", ""
            for tag in data.select('.details-section-contents .meta-info .content'):
                try:
                    if (tag.attrs['itemprop'] == 'datePublished'):
                        datePublished = tag.text
                    if (tag.attrs['itemprop'] == 'numDownloads'):
                        numDownloads = tag.text
                    if (datePublished != "" and numDownloads != ""):
                        break
                except:
                    pass
            try:
                if (numDownloads == ""):
                    numDownloads = 0
                app_data = {
                    "app": data.select('.id-app-title')[0].text,
                    "link": item['link'],
                    "autor": data.select('.document-subtitle.primary')[0].text,
                    "rate": rate,
                    "download": numDownloads,
                    "publish": datePublished,
                    "item": item['itemhead']
                }
            except:
                print('There is a problem with the URL {}'.format(item['link']))
                break

            all_information.append(app_data)
        print('{} %'.format(round(100 * index / len(app), 2)))
    return all_information


def WriteDB(information):
    for data in information:
        months = {
            "janvier": 1,
            "février": 2,
            "mars": 3,
            "avril": 4,
            "mai": 5,
            "juin": 6,
            "juillet": 7,
            "août": 8,
            "septembre": 9,
            "octobre": 10,
            "novembre": 11,
            "décembre": 12
        }

        index_key = data['publish'].split(' ')[1]
        time_temp = data['publish'].replace(data['publish'].split(' ')[1], str(months[index_key]))

        insert_data = GooglePlay(
            App=data['app'],
            Link=data['link'],
            Autor=data['autor'],
            Rate=data['rate'],
            Download=data['download'],
            Publish=datetime.datetime.strptime(time_temp, "%d %m %Y").date(),
            Item=data['item'],
        )
        db.session.add(insert_data)
    db.session.commit()


if __name__ == "__main__":
    tStart = time.time()
    print('Start parsing google play...(1/2)')
    data_list = setbrower()
    app_item = getAppLink(data_list)
    print('Start parsing google play...(2/2)')
    information = getAppInformation(app_item)
    print('End parsing google play')
    tEnd = time.time()
    print('It cost {} sec'.format(round(tEnd - tStart, 2)))
    print('Start Writing DB')
    WriteDB(information)
    print('End Writing DB')
    print('DONE')
