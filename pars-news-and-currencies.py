from bs4 import BeautifulSoup
import requests
import asyncio
import csv
import httpx
from urllib.parse import urljoin

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

async def parse_news(client: httpx.AsyncClient):
    URL = 'https://lenta.ru/'
    response = await client.get(URL, headers=HEADERS)

    if response.status_code != 200:
        print(f"Ошибка получения страницы! Статус-код: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    news_data = []
    news_titles_group = soup.select('.topnews__column .card-mini, .topnews__column .card-big')
    
    for news_card in news_titles_group:
        title_element = news_card.select_one('.card-mini__title, .card-big__title, h3')
        link_element = news_card.get('href')
        if title_element and link_element:
            title = title_element.text.strip()
            full_link = urljoin(URL, link_element)
            news_data.append({
                'title': title,
                'link': full_link
            })

    with open('lenta_news.csv', mode='w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        
        writer.writerow(['Заголовок', 'Ссылка на статью'])
        
        for item in news_data:
            writer.writerow([item['title'], item['link']])

    await asyncio.sleep(5)        
    print(f"\n======================\nПарсер новостей закончил работу!\nСпарсено новостей: {len(news_data)}. Данные сохранены в 'lenta_news.csv'\n======================\n")

async def parse_currencies(client: httpx.AsyncClient):
    URL = 'https://ru.myfin.by/currency/almetevsk'
    response = await client.get(URL, headers=HEADERS)

    if response.status_code != 200:
        print(f"Ошибка получения страницы! Статус-код: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    currencies_data = []
    rows = soup.select('.table-best tr')
    for row in rows:
        cols = row.select('td')
        if not cols:
            continue

        currency_name = cols[0].text.strip()
        currency_buy = cols[1].text.strip()
        currency_sell = cols[2].text.strip()
        currencies_data.append({
            'name': currency_name,
            'buy': currency_buy,
            'sell': currency_sell
        })

    with open('ru_myfin_currencies.csv', mode='w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        
        writer.writerow(['Валюта', 'Покупка', 'Продажа'])
            
        for item in currencies_data:
            writer.writerow([item['name'], item['buy'], item['sell']])      

    await asyncio.sleep(3)        
    print(f"\n======================\nПарсер валют закончил работу!\nСпарсено валют: {len(currencies_data)}. Данные сохранены в 'ru_myfin.csv'\n======================\n")

async def main():
    async with httpx.AsyncClient() as client:
        await asyncio.gather(
            parse_news(client),
            parse_currencies(client)
        )

asyncio.run(main())