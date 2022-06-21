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
import platform

UPDATING_FREQUENCY = 0.1
LOAD_DELAY = 1.5


def element_exists(driver, by, class_name):
    try:
        driver.find_element(by, class_name)
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
    while not element_exists(driver, By.CLASS_NAME, config.button_class()):
        time.sleep(UPDATING_FREQUENCY)

    # Wait for the elements to be loaded
    time.sleep(LOAD_DELAY)

    # If the error occurred, just click the button again
    if element_exists(driver, By.CLASS_NAME, config.error_text_class()) or element_exists(driver, By.XPATH, "//*[text()='No path']"):
        click_button(driver)

    # Wait for blocks to be loaded
    while not element_exists(driver, By.CLASS_NAME, config.blocks_class()):
        time.sleep(UPDATING_FREQUENCY)

    # Wait a bit more to assure that everything is uploaded
    time.sleep(LOAD_DELAY)

    # If the array was not fully loaded, scroll down and update elements
    while contains_empty(get_paths(driver)):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Get all paths
    paths = get_paths(driver)
    df = [dict(), dict()]
    for path in paths:
        push_path(path, df)

    csv_interactor.write()

    # Click button again and repeat the process
    click_button(driver)


def contains_empty(array):
    for element in array:
        # If array is empty
        if len(element) == 0:
            return True

    return False


def get_paths(driver):
    paths = []
    # Find block elements
    blocks = driver.find_elements(By.CLASS_NAME, config.blocks_class())

    for block in blocks:
        path = []

        # Find child div for the block (which in turn contains all hrefs)
        child_div = block.find_element(By.XPATH, './/*')
        path_objects = child_div.find_elements(By.TAG_NAME, "a")

        for path_object in path_objects:
            # Get href attribute to retrieve a link
            path.append(path_object.get_attribute("href").split('/wiki/')[1])

        paths.append(path)

    return paths


def push_path(path, df):
    limit = 3

    for i in range(0, len(path)):
        for j in range(i+1, len(path)):
            if df[0].get(path[i], 0) < limit and df[1].get(path[j], 0) < limit:
                csv_interactor.push_pair(pair.Pair(path[i], path[j], j-i))
                df[0][path[i]] = df[0].get(path[i], 0) + 1
                df[1][path[j]] = df[1].get(path[j], 0) + 1


def launch():
    # Initialize a driver
    driver = webdriver.Firefox(executable_path=config.driver_path())
    # Open a page
    driver.get(config.website_link())
    # Click the button
    click_button(driver)

