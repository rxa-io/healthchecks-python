from requests import get

def start(url, timeout=5):
    try:
        get(url + '/start', timeout=timeout)
    except:
        pass

def finish(url):
    get(url)
