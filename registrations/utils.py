from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_page(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_service = Service('C:/Driver/chromedriver.exe')

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get(url)
    page_source = driver.page_source
    driver.quit()
    return BeautifulSoup(page_source, 'lxml')

def get_product_name(page):
    product_title_element = page.find('span', {'id': 'productTitle'})

    if product_title_element:
        return product_title_element.text.strip()
    
    return None

def get_average_rating(page):
    average_rating_element = page.find('span', {'class': 'a-icon-alt'})
    if average_rating_element:
        return average_rating_element.text.strip().split(' ')[0]
    return None

def get_rating_breakdown(page):
    star_elements = page.find_all('span', {'class': '_cr-ratings-histogram_style_histogram-column-space__RKUAd'})
    breakdown = []
    
    for element in star_elements:
        if len(breakdown) == 5:
            break

        text = element.get_text(strip=True)

        if '%' in text:
            breakdown.append(text)

    return breakdown

def get_product_details(asin):
    url = f'https://www.amazon.in/dp/{asin}'
    page = get_page(url)

    product_name = get_product_name(page)
    average_rating = get_average_rating(page)
    rating_breakdown = get_rating_breakdown(page)

    data = {
        'product_name': product_name,
        'average_rating': average_rating,
        'rating_breakdown': rating_breakdown
    }
    print(data)

    return data