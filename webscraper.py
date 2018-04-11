import re
from bs4 import BeautifulSoup
from time import sleep

def linkToped(originalUrl, searchTerm):
    searchTerm = searchTerm.lower()
    searchTerm = re.sub(r'\s+', '+', searchTerm)
    finalSearchTerm = originalUrl + searchTerm
    return finalSearchTerm

def handleToped(driverItem, searchTerm, originalUrl):
    soup = []
    url = linkToped(originalUrl, searchTerm)
    driverItem.get(url)
    i = 350
    while True:
        # sleep
        sleep(0.5)

        # Scroll down to bottom by 350 every loop
        driverItem.execute_script("window.scrollTo(0, " + str(i) + ");")

        # Get the height of the document
        new_height = driverItem.execute_script("return document.body.scrollHeight")

        i += 350  # Add i + 350 every loop
        items = [] #Intialize empty items array

        # Check if the i is greater than document height
        if (i > new_height):
            # set the page source to using beautiful soup
            soup = BeautifulSoup(driverItem.page_source, 'lxml')
            break  # break the loop

    if "hot" not in driverItem.current_url:
        # find all product card
        page = soup.find_all('div', class_="_27sG_y4O")

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
    else:
        items = []
    return items