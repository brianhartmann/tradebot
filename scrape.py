import time 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By 
import os
from dotenv import load_dotenv
import dotenv
from algorithms import *

# Define the Chrome webdriver options
options = webdriver.ChromeOptions() 
options.add_argument("--headless") # Set the Chrome webdriver to run in headless mode for scalability

# By default, Selenium waits for all resources to download before taking actions.
# However, we don't need it as the page is populated with dynamically generated JavaScript code.
options.page_load_strategy = "none"

# Pass the defined options objects to initialize the web driver 
driver = Chrome(options=options) 
# Set an implicit wait of 5 seconds to allow time for elements to appear before throwing an exception
driver.implicitly_wait(5)
url = "https://www.quiverquant.com/congresstrading/politician/Nancy%20Pelosi-P000197" 
 
driver.get(url) 
time.sleep(3)

load_dotenv() #loads env file
id = os.getenv('last_order')
content = driver.find_element(By.CSS_SELECTOR, "table[class*='sortable paginated-table home-table'")
body = content.find_element(By.TAG_NAME, "tbody")
rows = body.find_elements(By.TAG_NAME, "tr")
new_id = 0
order_placed = False
row_count = 0
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    row = 0
    stock = 0
    order = 0
    date = 0
    seen = False
    for col in cols:
        a_tag = col.find_element(By.TAG_NAME, "a")
        if (row == 0):
            div = a_tag.find_element(By.TAG_NAME, "div")
            stock = div.find_element(By.TAG_NAME, "strong").get_attribute("textContent")
        elif(row == 1):
            order = a_tag.find_element(By.TAG_NAME, "strong").get_attribute("textContent").lower()
        elif(row == 3):
            date = a_tag.find_element(By.TAG_NAME, "strong").get_attribute("textContent")
            if (id == stock+order+date.replace(" ", "")):
                #we've hit the end
                seen = True
                print('There are no more trades to mimic. Stopping program...')
                break
            else:
                print(f'Placing a {order} order for {stock} reacting to the trade made by Pelosi on {date}')
                make_trade(stock, order)
                order_placed=True
        row+=1

    if (row_count == 0):
        new_id=stock+order+date.replace(" ", "")
        dotenv.set_key(dotenv.find_dotenv(), 'last_order', new_id)
    if (seen):
        if (order_placed):
            id = new_id
            print(f'Updated id to be {id}')
        break
    row_count+=1



