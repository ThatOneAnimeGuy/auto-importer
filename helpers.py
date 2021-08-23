import cloudscraper
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import random
import string

def get_value(d, key, default = None):
    try:
        return d[key]
    except:
        return default

def get_multi_level_value(d, *keys, **kwargs):
    default = get_value(kwargs, 'default')

    depth = len(keys)
    for i in range(depth):
        key = keys[i]
        d = get_value(d, key)
        if d is None and i < depth:
            return default
    return d

def create_scrapper_session(retries = 0, backoff_factor = 0.1, status_forcelist = (500, 502, 504, 423, 429)):
    session = cloudscraper.create_scraper()

    retry = Retry(
        total = retries,
        read = retries,
        connect = retries,
        backoff_factor = backoff_factor,
        status_forcelist = status_forcelist,
        allowed_methods = ['DELETE', 'GET', 'POST']
    )
    adapter = HTTPAdapter(max_retries = retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def get_random_ddg_cookie():
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
