import os

from selenium import webdriver
from bs4 import BeautifulSoup



# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.addArguments("start-maximized")
# chrome_options.addArguments("disable-infobars")
# chrome_options.addArguments("--disable-extensions")
# chrome_options.addArguments("--disable-gpu")
# chrome_options.addArguments("--no-sandbox")
driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)
driver.get('https://dnf.akaib.com/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.close()