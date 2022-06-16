import requests
import re

from internal.config import config


def page_content(response_json):
    pages = response_json["query"]["pages"]
    page = pages[0]
    revision = page["revisions"][0]
    content = revision["slots"]["main"]["content"]

    return content


def get(title):
    page_info = []
    page_info_dictionary = {}

    request_api = config.api_get_page().format(title)
    response = requests.get(request_api)
    response_json = response.json()

    content = page_content(response_json)
    words = re.findall(r'\w+', content)

    for word in words:
        if word in page_info_dictionary:
            page_info_dictionary[word] += 1
        else:
            page_info_dictionary[word] = 1

    for word in config.most_frequent_words():
        page_info.append(page_info_dictionary[word] if word in page_info_dictionary else 0)

    return page_info
