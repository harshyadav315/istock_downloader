import requests
from bs4 import BeautifulSoup
import re

target = input("Enter the image of istock URL : ")
if "istockphoto.com/photo/" not in target :
    print("Enter a valid Url...")
    exit()

url = "https://istock.7xm.xyz/get.php"

data = f"url={target}"

headers = {
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding" : "gzip, deflate, br",
    "accept-language" : "en-US,en;q=0.9",
    "cache-control" : "max-age=0",
    "Content-Type" : "application/x-www-form-urlencoded",
    "cookie" : "_ga=GA1.1.1861648104.1656132635; __qca=P0-1046793654-1656132636872; _ga_1JBPN4CCJ1=GS1.1.1656132635.1.1.1656133631.0; ezux_lpl_355945=1656133632061|108a6142-2ef6-49d2-4fff-27fdf6da1114|false; ezux_et_355945=3; ezux_tos_355945=269",
    "origin" : "https://istock.7xm.xyz",
    "referer" : "https://istock.7xm.xyz/index.php",
    "sec-fetch-dest" : "document",
    "sec-fetch-mode" : "navigate",
    "sec-fetch-site" : "same-origin",
    "sec-fetch-user" : "?1",
    "upgrade-insecure-requests" : "1",
    "user-agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
}

print("Please Wait ...")

res = requests.post(url,data=data,headers=headers)

data = res.content
# with open('res.txt','w') as f :
#     f.write(res.text)


css_selector = "body > main > section > div > div > div > li > a"

soup = BeautifulSoup(data,'lxml')
x = str(soup.select(css_selector)[0])
# print(x)

start = re.search('href="',x)
end = re.search('.jpg',x)
x = x[start.end():end.start()]
img_url = "https://istock.7xm.xyz/" + x +".jpg"

print(img_url)