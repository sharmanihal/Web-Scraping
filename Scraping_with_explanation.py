from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd

sauce = urllib.request.urlopen("https://www.realme.com/in/support/software-update").read()

# driver = webdriver.Chrome("/home/nihal/Downloads/chromedriver")
products = []  # List to store name of the product
# prices = []  # List to store price of the product
ratings = []  # List to store rating of the product

# So this and the next line of code gets us the sauce code of the actual page
# driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
# content = driver.page_source

# This is creating a beautiful soup object of the fetched content
soup = BeautifulSoup(sauce, 'lxml')

# print(soup) This will print the source code of the page that we have specified in driver.get() Statement
# This soup object can be used to interact with the sauce code of the website


size = []
name = []

# _________________________________________________________________

for head in soup.find_all('h3', class_='software-mobile-title'):
    name.append(head.find('a').get('title'))

# _________________________________________________________________


for s in soup.find_all('span', class_='software-filesize'):
    size.append(s.text)

# _________________________________________________________________
text = ''
date = []
for date in soup.find_all('div', class_='software-field'):
    text += date.text

date = re.findall('[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}', text)

# _________________________________________________________________

link = []
for ref in soup.find_all('a', class_='software-button'):
    link.append(ref.get('data-href'))
# _________________________________________________________________

version = []
text2 = ''
for ver in soup.find_all('div', class_='software-field'):
    text2 += ver.text
version = re.findall('RMX[A-Z|a-z|0-9|.|_]+', text2)
version += re.findall('CPH[A-Z|a-z|0-9|.|_]+', text2)
# print(version)
# _________________________________________________________________
md5 = []
text3 = ''
for md in soup.find_all('div', class_='software-field'):
    text3 += md.text
md5 = re.findall('[A-Z|a-z|0-9]{32}', text3)
# __________________________________________________________________
older=[]
for old in soup.find_all('div',class_='software-system'):
    older.append(old.text)
# __________________________________________________________________

df = pd.DataFrame({'Product Name': name, 'File Size': size, 'Date': date, 'Download Link': link, 'Version': version
                      , 'MD5 Hash': md5, "Older Version":older})
df.to_csv('products.csv', index=False, encoding='utf-8')

# for a in soup.findAll('a',href=True, attrs={'class':'article'}):
#     name=a.find('div', attrs={'class':'_3wU53n'})
#
#     rating=a.find('div',attrs={'class':'hGSR34'})
#     products.append(name.text)
#
#     rating.append(rating.text)
# df = pd.DataFrame({'Product Name':products,'Rating':rating})
# df.to_csv('products.csv', index=False, encoding='utf-8')
