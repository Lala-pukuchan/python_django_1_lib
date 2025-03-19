#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup


def get_link(url):
    # get the page
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None, None
    except Exception as e:
        return None, None

    # use BeautifulSoup to parse the page
    soup = BeautifulSoup(response.text, "html.parser")

    # get title
    title_tag = soup.find("h1", id="firstHeading")
    if title_tag:
        title = title_tag.get_text()
    else:
        title = None

    # get url
    content_div = soup.find(id="mw-content-text")
    allLinks = content_div.select("p > a")
    for link in allLinks:
        if link.get("href") is not None:
            url = link["href"]
            if (
                url.startswith("/wiki/")
                and not url.startswith("/wiki/Special:")
                and not url.startswith("/wiki/Help:")
            ):
                return "https://en.wikipedia.org" + link["href"], title

    return None, title


def roads_to_philosophy(start_query):
    visited = []
    current_url = "https://en.wikipedia.org/wiki/" + start_query.replace(" ", "_")
    count = 0
    while True:
        if current_url in visited:
            print("It leads to an infinite loop !")
            return
        visited.append(current_url)
        next_link, title = get_link(current_url)
        if title:
            print(title)
        count += 1
        if title and title.lower() == "philosophy":
            print(f"{count} roads from {start_query} to philosophy !")
            return
        if not next_link:
            print("It's a dead end !")
            return
        current_url = next_link


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 roads_to_philosophy.py "search term"')
        sys.exit(1)
    query = sys.argv[1]
    roads_to_philosophy(query)


if __name__ == "__main__":
    main()
