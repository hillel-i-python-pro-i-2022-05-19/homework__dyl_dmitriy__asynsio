import asyncio
from typing import TypeAlias

import aiohttp
import bs4

T_URL: TypeAlias = str
T_URLS: TypeAlias = list[T_URL]
T_HTML_TEXT: TypeAlias = str


async def get_text_from_url(url: T_URL) -> T_HTML_TEXT:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def get_urls(text: T_HTML_TEXT) -> T_URLS:
    soup = bs4.BeautifulSoup(markup=text, features='html.parser')

    urls = []
    for link_element in soup.find_all('a'):
        url = link_element.get('href')
        urls.append(url)

    return urls


async def main():
    # url = 'https://example.com'
    url = 'https://rozetka.ua'

    text = await get_text_from_url(url)
    urls = get_urls(text=text)

    print(urls)


if __name__ == '__main__':
    asyncio.run(main())
