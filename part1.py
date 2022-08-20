from bs4 import BeautifulSoup
import requests
import pandas as pd



url = "https://www.careerguide.com/career-options"

html = requests.get(url)

parsed = BeautifulSoup(html.content,"html.parser")

divs= parsed.find_all("div",{"class":"col-md-4"})

cats = {}

for e in divs:
    h2 = e.find("h2",{"class":"c-font-bold"})
    cat = None
    try:
        cat = h2.find("a").text
    except:
        cat = "some error occured"
    subcats = e.find("ul",{"class":"c-content-list-1 c-theme c-separator-dot"})
    # print(subcats)
    s = []
    if(subcats==None):
        subcats = []
    else:
        subcats = subcats.find_all("li")
    for t in subcats:
        s.append(t.find("a").text)

    cats[cat] = s

#data organising
organised = {}
max_len = 0

for col in cats.values():
    if(len(col)>max_len):
        max_len = len(col)

for k,v in cats.items():
    v.extend("-"*(max_len-len(v)))
    organised[k] = v

df = pd.DataFrame(organised)
print(df)
df.to_csv("job_cats_and_subcats.csv")


