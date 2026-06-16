from ddgs import DDGS

def web_search(query):

    urls = []

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)

        for result in results:
            print(result["title"])
            print(result["href"])
            print("-" * 50)

            urls.append(result["href"])

    return urls