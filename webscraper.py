import re
from bs4 import BeautifulSoup
from time import sleep
from flask import Flask


def loopThroughPages(driverItem):
    i = 350
    soup = [] #Intialize empty soup array or page source
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
    return soup

def handleSearchLink(originalUrl, searchTerm):
    searchTerm = re.sub(r'\s+', '+', searchTerm.lower())
    finalSearchTerm = originalUrl + searchTerm
    return finalSearchTerm


def handleToped(driverItem, originalUrl, searchTerm):
    items = [] #Intialize empty items array
    url = handleSearchLink(originalUrl, searchTerm)
    driverItem.get(url)
    soup = loopThroughPages(driverItem)

    if "hot" not in driverItem.current_url:
        # find all product card
        page = soup.find_all('div', class_="_27sG_y4O")

        # loop every product card in pages
        for item in page:
            # find the images inside the product card div
            images = item.find('div', class_="lTz_j9mr").find('img')
            # print(images)
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
                "price": int(price), 
                "link": link
            })
    else:
        # find all product card
        page = soup.find('div', id="product-results")
        productCard = page.find_all('div', class_="product-card ")
        for product in productCard:
            image = product.a.img['src']

            name = product.find('div', class_="detail__name js-ellipsis ng-binding").get_text()

            link = product.a['href']

            price = product.find('span', class_="detail__price ng-binding")
            price = re.sub(r"\D", "", price.get_text())

            items.append({
                "image": image,
                "name": name,
                "link": link,
                "price": int(price)
            })
    return items

def handleBukaLapak(driverItem, originalUrl, searchTerm):
    items = [] #Intialize empty items array
    url = handleSearchLink(originalUrl, searchTerm)
    driverItem.get(url)
    
    soup = loopThroughPages(driverItem)
    #get product carts
    productCard = soup.find_all('div', class_="product-card")

    #loop throught product items
    for item in productCard:
        images = ""
        name = ""
        price = ""
        links = item.a['href']
        items.append({
            "images": images,
            "name" : name,
            "price": price,
            "links": links
        })
    return items