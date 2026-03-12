import requests

def check_church(url):
    r = requests.get(url, stream=True, verify=False)

    if r.status_code == 200:
        return True
    else:
        return False    
