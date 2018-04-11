from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
from time import sleep
import re
import webscraper

urlToped = "https://www.tokopedia.com/search?st=product&q="
urlBukaLapak = "https://www.bukalapak.com/products?utf8=%E2%9C%93&search%5Bhashtag%5D=&search%5Bkeywords%5D=nastar&search%5Bsort_by%5D=price%3Aasc"

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=r"C:\Libs\chromedriver.exe", chrome_options=options)