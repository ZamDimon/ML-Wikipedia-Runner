# Selenium imports
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# Internal imports
from internal.config import config
from internal.dataset_generator import csv_interactor
from internal.dataset_generator import pair

# Other
import time
import requests


def element_exists(driver, class_name):
    try:
        driver.find_element(By.CLASS_NAME, class_name)
    except NoSuchElementException:
        return False
    return True


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
    text_fields = driver.find_elements(By.CLASS_NAME, config.text_fields_class())

    # Clear text fields
    text_fields[0].clear()
    text_fields[1].clear()

    # Send random page to the text fields
    text_fields[0].send_keys(get_random_page())
    text_fields[1].send_keys(get_random_page())

    # Click the button
    button = driver.find_element(By.CLASS_NAME, config.button_class())
    button.click()

    # If button did not appear, the blocks haven't loaded yet
    while not element_exists(driver, config.blocks_class()):
        time.sleep(0.1)

    time.sleep(1)

    # Error button: sc-lmgQwP jMdJku
    # 1977–78 Penn State Nittany Lions basketball team and Jan de Wael I
    if element_exists(driver, "jMdJku"):
        click_button(driver)

    while contains_null(get_paths(driver)):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    paths = filter_paths(get_paths(driver))
    for path in paths:
        push_path(path)
    csv_interactor.write()
    click_button(driver)


def contains_null(array):
    for element in array:
        if len(element) == 0:
            return True
    return False


def get_paths(driver):
    paths = []
    blocks = driver.find_elements(By.CLASS_NAME, config.blocks_class())

    for block in blocks:
        path = []

        another_object = block.find_element(By.XPATH, './/*')
        path_objects = another_object.find_elements(By.TAG_NAME, "a")

        for path_object in path_objects:
            path.append(path_object.get_attribute("href").split('/wiki/')[1])

        paths.append(path)

    return paths


def filter_paths(paths):
    # If paths is either an empty set or a single-element set, return it
    if len(paths) <= 1:
        return paths

    filtered_paths = [paths[0]]
    for path in paths[1:]:
        if len(set(paths[0]) ^ set(path))/2 >= 3:
            filtered_paths.append(path)
    return filtered_paths


def push_path(path):
    for i in range(1, len(path)):
        csv_interactor.push_pair(pair.Pair(path[0], path[i], i))


def launch():
    print(config.driver_path())
    driver = webdriver.Firefox(executable_path=config.driver_path())
    driver.get(config.website_link())

    click_button(driver)

