import requests
from bs4 import BeautifulSoup
import json


def sample_scrapper():

    url = 'https://www.google.com/search?q=Python'
    html = requests.get(url).content
    bs_parsed = BeautifulSoup(html, 'html.parser')

    # Retrieve all h3
    tags = bs_parsed('h3')
    for tag in tags:
        print(tag.find('div').text)
        print(tag.parent)

# Compare price


def compare_prices(product_laughs, product_glomark):
    # TODO: Aquire the web pages which contain product Price
    product_laughs_page = requests.get(product_laughs).content
    product_glomark_page = requests.get(product_glomark).content

    bs_product_laughs = BeautifulSoup(product_laughs_page, 'html.parser')
    # bs_product_glomark_page = BeautifulSoup(product_glomark_page, 'html.parser')

    # print(bs_laughs_coconut_page.find(
    #     'div', {'class': 'product-shop-content'}))
    print(product_glomark_page.json())

    # TODO: LaughsSuper supermarket website provides the price in a span text.

    # TODO: Glomark supermarket website provides the data in jason format in an inline script.
    # You can use the json module to extract only the price

    # TODO: Parse the values as floats, and print them.

    # print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    # print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)

    # if(price_laughs>price_glomark):
    #     print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    # elif(price_laughs<price_glomark):
    #     print('Laughs is cheaper Rs.:',price_glomark - price_laughs)
    # else:
    #     print('Price is the same')


# compare_prices('https://scrape-sm1.github.io/site1/COCONUT%20market1super.html',
#                'https://glomark.lk/coconut/p/11624')

# response = requests.get('http://host1.open.uom.lk:8080/api/products')
# data = response.json()
# print(len(data['data']))

# response = requests.put("http://host1.open.uom.lk:8080/api/products",
#                         json={
#                             "id": 12452,
#                             "productName": "Araliya Basmathi Rice",
#                             "description": "White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
#                             "category": "Rice",
#                             "brand": "Araliya",
#                             "expiredDate": "2023.05.04",
#                             "manufacturedDate": "2022.02.20",
#                             "batchNumber": 324567,
#                             "unitPrice": 1020,
#                             "quantity": 200,
#                             "createdDate": "2022.02.24"
#                         },
#                         headers={"Content-Type": "application/json"},
#                         )

# print(response.json())

def compare_prices(product_laughs, product_glomark):
    # TODO: Aquire the web pages which contain product Price
    laughs_page = requests.get(product_laughs).content
    laughs_soup = BeautifulSoup(laughs_page, 'html.parser')
    glomark_page = requests.get(product_glomark).content
    glomark_soup = BeautifulSoup(glomark_page, 'html.parser')

    # TODO: LaughsSuper supermarket website provides the price in a span text.
    try:
        product_name_laughs = laughs_soup.find(
            'div', {'class': 'product-name'}).text.strip()
        price_laughs = float(laughs_soup.find(
            'span', {'class': 'regular-price'}).text.strip()[3:])

        # TODO: Glomark supermarket website provides the data in jason format in an inline script.
        # You can use the json module to extract only the price

        product_name_glomark = glomark_soup.find(
            'div', {'class': 'product-title'}).text.strip()
        price_glomark_string = glomark_soup.find(
            'script', {'type': 'application/ld+json'}).text.strip()
    except:
        print('Question author has goofed. Please report')
        return
    price_glomark_dic = json.loads(price_glomark_string)
    price_glomark = float(price_glomark_dic['offers'][0]['price'])

    # TODO: Parse the values as floats, and print them.

    print('Laughs  ', product_name_laughs, 'Rs.: ', price_laughs)
    print('Glomark ', product_name_glomark, 'Rs.: ', price_glomark)

    if (price_laughs > price_glomark):
        print('Glomark is cheaper Rs.:', price_laughs - price_glomark)
    elif (price_laughs < price_glomark):
        print('Laughs is cheaper Rs.:', price_glomark - price_laughs)
    else:
        print('Price is the same')


compare_prices('https://scrape-sm1.github.io/site1/COCONUT%20market1seuper.html',
               'https://glomark.lk/coconut/p/11624')
