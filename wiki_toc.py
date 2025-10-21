import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {
    "User-Agent": "DescriptiveBot/1.0 (https://github.com/yourprofile/email@example.com)"
}

url = "https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"
response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.text, 'lxml')

results = []

# Scrape all h2 & h3 sections as main headers
for header in soup.find_all(['h2', 'h3']):
    section = header.text.strip()
    # Find the next sibling elements until the next section header
    el = header.find_next_sibling()
    desc = []
    topics = []
    while el and el.name not in ['h2', 'h3']:
        # Collect paragraph descriptions
        if el.name == 'p':
            desc.append(el.text.strip())
        # Collect each bullet point in lists
        if el.name in ['ul', 'ol']:
            for li in el.find_all('li'):
                topics.append(li.text.strip())
        el = el.find_next_sibling()
    results.append({
        'section': section,
        'description': " ".join(desc),
        'topics': "; ".join(topics)
    })

# Print results
for item in results:
    print(f"Section: {item['section']}")
    print(f"Description: {item['description']}")
    print(f"Topics: {item['topics']}\n")

# Optional: Export to CSV
with open("gfg_python_tutorial.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ['section', 'description', 'topics']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in results:
        writer.writerow(item)
