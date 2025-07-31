import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from scrapy.http import HtmlResponse



class DuckSpider_selenium(scrapy.Spider):
    name = "duckselenium"
    allowed_domains = ["duckduckgo.com"]
    start_urls = ["https://duckduckgo.com"]
    
    
    def __init__(self, name = None, **kwargs):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver_path = "C:\\Users\\User\\Downloads\\chromedriver-win32\\chromedriver.exe"
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service= service, options= chrome_options)
        
    def parse(self, response):
        for url in self.start_urls:
            self.driver.get(url)
            
            sel_response = HtmlResponse(
                url = self.driver.current_url,
                body = self.driver.page_source,
                encoding = 'utf-8'
                
            )
            
            title = sel_response.xpath('//h2[@class="homepage-cta-section_title__yh7tH heading_heading2__WFJ4M heading_heading__yebkp"]//text()').get()
            print(title)
            yield {"title" : title}
     
    def closed(self, response):
        self.driver.quit()       
            
