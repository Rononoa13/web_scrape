from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd



page_response = requests.get('http://annapurnapost.com/sitemap.xml')
soup =  BeautifulSoup(page_response.content, 'xml')


output_url = []

#print(soup.prettify())

for date in soup.find_all('lastmod'):
    print(date.text)



for url in soup.find_all('loc'):
    output_url.append(url.text)

#print(output_url)
# create new dataframe

dataframe = pd.DataFrame(output_url)
#print(dataframe)
dataframe.to_csv(r'/home/ed_666/Documents/Project_Scrape/aanapurna_dailyLink.csv', index = False)


    