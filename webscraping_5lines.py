import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Agent-Tina/1.0 (https://github.com/koushik1124/koushikyadagiri24@gmail.com)"
}

response = requests.get("https://www.geeksforgeeks.org/python/python-programming-language-tutorial/", headers=headers)
soup = BeautifulSoup(response.text, "lxml")

# Find the div containing the main article content, and then the first <p> inside it
main_content = soup.find("div", class_="text")
if not main_content:
    main_content = soup.find("article")  # Fallback, sometimes content wrapped in <article>

first_p = None
if main_content:
    first_p = main_content.find("p")
else:
    # As a final fallback, get the *second* <p> in the whole page (skip first)
    all_paragraphs = soup.find_all("p")
    if len(all_paragraphs) > 1:
        first_p = all_paragraphs[1]

if first_p:
    print(first_p.text.strip())
else:
    print("No valid <p> tag found in the main content area.")
