# Goals:
# Extract all headings
# Extract all paragraphs containing the word “link”
# Extract all links and images with their attributes
# Convert the table into a list of dictionaries
# Extract all items in unordered and ordered lists
# Extract text from divs by class and id

import re
from bs4 import BeautifulSoup

with open('C:/Users/igoel/Desktop/AI_Learning/practise_code/python_files/Automate_boring_stuff/practise_webscapping.html','r',encoding='utf-8') as f:
    html=f.read()

soup=BeautifulSoup(html,'html.parser')

# All Headings
headings=soup.select('h1,h2,h3')
print('Headings:')
for h in headings:
    print('-',h.get_text())
print("\n" + "-"*50 + "\n")


# paragraphs containing links
para_with_links= [p for p in soup.select('p') if 'link' in p.text.lower()]
print('Paragraphs containing links:')

for p in para_with_links:
    print('-',p.get_text())
print("\n" + "-"*50 + "\n")


# Links and images
print('Links:')
links=soup.select('a')
for a in links:
    print(f'{a.get_text()} -> {a.get('href')}')

print('\n Images:')
images=soup.select('img')

for img in images:
    print(f'{img.get('alt')} -> {img.get('src')}')
print("\n" + "-"*50 + "\n")


# convert tables into list of dictionaries

tables=soup.find_all('table')
all_tables_data=[]

for table in tables:
    header=[th.text.strip() for th in table.find_all('th')] # type: ignore
    rows=[]
    for tr in table.find_all('tr'): # type: ignore
        cells=tr.find_all('td') # type: ignore
    
        if cells:
            row_data={header[i]: cells[i].text.strip() for i in range(0,len(cells))}
            rows.append(row_data)
    
    all_tables_data.append(rows)

print('\n Table Data:')

for table in all_tables_data:
    for row in table:
        print(row)


# Extract unordered and ordered list

ul_items=[li.text.strip() for ul in soup.find_all('ul') for li in ul.find_all('li')]
ol_items=[li.text.strip() for ol in soup.find_all('ol') for li in ol.find_all('li')]

print('\nUnordered List:')
for li in ul_items:
    print('-',li)

print('\nOrdered List:')
for li in ol_items:
    print('-',li)

# extract text from divs by class and id

divs_by_class=