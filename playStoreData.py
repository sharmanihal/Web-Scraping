import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
import re

driver = webdriver.Chrome('/home/nihal/Downloads/chromedriver')
driver.get(
    'https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU&hl=en')


itr = 0

while itr<10:
    name = []
    rating = []
    content = driver.execute_script('return document.documentElement.outerHTML')
    soup = BeautifulSoup(content, 'html.parser')
    for i in soup.find_all('div',class_='WsMG1c nnK0zc'):
        name.append(i.get('title'))

    text = ''
    for i in soup.find_all('div', class_='pf5lIe'):
        text += (i.find('div').get('aria-label'))
    rating += re.findall('[0-9|.]+', text)

    itr+=1
    time.sleep(5)

df=pd.DataFrame({'Name':name,'Rating':rating})
df.to_csv('PlayStore.csv',index=False,encoding='utf-8')

