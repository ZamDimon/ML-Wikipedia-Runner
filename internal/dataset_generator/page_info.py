from internal.config import config

import requests
import re


def page_content(response_json):
    pages = response_json["query"]["pages"]
    page = pages[0]
    revision = page["revisions"][0]
    content = revision["slots"]["main"]["content"]

    return content


def get(title):
    page_info = []
    page_info_dictionary = {}

    # Make API request
    request_api = config.api_get_page().format(title)

    # Make request and get the corresponding response
    response = requests.get(request_api)
    # Convert it to json format
    response_json = response.json()

    # Get raw content
    content = page_content(response_json)
    # Get array of words from the content
    words = re.findall(r'\w+', content)

    for word in words:
        # If word already exists, increment the corresponding value in dictionary. Else initialize it
        if word in page_info_dictionary:
            page_info_dictionary[word] += 1
        else:
            page_info_dictionary[word] = 1

    for word in config.most_frequent_words():
        page_info.append(page_info_dictionary[word] if word in page_info_dictionary else 0)

    return page_info
