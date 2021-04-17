
import requests
import os
import subprocess
from bs4 import BeautifulSoup
imageName = input("Enter Image Collection   :  ")
url = f"https://unsplash.com/s/photos/{imageName}?orientation=portrait"
unsplash = requests.get(url)
unsplach_soup = BeautifulSoup(unsplash.content, 'html.parser')
body = unsplach_soup.find("body")
data_list = ((((body.find(id="app").find("div")).find("div", {
             "data-test": "search-route"}).find("div", {"data-test": "search-photos-route"}).find("div"))))

if os.path.exists(imageName):
    for href in (data_list.find_all("div", {'class': "_1ZjfQ"})):
        if (len((href.find_all("a", {"title": "Download photo"}))) != 0):
            for link in (href.find_all("a", {"title": "Download photo"})):
                filename=(link["href"].split("/")[4])
                filelink=(link["href"].split("?")[0])
                file_path = "./"+imageName+"/" + filename+".jpg"
                subprocess.check_output(['wget', '-O', file_path, filelink])
                
else:
    os.mkdir(imageName)
    for href in (data_list.find_all("div", {'class': "_1ZjfQ"})):
        if (len((href.find_all("a", {"title": "Download photo"}))) != 0):
            for link in (href.find_all("a", {"title": "Download photo"})):
                filename=(link["href"].split("/")[4])
                filelink=(link["href"].split("?")[0])
                file_path = "./"+imageName+"/" + filename+".jpg"
                subprocess.check_output(['wget', '-O', file_path, filelink])