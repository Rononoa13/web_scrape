from bs4 import BeautifulSoup
import requests
import csv



page_response = requests.get('http://annapurnapost.com/sitemap.xml')
soup =  BeautifulSoup(page_response.content, 'xml')

output_url = []
print(soup.prettify())
for url in soup.find_all('loc'):
    output_url.append(url.text)
    print(url.text)

with open('url_output.text', 'a') as f:
    f.write("%s\n" % output_url)
    print("\n")


