import os
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import shutil
import requests

driver = webdriver.Chrome('/home/nihal/Downloads/chromedriver')
driver.get('https://www.chrisburkard.com/Shop/Best-Sellers/')

itr = 0

while itr < 10:

    content = driver.execute_script('return document.documentElement.outerHTML')
    soup = BeautifulSoup(content, 'html.parser')
    image = []
    for i in soup.find_all('img'):
        image.append(i.get('src'))

    current_path = os.getcwd()
    for img in image:
        try:
            file_name = os.path.basename(img)
            img_r = requests.get(img, stream=True)
            print(img_r)
            new_path = os.path.join(current_path, 'images', file_name)
            print(new_path)
            with open(new_path, 'wb') as obj:
                shutil.copyfileobj(img_r.raw, obj)
            del img_r
        except:
            pass
    itr += 1
    time.sleep(5)





