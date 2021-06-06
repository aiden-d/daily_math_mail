from os import error
import os as os
from os import path
import secrets
import shutil
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
htmlpath = input("input html path: ")


def findIndexOfLetter(s, l):
    for i in range(len(s) - len(l)):
        if (s[i:i + len(l)] == l):
            return i


s = htmlpath[findIndexOfLetter(htmlpath, "AA HL"):len(htmlpath)]
collection_name = s[23:len(s) - 5]
print(collection_name)
filespath = htmlpath[0:len(htmlpath)-5] + "_files/"

with open(htmlpath) as fp:
    soup = BeautifulSoup(fp, 'html.parser')


def createImageName():
    name = secrets.token_urlsafe(10)
    if(path.exists("images/" + str(name) + ".png") == False):
        return name
    else:
        return createImageName()


def getQuestionImage(fname, span):
    global filespath
    next = span.find("a", class_="et_pb_lightbox_image")
    nextStr = str(next['href'])
    print("img = " + nextStr)
    # make get file without loop
    print(nextStr)
    length = len(nextStr)
    for i in range(length):
        if(nextStr[i:i+4] == ".png"):
            print(nextStr[i-6:i+4])
            path = filespath + \
                str(nextStr[i-6:i+4])
            shutil.copyfile(
                path, "images/" + fname + '.png')
            return
    for i in range(length):
        if(nextStr[i:i+4] == ".gif"):
            print(nextStr[i-6:i+4])
            path = filespath + \
                str(nextStr[i-6:i+4])
            shutil.copyfile(
                path, "images/" + fname + '.png')
            return


def getAnswerImage(fname, span):

    next = span.find_all("a", class_="wplightbox")
    url = next[1]['href']
    r = requests.get(url, stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open("images/" + fname+"-ms.png", 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', fname)
    else:
        print('Image Couldn\'t be retreived')


def main():
    for i in range(3, 100):
        span = soup.find(
            "div", class_="et_pb_section et_pb_section_"+str(i)+" et_pb_with_background et_section_regular")
        if (span == None):
            return
        fname = str(createImageName())
        print("fname = " + fname)
        getQuestionImage(fname, span)
        getAnswerImage(fname, span)
        f = open("index.txt", "a+")
        f.write(fname + ","+collection_name+"\n")
        f.close


main()
