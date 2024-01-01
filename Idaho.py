import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

driver = webdriver.Chrome()
action = ActionChains(driver)
driver.maximize_window()

def waitelem(links):
    timeout = 10
    a=1
    element_found = False
    while not element_found:
        try:
            # Wait until the element with id "myElement" appears
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH,links)))

            # If the element appears, set the flag to True and exit the loop
            element_found = True

            # Perform further actions with the element
            print("Element appeared!")
            # Additional code to interact with the element
        except:
            # Handle the exception when the element does not appear within the specified timeout
            print("Element not found. Retrying...")
            a=a+1
        if a ==3:
            element_found = True
        


def selection(xpaths, name):
    dropdown_element = driver.find_element(By.XPATH,xpaths)

    # Create a Select object with the dropdown element
    dropdown = Select(dropdown_element)

    dropdown.select_by_visible_text(name)

def actionss(xpaths):
    but = driver.find_element(By.XPATH,xpaths)
    action.move_to_element(but).perform()
    action.click(but).perform()
    
driver.get('https://idahostars.org/Families?page13735=1&size13735=48#Search')
# waitelem('//*[@id="angrid13735"]/div[3]/div[3]/div/table/tbody/tr[1]/td[11]/div[1]/button')
time.sleep(20)


all_links = []

x = 1
while x<=11:
    try:
        links = driver.find_elements(By.XPATH,'//*[@id="angrid13735"]/div[3]/div[3]/div/table/tbody/tr/td[11]/div[2]/button')
        for li in links:
            action.move_to_element(li).perform()
            action.click(li).perform()
            time.sleep(1)
            a_links = driver.find_element(By.XPATH,'//*[@id="angrid13735"]/div[3]/div[3]/div/table/tbody/tr/td/div/div/div[2]/div/a')
            all_links.append(a_links.get_attribute('href'))
        try:
            destination_element  = driver.find_element(By.XPATH,'//*[@id="angrid13735"]/div[3]/div[4]/div/div[1]/ul/li[3]/button/span')
            driver.execute_script("arguments[0].scrollIntoView();", destination_element)
        except:
            print("no more next Pages")
    except:
        print("something goes wrong")
    x = x+1
    
    actionss('//*[@id="angrid13735"]/div[3]/div[4]/div/div[1]/ul/li[3]/button/span')
    time.sleep(20)


print(len(all_links))

Name = []
Address = []
City = []
Zip_Code = []
Phone_Number = []
# License_Number = []
Email = []
Director_Name = []
Facility_Type = []
for l in all_links:
    time.sleep(5)
    try:
        n = driver.find_element(By.XPATH,'//*[@id="angrid13772"]/div[3]/div[2]/div[2]/div/div[1]/span/strong')
        Name.append(n.text)
    except:
        Name.append("Not Available")
    
    try:
        add = driver.find_element(By.XPATH,'//*[@id="angrid13772"]/div[3]/div[2]/div[2]/div/div[2]/div/span/div[1]/div[1]')
        ads = add.text
        ads = ads.split('\n')
        Address.append(ads[0])
        cit = ads[1]
        cit = cit.split(', ID ')
        License_Number = []
        City.append(cit[0])
        Zip_Code.append(cit[1])
        
        Phone_Number.append(ads[2])
        
        Email.append(ads[3])
    except:
        Address.append("Not Available")
        City.append("Not Available")
        Zip_Code.append("Not Available")
        Phone_Number.append("Not Available")
        Email.append("Not Available")
        
    try:
        dr = driver.find_element(By.XPATH,'//*[@id="angrid13772"]/div[3]/div[2]/div[2]/div/div[2]/div/span/div[2]/div[1]')
        dr = dr.text
        dr = dr.split("\n")
        Director_Name.append(dr[0])
        Facility_Type.append(dr[1])
    except:
        Director_Name.append("Not Available")
        Facility_Type.append("Not Available")
        
Data = {
    "Name":Name,
    "Address":Address,
    "City":City,
    "Zip Code":Zip_Code,
    "Phone Number":Phone_Number,
    "License Number":License_Number,
    "Email":Email,
    "Director Name":Director_Name,
    "Facility Type":Facility_Type
}
    
driver.quit()
    
    
    
    
    
    