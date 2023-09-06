import pandas as pd
import requests
from bs4 import BeautifulSoup

Prod_name =[]
Price =[]
Desc =[]
# Review =[]

for i in range(2,12):
    url = "https://www.flipkart.com/search?q=laptop+under+80000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    box = soup.find("div",class_="_1YokD2 _3Mn1Gg")

    name = box.find_all("div", class_="_4rR01T")
    for i in name:
        n = i.text
        Prod_name.append(n)
    # print(Prod_name)

    price = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in price:
        n = i.text
        Price.append(n)
    # print(Price)

    # rev = box.find_all("div", class_="_3LWZlK")
    # for i in rev:
    #     n = i.text
    #     Review.append(n)
    # # print(Review)

    desc = box.find_all("ul", class_="_1xgFaf")
    for i in desc:
        n = i.text
        Desc.append(n)
    # print(Desc)
# print(len(Prod_name))

# print(len(Prod_name))
# print(len(Price))
# print(len(Desc))
df = pd.DataFrame({"Product Name":Prod_name,"Prices":Price,"Description":Desc})
# print(df)

df.to_csv("D:/POORNIMA CLASSES/7th Semester/ITS Data Engineering/Laptop_Under_80,000.csv")
print("CSV MADE")

# np = soup.find("a",class_ = "_1LKTO3").get("href")
# cnp = "https://www.flipkart.com"+np
# print(cnp)









    # url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text,"lxml")
    # print(soup)

