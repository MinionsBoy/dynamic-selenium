import requests

BASE_URL = "https://automationexercise.com/api/"

def get_all_products(): 
    return requests.get(BASE_URL + "productsList")

def get_product_detail(product_id):
    return requests.get(BASE_URL + f"productDetails?id={product_id}")

def search_products(query):
    return requests.get(BASE_URL + f"searchProduct?search_product={query}")

def post_search_products(query):
    return requests.post(BASE_URL + "searchProduct", data={"search_product": query})

def post_search_products_no_param():
    return requests.post(BASE_URL + "searchProduct")

def get_all_brands():
    return requests.get(BASE_URL + "brandsList")

def put_all_brands():
    return requests.put(BASE_URL + "brandsList")

def get_all_categories():
    return requests.get(BASE_URL + "categoriesList")

def post_verify_login_valid(email, password):
    return requests.post(BASE_URL + "verifyLogin", data={"email": email, "password": password})

def post_verify_login_no_email(password):
    return requests.post(BASE_URL + "verifyLogin", data={"password": password})

def delete_verify_login(email, password):
    return requests.delete(BASE_URL + "verifyLogin", data={"email": email, "password": password})

def post_verify_login_invalid(email, password):
    return requests.post(BASE_URL + "verifyLogin", data={"email": email, "password": password})

def post_create_user(name, email, password):
    return requests.post(BASE_URL + "createAccount", data={"name": name, "email": email, "password": password})

def delete_user(email):
    return requests.delete(BASE_URL + "deleteAccount", data={"email": email})

def put_update_user(email, name=None, password=None):
    data = {"email": email}
    if name:
        data["name"] = name
    if password:
        data["password"] = password
    return requests.put(BASE_URL + "updateAccount", data=data)

def get_user_detail_by_email(email):
    return requests.get(BASE_URL + f"getUserDetailByEmail?email={email}")
