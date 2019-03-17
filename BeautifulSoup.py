from bs4 import BeautifulSoup
import requests
url=input("your_url")
r=requests.get("your_url")
data=r.text
print(data)
soup=BeautifulSoup(data)
print(soup)
for i in soup.find_all("img"):
    print(i.get("img"))
