from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, Route
from typing import List, Dict, Optional
import random, time

main_categories: List[str] = ["https://www.amazon.com/b?node=172282"]

temp_links: List[str] = []
gatheredItems: List[Dict] = []

def block_unneded_resources(route: Route):
    if route.request.resource_type in ["image", "font", "stylesheet"]:
        route.abort()
    else:
        route.continue_()

def get_page_content(page, url: str, retries: int = 3) -> Optional[str]:
    for attempt in range(retries):
        try:
            page.goto(url, wait_until="domcontentloaded", timeout = 30000)
            return page.content()
        except Exception as e:
            print(f"Error finding {url}: {e}")
            time.sleep(random.uniform(2,5))
    return None

#links-gathering pipeline
def get_links(htmlLink: str):
    base_url = "https://www.amazon.com"
    soup = BeautifulSoup(htmlLink, 'html.parser')

    try:
        department = soup.find_all('a', class_='dcl-product-link')
        for x in department:
            href = x.get('href')
            if href:
                department_string = (base_url + href).strip()
                temp_links.append(department_string)
    except AttributeError:
        department_string = "No links found"

#content-page pipeline
def get_content(htmlLink: str):
    item: Dict = {}
    soup = BeautifulSoup(htmlLink, 'html.parser')

    try:
        title = soup.find(attrs={"id": 'productTitle'})
        if title:
            title_value = title.string.strip()
    except AttributeError:
        title_value = "NA"
    item["productTitle"] = title_value

    try:
        price = soup.find(attrs={"class": 'aok-offscreen'})
        if price:
            price_value = price.string.strip()
    except AttributeError:
        price_value = "NA"
    item["productPrice"] = price_value

    try:
        ratings = soup.find(attrs={"class": 'a-icon-alt'})
        if ratings:
            ratings_value = ratings.string.strip()
    except AttributeError:
        ratings_value = "NA"
    item["productRatings"] = ratings_value

    subCategory_value = "NA"
    try:
        subCategory = soup.find(attrs={"aria-current": 'page'})
        if subCategory:
            subCategory_value = subCategory.string.strip()
    except AttributeError:
        subCategory_value = "NA"
    item["productSubCategory"] = subCategory_value

    mainCategory_value = "NA"
    try:
        mainCategory = soup.find(attrs={"class": 'a-link-normal a-color-tertiary'})
        if mainCategory:
            mainCategory_value = mainCategory.string.strip()
    except AttributeError:
        mainCategory_value = "NA"
    item["productMainCategory"] = mainCategory_value

    img_value = "NA"
    try:
        img = soup.find('img', id='landingImage').get('src')
        if img:
            img_value = img.strip()
    except AttributeError:
        img_value = "NA"
    item["productImg"] = img_value

    description_value = "NA"
    try:
        description = soup.find(attrs={"id": 'productDescription'}).find('span')
        if description:
            description_value = description.string.strip()
    except AttributeError:
        description_value = "NA"
    item["productDescription"] = description_value
    print(item)
    gatheredItems.append(item)

if __name__ == '__main__':
    print("Starting Scraper")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.route("**/*", block_unneded_resources)

        print("getting categories")
        for i in main_categories:
            category = get_page_content(page, i)
            if category:
                get_links(category)
        print("getting content...")
        for i in temp_links:
            htmlLink = get_page_content(page, i)
            if htmlLink:
                get_content(htmlLink)
            time.sleep(random.uniform(1,3))

        browser.close()

        print(gatheredItems)