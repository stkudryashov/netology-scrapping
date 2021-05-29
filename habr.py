import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
if not response.ok:
    raise ValueError('no response')

soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('article')

for article in articles:
    title = article.find('a', class_='post__title_link')
    date = article.find('span', class_='post__time').text
    href = title.attrs.get('href')
    response = requests.get(href)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.find('div', class_='post__text').text

    for word in KEYWORDS:
        if word in text:
            print(f'{date} - {title.text} - {href}')
            break
