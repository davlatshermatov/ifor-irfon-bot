import requests


async def select_all_categories():
    url = "https://ifor-irfon.herokuapp.com/api/categories/"
    r = requests.get(url)
    return r.json()


# async def select_all_subcategories(category_id):
#     url = "http://127.0.0.1:8000/api/sub-categories/"
#     r = requests.get(url, params={"category_id": category_id})
#     return r.json()


async def add_user(full_name, username, telegram_id):
    url = "https://ifor-irfon.herokuapp.com/api/bot-users/"
    r = requests.post(url, json={
        "full_name": full_name,
        "username": username,
        "telegram_id": telegram_id,
    })
    return r.json()


async def select_user(**kwargs):
    url = "https://ifor-irfon.herokuapp.com/api/bot-users/"
    r = requests.get(url, params=kwargs)
    return r.json()


async def get_products(category_id):
    url = "https://ifor-irfon.herokuapp.com/api/products/"
    r = requests.get(url, params={"category_id": category_id})
    return r.json()
