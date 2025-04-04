from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


service = Service()

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

url = 'https://books.toscrape.com/'

driver.get(url)

titleElements = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]

bookslist = []

for title in titleElements:
    tmp = {}
    tmp["Titulo"] = title.get_attribute('title')
    title.click()
    tmp["Valor"] = driver.find_element(By.CLASS_NAME, "price_color").text
    tmp["Estoque"] = int(driver.find_element(By.CLASS_NAME, 'instock').text.replace('In stock (', '').replace(' available)', ''))
    bookslist.append(tmp) 
    driver.back()

df = pd.DataFrame(bookslist)
df.to_json("dados_livros.json", orient='records', indent=4, force_ascii=False)

driver.quit()
