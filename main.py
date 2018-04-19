from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
from time import sleep
import re
import webscraper
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import os

urlToped = "https://www.tokopedia.com/search?st=product&q="
urlBukaLapak = "https://www.bukalapak.com/products?utf8=✓&source=navbar&from=omnisearch&search_source=omnisearch_organic&search[hashtag]=&search[keywords]="

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)
if(os == 'nt'):
    driver = webdriver.Chrome(executable_path=r"C:\Libs\chromedriver.exe", chrome_options=options)

app = Flask(__name__)
CORS(app)

@app.route("/toped")
def toped():
    args = request.args.get('query', default = "/")
    if(args == "/" ):
        return redirect("/")
    else:
        return jsonify(webscraper.handleToped(driver, urlToped, args))

@app.route('/bukalapak')
def bukalapak():
    args = request.args.get('query', default = "/")
    if(args == "/" ):
        return redirect("/")
    else:
        return jsonify(webscraper.handleBukaLapak(driver, urlBukaLapak, args))
 
@app.route("/")
def home():
    return "Home page"


if __name__ == "__main__":
    app.run(host='0.0.0.0')