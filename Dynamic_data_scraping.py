import os
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import shutil
import time

driver = webdriver.Chrome("/home/nihal/Downloads/chromedriver")

driver.get("https://www.chrisburkard.com/Shop/Best-Sellers/")

itr = 0
# we use while loop so that it script gets time to fetch image data
while itr < 10:
    content = driver.execute_script('return document.documentElement.outerHTML')
    # This is creating a beautiful soup object of the fetched content
    soup = BeautifulSoup(content, 'html.parser')
    image = []
    for i in soup.find_all('img'):
        image.append(i.get('src'))

    current_path = os.getcwd()  # returns the working directory address

    for img in image:
        try:
            filename = os.path.basename(img)  # returns the basename eg. /home/nihal.jpeg this will return nihal.jpeg
            img_r = requests.get(img, stream=True)  # this gets the image using its url(img)

            new_path = os.path.join(current_path, 'images',filename)  # this helps create a well defined path for the image


            # this will help us store the image
        # open('path of file if present open otherwise create, 'format read only write only etc') as referstheobject
            with open(new_path, 'wb') as output_file:
                # wb means write only binary format overwrite existing file or create a new file
                # we want this because we are grabbing raw data of image by img_r.raw
                shutil.copyfileobj(img_r.raw, output_file)
                # shutil.copyfileobj() method in Python is used to copy the contents of a file-like object to another file-like object.
            del img_r
        except:
            pass

    itr += 1
    time.sleep(5)
