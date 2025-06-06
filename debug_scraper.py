import cloudscraper
from bs4 import BeautifulSoup

def test_pagination():
    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True
        }
    )
    
    # Try accessing page 2 directly
    url = "https://pcgameskey.com/shop/page/2/"
    response = scraper.get(url)
    print(f"Status code for page 2: {response.status_code}")
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        products = soup.select('ul.products li.product, div.products div.product')
        print(f"Number of products found on page 2: {len(products)}")
        
        # Print product names if any found
        for product in products:
            name_elem = product.select_one('.woocommerce-loop-product__title, h2, h3 a')
            if name_elem:
                print(f"Product found: {name_elem.text.strip()}")

if __name__ == "__main__":
    test_pagination()
