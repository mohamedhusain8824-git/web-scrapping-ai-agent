from tools.search import search_web
from tools.scraper import scrape_url
from agents.summarizer import summarize

query = input("Ask me anything: ")

print("\nSearching...\n")

urls = search_web(query)

all_text = ""

for url in urls:

    print(f"Scraping: {url}")

    text = scrape_url(url)

    if text:
        all_text += text[:2000]
        all_text += "\n\n"

print("\nGenerating AI Summary...\n")

result = summarize(all_text)

print(result)