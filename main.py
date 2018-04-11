from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
from time import sleep
import re

urlToped = "https://www.tokopedia.com/search?st=product&q=stefan+janoski"
urlBukaLapak = "https://www.bukalapak.com/products?utf8=%E2%9C%93&search%5Bhashtag%5D=&search%5Bkeywords%5D=nastar&search%5Bsort_by%5D=price%3Aasc"

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=r"C:\Libs\chromedriver.exe", chrome_options=options)


def handleToped(driverItem):
    soup = []
    driverItem.get(urlToped)
    i = 350
    while True:
        # sleep
        sleep(0.5)

        # Scroll down to bottom by 350 every loop
        driverItem.execute_script("window.scrollTo(0, " + str(i) + ");")

        # Get the height of the document
        new_height = driverItem.execute_script("return document.body.scrollHeight")

        i += 350  # Add i + 350 every loop

        # Check if the i is greater than document height
        if (i > new_height):
            # set the page source to using beautiful soup
            soup = BeautifulSoup(driverItem.page_source, 'lxml')
            break  # break the loop

    # find all product card
    page = soup.find_all('div', class_="_27sG_y4O")
    items = []

    # loop every product card in pages
    for item in page:
        print(item.a['href'])

        # find the images inside the product card div
        images = item.find('div', class_="lTz_j9mr").find('img')

        # find the names inside the product card div
        name = item.find('span', class_="_1fFgipsd")

        # find the price inside the product card div
        price = item.find('span', class_="_2Z7a1qvz")

        #remove all string from price 
        price = re.sub(r"\D", "", price.get_text())

        #get product link
        link = item.a['href']
        items.append({
            "images": images['src'], 
            "name": name.get_text(), 
            "price": price, 
            "link": link
        })
    return items