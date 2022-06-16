from selenium import webdriver
import time
import requests

from internal.config import config


def get_random_page():
    # Send request and get the response
    response = requests.get(config.api_random_page())
    response_json = response.json()

    # Get pages from the response and the first key in the dictionary
    pages = response_json['query']['pages']
    first_key = next(iter(pages))

    # Return the title of the page
    return pages[first_key]['title']


def click_button(driver):
    # Get text fields
    text_fields = driver.find_elements_by_class_name(config.text_fields_class())

    # Clear text fields
    text_fields[0].clear()
    text_fields[1].clear()

    # Send random page to the text fields
    text_fields[0].send_keys(get_random_page())
    text_fields[1].send_keys(get_random_page())

    # Click the button
    button = driver.find_element_by_class_name(config.button_class())
    button.click()
    time.sleep(20)
    print(get_paths(driver))


def get_paths(driver):
    paths = []
    blocks = driver.find_elements_by_class_name(config.blocks_class())

    for block in blocks:
        path = []
        path_objects = block.find_element_by_css_selector("*").find_elements_by_tag_name("a")
        for path_object in path_objects:
            path.append(path_object.get_attribute("href"))

        paths.append(path)

    return paths


def launch():
    print(config.driver_path())
    driver = webdriver.Firefox(executable_path=config.driver_path())
    driver.get(config.website_link())

    click_button(driver)

