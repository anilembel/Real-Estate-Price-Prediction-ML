from get_links import *
from threads import * 
from cleaning import *

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import json
import requests
import numpy as np
from concurrent.futures import ThreadPoolExecutor

test = f"./links.txt"

def csv_file(datas):
    #using pandas to create a dataframe
    df = pd.DataFrame(datas)
    df.replace("", None, inplace=True)

    # Saving the dataframe into a CSV file 
    df.to_csv("property_data.csv", mode="a", header=None, index=False)
    return df

def main():
    #getting the link    
    get_links()
    #scraping and cleaning datas
    datas = clean_data()
    # creating csv
    csv_file(datas)
         
if __name__ == "__main__":
    main() 
