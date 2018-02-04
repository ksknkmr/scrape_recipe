# Coding: utf-8

### 個別の材料をCSVに出力 ###

import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

#CSV操作
f = open("recipe_data.csv","a")
writer = csv.writer(f, lineterminator="\n")

#材料リストと量リスト
csv_list = []
quant_list = []

#スクレイピング準備
url = "XXXXX"
req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
res = urlopen(req)
html = res.read()
soup = BeautifulSoup(html,"html.parser")

recipe_main = soup.find("div", attrs={"id": "recipe-main"})
recipe_title = recipe_main.find("h1", attrs={"class": "recipe-title fn clearfix"})
csv_list.append(recipe_title.string)

#素材抽出
for ingredient in recipe_main.findAll("div", attrs={"class": "ingredient_name"}):
    csv_list.append(ingredient.text)
for quantity in recipe_main.findAll("div", attrs={"class":"ingredient_quantity amount"}):
    quant_list.append(quantity.text)

for i in range(len(quant_list)):
    csv_list[i + 1] += " " + quant_list[i]


writer.writerow(csv_list)
f.close()