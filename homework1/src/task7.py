import requests

def check_website_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException:
        return None