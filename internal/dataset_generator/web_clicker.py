from selenium import webdriver
import time
import requests

website_link = 'https://www.sixdegreesofwikipedia.com/'
api_wiki_random_page = 'https://en.wikipedia.org/w/api.php?format=json&action=query&generator=random&grnnamespace=0&prop=revisions|images&rvprop=content&grnlimit=1'


def get_random_page():
    # Send request and get the response
    response = requests.get(api_wiki_random_page)
    response_json = response.json()

    # Get pages from the response and the first key in the dictionary
    pages = response_json['query']['pages']
    first_key = next(iter(pages))

    # Return the title of the page
    return pages[first_key]['title']


def click_button(driver):
    # Get text fields
    text_fields = driver.find_elements_by_class_name("react-autosuggest__input")

    # Clear text fields
    text_fields[0].clear()
    text_fields[1].clear()

    # Send random page to the text fields
    text_fields[0].send_keys(get_random_page())
    text_fields[1].send_keys(get_random_page())

    # Click the button
    button = driver.find_element_by_class_name("bojiJp")
    button.click()
    time.sleep(20)
    print(get_paths(driver))


def get_paths(driver):
    paths = []
    blocks = driver.find_elements_by_class_name("lazyload-wrapper ")

    for block in blocks:
        path = []
        path_objects = block.find_element_by_css_selector("*").find_elements_by_tag_name("a")
        for path_object in path_objects:
            path.append(path_object.get_attribute("href"))

        paths.append(path)

    return paths


driver = webdriver.Firefox(executable_path=r'driver/geckodriver')
driver.get(website_link)

click_button(driver)
#time.sleep(10)
#click_button(driver)
