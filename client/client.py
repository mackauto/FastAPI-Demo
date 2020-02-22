from pprint import pprint
import requests

base_url = "http://127.0.0.1:8000"


def get_root():
    path = "/"
    url = base_url + path
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        pprint(response.json())


def get_async_root():
    path = "/async/"
    url = base_url + path
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        pprint(response.json())


def get_item():
    item_id = 1
    q = "query"
    path = "/items/{item_id}?q={q}".format(item_id=item_id, q=q)
    url = base_url + path
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        pprint(response.json())


def get_async_item():
    item_id = 1
    q = "query"
    path = "/async/items/{item_id}?q={q}".format(item_id=item_id, q=q)
    url = base_url + path
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        pprint(response.json())


if __name__ == '__main__':
    # get_root()
    # get_async_root()
    # get_item()
    # get_async_item()
    pass
