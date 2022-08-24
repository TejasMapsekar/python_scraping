import os
import mysql.connector
import pandas as pd 

df = pd.read_csv("job_cats_and_subcats.csv")

cats = df.columns.to_list()
subcats = []
for c in df.columns.to_list()[1:]:
    subcats = subcats+df[c].to_list()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="scraping"
)

mycursor = mydb.cursor()

for cat in cats:
    try:
        mycursor.execute(f"INSERT INTO scraping.jobtypes1(category) VALUES ('{cat}');")
    except:
        print("error in cats")

for c in subcats:
    try:
        if(c != "-"):
            mycursor.execute(f"INSERT INTO scraping.jobtypes2(subcategory) VALUES('{c}');")
    except Exception as e:
        print("error in subcats")
        print(e)

for col in df.columns.to_list()[1:]:
    for entry in df[col]:
        try:
            mycursor.execute(f"INSERT INTO scraping.categoryandsubcategory(category,subcategory) VALUES ('{col}','{entry}');")
        except:
            print("error in table3")

comp = []
jobs = []
loc = []



l = os.listdir()
for f in l:
    if("jobs" in f):
        temp = pd.read_csv(f)
        comp = comp + temp["Company"].to_list()
        jobs = jobs + temp["Job position"].to_list()
        loc = loc + temp["Location"].to_list()

for name,location,job in zip(comp,jobs,loc):
    mycursor.execute(f"INSERT INTO scraping.jobs(name,location,job) VALUES ('{name}','{location}','{job}');")

df = pd.read_csv("all_companies.csv")

for row in df.values:
    for company,desc,loc,num in row:
        try:
            mycursor.execute(f"INSERT INTO scraping.company_details(company,description,location,numberofemp) VALUES ('{company}','{desc}','{loc}','{num}');")
        except:
            print("last_table_error")