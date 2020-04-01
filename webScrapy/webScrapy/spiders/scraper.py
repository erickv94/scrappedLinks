# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.support.ui import Select
from .. import settings
from selenium.common.exceptions import NoSuchElementException
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import datetime

 
class ScraperSpider(CrawlSpider):
    name = 'scraper'
    allowed_domains = ['www.greatplacetowork.com']
    search_url = 'https://www.greatplacetowork.com/forallsummit/speakers'
    start_urls = ['https://www.greatplacetowork.com/forallsummit/speakers']
    short_sleep=4
    medium_sleep=5
    long_sleep=10


    def parse(self, response):
        url = "https://www.greatplacetowork.com/forallsummit/speakers"
        chromedriver_path="C:/chromedriver"
        chrome_options = webdriver.ChromeOptions()
        partial_url="213129/agenda/speakers/"

        current_directory=str(Path(__file__).parent.parent.absolute())
        csv_dir=current_directory+"/data/"
        Path(csv_dir).mkdir(parents=True,exist_ok=True)
        #prefs = {"download.default_directory": path }
        #chrome_options.add_experimental_option('prefs',prefs)
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('window-size=1024x768')
        #chrome_options.add_argument("disable-gpu")
        #chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--start-maximized")
        #print(current_directory)

        #exec(open(current_directory+ '/'+'pdf_extraction.py').read())





        browser = webdriver.Chrome(chromedriver_path,chrome_options=chrome_options)
        
        browser.get(url)
        browser.get_cookies()
        sleep(self.medium_sleep)
        
        iframe=browser.find_element_by_tag_name('iframe')
        src_iframe=iframe.get_attribute("src")
        browser.get(src_iframe)
        browser.get_cookies()
        
        sleep(self.short_sleep)
        anchors=browser.find_elements_by_tag_name('a')
        list_urls=[]
        for url in anchors:
            href=url.get_attribute('href')
            if(href):
                list_urls.append(href)


        asserts_urls=[]
        for url in list_urls:
            if partial_url in url:
                asserts_urls.append(url)

        with open( csv_dir +"data"+".csv", "w") as csvFile:
            csv_output = csv.writer(csvFile)
            csv_output.writerow(["URLS with pattern {}".format(partial_url)])
            for url in asserts_urls:
                csv_output.writerow([url])
        browser.close()






                


