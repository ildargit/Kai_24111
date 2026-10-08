import asyncio
import aiohttp
from bs4 import BeautifulSoup
import pandas as pd

default_url = "https://books.toscrape.com/catalogue/"

urls = [
    "a-light-in-the-attic_1000/index.html",
    "tipping-the-velvet_999/index.html",
    "soumission_998/index.html",
]


async def parse_product(session, url: str):
    headers = {"User-Agent": "Mozilla/5.0"}
    async with session.get(default_url + url, headers=headers) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")

        title = (
            soup.find("h1").get_text(strip=True) if soup.find("h1") else "Не найдено"
        )
        price_elem = soup.find("p", class_="price_color")
        price = price_elem.get_text(strip=True) if price_elem else "Нет цены"

        return {"URL": url, "Title": title, "Price": price}


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [parse_product(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    df = pd.DataFrame(results)
    print(df.to_string(index=False))


asyncio.run(main())
