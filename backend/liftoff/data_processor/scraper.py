import os
import sys
import django

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liftoff.settings')
django.setup()

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
from typing import List, Dict, Optional
import random, time

main_categories: List[str] = [ "https://www.amazon.com/b?node=7141123011"]

temp_links: List[str] = []

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

from data_processor.services import add_item
from data_processor.models import techItems, carParts, toys, clothesItems, forYouPage
def get_content(htmlLink: str):
    item: Dict = {}
    soup = BeautifulSoup(htmlLink, 'html.parser')

    try:
        title = soup.find(attrs={"id": 'productTitle'})
        if title:
            title_value = title.string.strip()
            title_value = title_value[:50]
        item["title"] = title_value
    except AttributeError:
        title_value = "NA"
    except UnboundLocalError:
        title_value = "NA"

    try:
        price = soup.find(attrs={"class": 'aok-offscreen'})
        if price:
            price_value = price.string.strip()
            price_value = price_value[:10]
        item["price"] = price_value
    except AttributeError:
        price_value = "NA"
    except UnboundLocalError:
        price_value = "NA"

    try:
        ratings = soup.find(attrs={"class": 'a-icon-alt'})
        if ratings:
            ratings_value = ratings.string.strip()
            ratings_value = ratings_value[:10]
        item["ratings"] = ratings_value
    except AttributeError:
        ratings_value = "NA"
    except UnboundLocalError:
        ratings_value = "NA"

    subCategory_value = "NA"
    try:
        subCategory = soup.find(attrs={"aria-current": 'page'})
        if subCategory:
            subCategory_value = subCategory.string.strip()
            subCategory_value = subCategory_value[:15]
        item["subCategory"] = subCategory_value
    except AttributeError:
        subCategory_value = "NA"
    except UnboundLocalError:
        subCategory_value = "NA"

    mainCategory_value = "NA"
    try:
        mainCategory = soup.find(attrs={"class": 'a-link-normal a-color-tertiary'})
        if mainCategory:
            mainCategory_value = mainCategory.string.strip()
            mainCategory_value = mainCategory_value[:15]
        item["mainCategory"] = mainCategory_value
    except AttributeError:
        mainCategory_value = "NA"
    except UnboundLocalError:
        mainCategory_value = "NA"

    img_value = "NA"
    try:
        img = soup.find('img', id='landingImage').get('src')
        if img:
            img_value = img.strip()
            img_value = img_value[:300]
        item["img_link"] = img_value
    except AttributeError:
        img_value = "NA"
    except UnboundLocalError:
        img_value = "NA"

    description_value = "NA"
    try:
        description = soup.find(attrs={"id": 'productDescription'}).find('span')
        if description:
            description_value = description.string.strip()
            description_value = description_value[:50]
        item["description"] = description_value
    except AttributeError:
        description_value = "NA"
    except UnboundLocalError:
        description_value = "NA"
    
    print("saving item: ", item.get("title"))
    main_category = item.get("mainCategory", "").lower()

    if main_category and "electronics" in main_category:
        model = techItems
    elif main_category and "automotive" in main_category:
        model = carParts
    elif main_category and "toys" in main_category:
        model = toys
    elif main_category and ("clothing" in main_category or "apparel" in main_category):
        model = clothesItems
    else:
        model = forYouPage
    
    obj, err = add_item(model, item)
    if err:
        print("error adding item: ", err)

if __name__ == '__main__':
    print("Starting Scraper")
    with Stealth().use_sync(sync_playwright()) as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.set_viewport_size({
            "width": random.randint(1100, 1920),
            "height": random.randint(900, 1080)
        })

        page.set_extra_http_headers({
            "User-Agent": random.choice([
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
                "(KHTML, like Gecko) Version/17.0 Safari/605.1.15",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            ]),
            "Accept-Language": "en-US,en;q=0.9"
        })
        
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
            time.sleep(random.uniform(2.5,6.5))

        browser.close()