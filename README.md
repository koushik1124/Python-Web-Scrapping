# 🕸️ Python Web Scraping Tutorial — GeeksforGeeks Example  

[![Python](https://img.shields.io/badge/Python-Web%20Scraping-blue?logo=python)](https://www.python.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-HTML%20Parsing-green)](https://www.crummy.com/software/BeautifulSoup/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red)

> 🚀 A beginner-friendly **Python web scraping** project using `Requests` and `BeautifulSoup` — demonstrating how to extract and export structured data from [GeeksforGeeks](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/) tutorials.


📚 Table of Contents

✨ Overview

⚡ Quick Start

🔁 Workflow

🧩 Libraries Used

⚙️ How It Works

🧭 BeautifulSoup Usage

📤 Exporting Data to CSV

🚀 Advanced Topics

📜 License

🔗 References

✨ Overview

This project demonstrates how to scrape GeeksforGeeks Python tutorials using Python.

You’ll learn how to:

Fetch web content using the requests library.

Parse and extract headings, paragraphs, and links using BeautifulSoup4.

Export structured results to a CSV file.

Implement best practices for ethical and efficient scraping.

⚡ Quick Start

Run this minimal version to see it in action 👇

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.geeksforgeeks.org/python/python-programming-language-tutorial/")
soup = BeautifulSoup(response.text, "lxml")
print(soup.find("h2").text)


Check the main script for detailed extraction logic, selectors, and CSV export examples.

🔁 Workflow
  ┌───────────┐
  │  Fetch    │  ← requests
  └────┬──────┘
       │
       ▼
  ┌───────────┐
  │  Parse    │  ← BeautifulSoup
  └────┬──────┘
       │
       ▼
  ┌───────────┐
  │  Export   │  ← CSV File
  └───────────┘

🧩 Libraries Used
Library	Purpose
requests	Fetches HTML content from a webpage
beautifulsoup4	Parses and extracts HTML tags
lxml	Fast HTML parser
csv	Exports structured data to a file
🛠️ Install Dependencies
pip install requests beautifulsoup4 lxml

⚙️ How It Works

Fetch: Uses requests.get() with a User-Agent header to retrieve page HTML.

Parse: Extracts <h2>, <p>, and list elements using BeautifulSoup’s tag-finding functions.

Export: Writes the structured content into a data.csv file.

💡 Tip: Add time.sleep(2) between requests to avoid being rate-limited.

🧭 BeautifulSoup Usage
Common Tag Operations
soup.h1
soup.find("p")
soup.find("div", class_="text")
soup.find_all("h2")
soup.find_all("li")


Navigate the DOM tree using .parent, .next_sibling, and .find_next() to collect related data.

📤 Exporting Data to CSV
import csv

with open("output.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Section", "Description", "Topics"])
    writer.writerow(["Introduction", "Overview of Python", "Basics, Syntax"])


Each CSV row contains a section name, description, and list of subtopics.

🚀 Advanced Topics

🧠 Dynamic Pages: Use tools like Selenium, Playwright, or requests-html for JavaScript-heavy websites.
🤝 Politeness: Always include headers and respect site robots.txt and ToS.
🔁 Customization: Change the url to target other tutorial pages or categories.

📜 License

Licensed under the MIT License
.
Please ensure compliance with GeeksforGeeks’ Terms of Service
 when scraping or redistributing content.

🔗 References

Python Requests Docs

BeautifulSoup4 Documentation

Python CSV Library

Web Scraping with Python – Real Python

🌟 Support & Feedback

If you found this useful, consider giving it a ⭐ on GitHub!
Your support helps me create more open-source tutorials and beginner-friendly projects
