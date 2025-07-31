import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DuckSpider(scrapy.Spider):
    name = "duck"
    allowed_domains = ["duckduckgo.com"]
    start_urls = ["https://duckduckgo.com"]

    def __init__(self, name = None, **kwargs):
       
        driver_url = "C:\\Users\\User\\Downloads\\chromedriver-win32\\chromedriver.exe"
        service = Service(driver_url)
        self.driver = webdriver.Chrome(service= service)
        

    def parse(self, response):
        url = self.start_urls[0]
        self.driver.get(url)
        
        input_box = self.driver.find_element(By.ID, 'searchbox_input')
        search_btn = self.driver.find_element(By.CLASS_NAME,  "iconButton_button__A_Uiu.searchbox_searchButton__LxebD")
        
        input_box.send_keys("python")
        search_btn.click()
        

        WebDriverWait(self.driver , 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//span[@class="EKtkFWMYpwzMKOYr0GYm LQVY1Jpkk8nyJ6HBWKAk"]'))
        )
        titles_elements = self.driver.find_elements(By.XPATH, '//span[@class="EKtkFWMYpwzMKOYr0GYm LQVY1Jpkk8nyJ6HBWKAk"]')
        all_titles = [elem.text for elem in titles_elements]
        print("All Titles:", all_titles)

        
  
        self_response = HtmlResponse(
            url = self.driver.current_url,
            body = self.driver.page_source,
            encoding = 'utf-8'
        )
      

            
    def closed(self, reason):
        self.driver.quit()
