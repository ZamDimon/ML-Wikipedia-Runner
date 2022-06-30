from internal.config import config

import requests
import re

# We will define this variable as global to avoid
# reading txt file while running the functions
most_frequent_words = config.most_frequent_words()
NO_CONTENT = 'No Content'


def page_content(response_json):
    pages = response_json["query"]["pages"]
    page = pages[0]
    if 'missing' in page:
        if page['missing'] is True:
            return NO_CONTENT

    revision = page["revisions"][0]
    content = revision["slots"]["main"]["content"]

    return content


def get(title):
    # Declare words_dictionary based on keys from most frequent statistics
    words_dictionary = dict.fromkeys(most_frequent_words, 0)

    # Compose API request string
    request_api = config.api_get_page().format(title)
    # Make request and get the corresponding response
    response = requests.get(request_api)
    # Convert it to json format
    response_json = response.json()

    # Get raw content
    content = page_content(response_json)

    # If content is missing, print it out
    if content == NO_CONTENT:
        return NO_CONTENT

    # Get array of words from the content
    words = re.findall(r'\w+', content)

    for word in words:
        # If word does not exist in dictionary, omit it. Otherwise, increment the value
        if word in words_dictionary:
            words_dictionary[word] += 1

    return words_dictionary.values()
