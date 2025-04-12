import requests
from bs4 import BeautifulSoup 


url= "https://www.jumia.co.ke/flash-sales/?srsltid=AfmBOopvMyF02YyRTxnBpwD_r7O63I877SjGiogZoTxVu8zUymaX1pg2"
response=requests.get(url)
print(response.status_code)

if response.status_code== 200:
    print("Page is ready for scraping")
else:
    print(f"Error {response.status_code}")

# print(response.text)
soup= BeautifulSoup(response.text, "html.parser")
deals =soup.find("section", class_="card -oh _fw -rad4")

print("Below are the deals available:")
products=deals.find_all("article", class_="prd _box col _hvr")
product_data=[]

for product in products:
    product_name= product.find("div", class_="name").text
    price=product.find("div", class_="prc").text
    discount_tag = product.find("div", class_="bdg _dsct")
    discount = discount_tag.text if discount_tag else ""

    details=({"product_name": product_name},
                            {"Price": price},
                            {"Discount": discount})
    product_data.append(details)
    print(details)
    







print("Below are the flash sales:")

flash_sales= soup.find("section", class_="card -fh")
flash_items=flash_sales.find_all("article", class_="prd _fb _p col c-prd")
items=[]

for item in flash_items:
    name=item.find("h3", class_="name").text
    item_price=item.find("div", class_="prc").text
    discount_amt = item.find("div", class_="bdg _dsct _sm")
    item_discount = discount_amt.text if discount_amt else ""
    rating = item.find("div", class_="stars _s").text if item.find("div", class_="stars _s") else ""
    

    flash_details=({"Item Name": name},
                   {"Price": item_price},
                   {"Discount": item_discount},
                   {"Rated": rating})
    

    items.append(flash_details)
    print(flash_details)
    








