import requests as req
import json

def get_photo(status):
    url = f'https://http.cat/{status}'
    if req.get(url).status_code != 200:
        url = url.replace(status, '404')
    return f'photo{url}'