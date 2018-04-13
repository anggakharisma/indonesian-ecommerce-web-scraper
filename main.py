from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
from time import sleep
import re
import webscraper

urlToped = "https://www.tokopedia.com/search?st=product&q="
urlBukaLapak = "https://www.bukalapak.com/products?utf8=✓&source=navbar&from=omnisearch&search_source=omnisearch_organic&search[hashtag]=&search[keywords]="

options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome(executable_path=r"C:\Libs\chromedriver.exe", chrome_options=options)

# print(webscraper.handleToped(driver, urlToped, "hdd enclosure"))
print(webscraper.handleBukaLapak(driver, urlBukaLapak, "nastar"))
