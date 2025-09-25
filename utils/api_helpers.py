import requests

BASE_URL = "https://automationexercise.com/api/"

def get_all_products():
    return requests.get(BASE_URL + "productsList")

def get_product_detail(product_id):
    return requests.get(BASE_URL + f"productDetails?id={product_id}")

def search_products(query):
    return requests.get(BASE_URL + f"searchProduct?search_product={query}")

def get_all_brands():
    return requests.get(BASE_URL + "brandsList")

def get_all_categories():
    return requests.get(BASE_URL + "categoriesList")
