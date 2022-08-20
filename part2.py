from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import pandas as pd

df = pd.read_csv("job_cats_and_subcats.csv")
j = df.columns.to_list()[1:-1]

for job in j:
    try:
        time_to_load = 10
        url = "https://www.linkedin.com/home"
        options = Options()
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        # time.sleep(time_to_load)

        job_titles = []
        company_name = []
        location = []

        driver.find_element(By.XPATH, '/html/body/nav/ul/li[4]/a').click()
        time.sleep(time_to_load)
        driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input').send_keys(job)
        driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/section/section[2]/form/button').click()
        time.sleep(5)
        all_jobs = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[2]/ul')
        parsed_jobs = BeautifulSoup(all_jobs.get_attribute("innerHTML"),"html.parser")
        lis= parsed_jobs.find_all("li")

        for li in lis:
            info = li.text.split("\n")
            info = [x.strip() for x in info if(x.strip())]
            job_titles.append(info[0])
            company_name.append(info[2])
            location.append(info[3])

        df = pd.DataFrame({"job position":job_titles,"company":company_name,"location":location})
        df.to_csv(f"jobs_{job}.csv")
        driver.close()
    except:
        pass
