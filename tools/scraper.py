import trafilatura

def scrape_url(url):

    downloaded = trafilatura.fetch_url(url)

    if downloaded is None:
        return None

    text = trafilatura.extract(downloaded)

    return text


if __name__ == "__main__":

    url = "https://aiweekly.co/"

    content = scrape_url(url)

    print(content[:3000])