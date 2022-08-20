from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os
import pandas as pd

d = []
l = []
e = []
company_list = []

all_files = os.listdir()
for f in all_files:
    if("jobs" in f):
        temp = pd.read_csv(f)
        company_list = company_list+ temp["company"].to_list()

company_list = list(set(company_list))[0:2]
print(company_list)
for company in company_list:
    try:
        time_to_load = 10
        if(" " in company):
            company = ("-").join(company.split(" "))
        url = f"https://in.linkedin.com/company/{company}?trk=public_jobs_topcard-org-name"
        options = Options()
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(10)
        description = " "
        loc = " "
        emp = " "
        f = False
        try:
            description = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/section[1]/div/p').text
            loc = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/section[1]/div/dl/div[4]/dd').text
            emp = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/section[1]/div/dl/div[3]/dd').text
        except:
            driver.find_element(By.XPATH, '//*[@id="main-content"]/div/form/p/button').click()
            driver.find_element(By.XPATH, '//*[@id="session_key"]').send_keys("mhapsekartejas420@gmail.com")
            driver.find_element(By.XPATH, '//*[@id="session_password"]').send_keys("manju420")
            driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div/form/button').click()
            f = True

        if(f):
            description = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/section[1]/div/p').text
            loc = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/section[1]/div/dl/div[4]/dd').text
            emp = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/section[1]/div/dl/div[3]/dd').text
            f = True
        d.append(description)
        l.append(loc)
        e.append(emp)

        driver.close()
    except:
        pass

organized = {}
cats = {"comapny":company_list,"description":d,"location":l,"number of employees":e}

df = pd.DataFrame(organized)
df.to_csv("all_companies.csv")

