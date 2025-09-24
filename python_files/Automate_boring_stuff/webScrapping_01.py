# ------Foundation-----------------------------------

# import webbrowser

# webbrowser.open('https://www.google.com')

# --------------------Requests---------------------------------

# import requests

# res = requests.get("https://automatetheboringstuff.com",verify=False)
# print(type(res))
# print(res.status_code)
# print(len(res.text))
# print(res.text[:500])

# --------------------Beautifulsoup4---------------------------------

import requests
from bs4 import BeautifulSoup

url = "http://automatetheboringstuff.com"

res=requests.get(url)
res.raise_for_status()

# parse with beautifulsoup

soup=BeautifulSoup(res.text,'html.parser')

# paragraphs=soup.select('p')

# print(f'Number of <p> tags found - {len(paragraphs)}')
# print('\n First paragraph -\n')
# print(paragraphs[0].get_text())

links=soup.select('a')
print(f'Number of links found - {len(links)}')
print('First 5 links -')
for link in links[:5]:
    href=link.get('href')
    text=link.get_text()
    print(f'Text -> {href}')