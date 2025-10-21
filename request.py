import requests

url_to_parse = "https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
response = requests.get(url_to_parse, headers=headers)
print(response)
