
from bs4 import BeautifulSoup

from selenium import webdriver

start_number = 95654
max_number = 95660

driver = webdriver.Chrome()

urls = [
    'http://annapurnapost.com/news/95654'
]


def get_txt_soup(text):
    text = str(text)
    _soup = BeautifulSoup(text, 'lxml')
    return _soup


if __name__ == '__main__':

    for url in urls:
        driver.get(url)

        page_response = driver.execute_script("return document.documentElement.outerHTML")
        driver.quit()

        soup = BeautifulSoup(page_response, 'lxml')

        data = soup.find_all('div', class_='detail-news')
        date = get_txt_soup(data).find('p', {'class': 'detail-time'}).text

        article = get_txt_soup(data).findAll('p', {'class': 'drop-cap change-font'})

        heading = get_txt_soup(data).find('h1').text

        section = get_txt_soup(data).find('div', {'class': 'no-work'})
        section = get_txt_soup(section).findAll('span')[1].text

        source = 'AnnapurnaPost'

        print(section.strip())
        print(date.strip())
        
        print(heading.strip())
        print(source.strip())
        print(article)