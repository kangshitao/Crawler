# beautiful soup4使用练习
import requests
from bs4 import BeautifulSoup

r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
print(demo)