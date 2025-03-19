#!/usr/bin/env python3
import sys
import requests
import dewiki


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 request_wikipedia.py "search term"')
        print('Example Usage: python3 request_wikipedia.py "chocolatine"')
        sys.exit(1)

    # take the search term from the command line and create a filename
    query = sys.argv[1]
    filename = query.replace(" ", "_") + ".wiki"

    # API URL for parsing wikitext
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "parse",
        "page": query,
        "format": "json",
        "redirects": "true",
        "prop": "wikitext",
    }

    try:
        response = requests.get(url=URL, params=PARAMS)
        if response.status_code != 200:
            print("Error: Received status code", response.status_code)
            sys.exit(1)

        # get response data as JSON
        data = response.json()
        # check for errors in the response
        if "error" in data:
            print("Error:", data["error"]["info"])
            sys.exit(1)
        wiki_text = data["parse"]["wikitext"]["*"]

        # convert the wiki markup to plain text with dewiki
        plain_text = dewiki.from_string(wiki_text)
        if not plain_text.strip():
            print("No content found for query.")
            sys.exit(1)
        # output the plain text to a file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(plain_text)
        print(f"Result written to {filename}")
    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
