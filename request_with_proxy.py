import requests

def request_url_with_proxy(url, proxy):
    try:
        response = requests.get(url, proxies=proxy, timeout=10)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

url = "http://example.com"
proxy = {
    "http": "http://10.10.1.10:3128"
}

response = request_url_with_proxy(url, proxy)

if response:
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.text[:100]}...")