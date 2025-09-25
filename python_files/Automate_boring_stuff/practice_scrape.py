from bs4 import BeautifulSoup

# Load the local HTML file
with open("C:/Users/igoel/Desktop/AI_Learning/practise_code/python_files/Automate_boring_stuff/practise_webscapping.html", "r", encoding="utf-8") as f:
    html = f.read()


soup=BeautifulSoup(html,'html.parser')

# extract paragraphs

paragraphs=soup.select('p')
print('Paragraphs:')
for i,p in enumerate(paragraphs,1):
    print(f'{i}.{p.get_text()}')
print('\n'+'-'*50+'\n')

# extract headings

headings=soup.select('h1, h2, h3')
print('Headings:')
for h in headings:
    print(f'- {h.get_text()}')
print('\n'+'-'*50+'\n')

# extract links

links=soup.select('a')
print('Links:')
for a in links:
    print(f'{a.get_text()} -> {a.get('href')}')
print('\n'+'-'*50+'\n')

# Extract images

images=soup.select('img')
print('Images:')
for img in images:
    print(f'{img.get('alt')} -> {img.get('src')}')
print('\n'+'-'*50+'\n')

# extract list items

ul_items=soup.select('ul li')
ol_items=soup.select('ol li')

print('Unordered list items:')
for li in ul_items:
    print(f' - {li.get_text()}')

print('\n Ordered list items:')
for li in ol_items:
    print(f' - {li.get_text()}')
print('\n'+'-'*50+'\n')

# extract table data

table=soup.select_one('table')
rows=table.select('tr') # type: ignore

print('Table data:')
for row in rows:
    cols=row.select('th,td')
    row_data=[col.getText() for col in cols]
    print(row_data)
print('\n'+'-'*50+'\n')

