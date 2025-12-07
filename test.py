import requests
from bs4 import BeautifulSoup as BS

url = "https://sinoptik.ua/ru/pohoda/kyiv"
class_ = "RSWdP9mW X6TmI5bI"
r = requests.get(url)
html = BS(r.text, "html.parser")
t = html.find(class_=class_).text

print(t)
with open("test.html", "w", encoding="utf-8") as f:
    f.writelines(str(html))