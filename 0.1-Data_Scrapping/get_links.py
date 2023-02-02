from selenium import webdriver
from bs4 import BeautifulSoup
import re
import json
import requests
import numpy as npurl
from concurrent.futures import ThreadPoolExecutor
import itertools

# destination file of the URLs collected
test = f"links.txt"

# detect if the page contains a pagination
def pagination(url, driver):

    driver.get(url)
    
    soup=BeautifulSoup(driver.page_source, "html.parser")
    has_pagination = soup.find("lu", {"class":"pagination"})
    if has_pagination == -1:
        page_exists = False
    else:
        page_exists = True
    return page_exists

# navigates through the search result pages
def get_links():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(15)
    driver.implicitly_wait(15)

    list_of_links = []
    provinces = ["antwerp", "walloon-brabant", "flemish-brabant", "brussels", "west-flanders", "east-flanders", 
                "hainaut", "liege", "limburg", "luxembourg", "namur"]
    prov = 0
    province = provinces[prov]
    page_num = 1

    url = (
        "https://www.immoweb.be/en/search/house-and-apartment/for-sale/"+province+
        "/province?countries=BE&page="+str(page_num)+"&orderBy=relevance"
    )

# browse page 1 of each province, then page 2 and so on
    urls = []
    for (page_num, province) in itertools.product(range(1,334), provinces):
        urls.append("https://www.immoweb.be/en/search/house-and-apartment/for-sale/"+province+
        "/province?countries=BE&page="+str(page_num)+"&orderBy=relevance")
    for uri in urls:
        driver.get(uri)
        
# close webdriver
    driver.quit()
    driver.close()

    print(len(list_of_links))
    return list_of_links

# save the list of links into an external file
def link_file(datas):
    with open(test, 'a') as file:
        file.write(f'{datas}\n')

# call get_links without using threads
