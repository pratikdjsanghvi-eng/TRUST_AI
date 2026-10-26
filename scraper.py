import requests
from bs4 import BeautifulSoup


def scrape_product(url: str):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/153.0 Safari/537.36"
        )
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    title = None

    h1 = soup.find("h1")

    if h1:
        title = h1.get_text(
            " ",
            strip=True
        )

    elif soup.title:
        title = soup.title.get_text(
            " ",
            strip=True
        )

    description = None

    meta = soup.find(
        "meta",
        attrs={"name": "description"}
    )

    if meta:
        description = meta.get("content")

    price = None

    price_selectors = [
        '[itemprop="price"]',
        '.price',
        '.product-price',
        '[class*="price"]'
    ]

    for selector in price_selectors:

        element = soup.select_one(selector)

        if element:
            price = element.get_text(
                " ",
                strip=True
            )
            break

    return {
        "url": url,
        "title": title,
        "price": price,
        "seller": None,
        "description": description,
        "ingredients": None
    }