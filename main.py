import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome(executable_path="/Users/dipaolo/Downloads/chromedriver", options=options)

driver.get('http://time.is')
time.sleep(5)

driver.close()
