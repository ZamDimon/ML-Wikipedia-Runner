import yaml
import os
import platform
from pathlib import Path

script_path = Path(__file__).parent.parent.parent
config_path = os.path.join(script_path, 'config.yaml')

with open(config_path, 'r') as stream:
    config = yaml.safe_load(stream)


def driver_path():
    if platform.system() != "Darwin":
        return os.path.join(script_path, config['web_clicker']['driver_path'])
    else:
        return os.path.join(script_path, config['web_clicker']['driver_path_mac'])


def website_link():
    return config['web_clicker']['website_link']


def api_random_page():
    return config['web_clicker']['api_random_page']


def api_get_page():
    return config['web_clicker']['api_get_page']


def text_fields_class():
    return config['web_clicker']['text_fields_class']


def button_class():
    return config['web_clicker']['button_class']


def blocks_class():
    return config['web_clicker']['blocks_class']


def error_text_class():
    return config['web_clicker']['error_text_class']


def no_found_text_class():
    return config['web_clicker']['no_found_text_class']


def most_frequent_words():
    return open(os.path.join(script_path, config['dataset_generator']['most_frequent_words']), "r").read().splitlines()


def dataset_path():
    return os.path.join(script_path, config['dataset_generator']['dataset_path'])


def dataset_with_features_path():
    return os.path.join(script_path, config['dataset_generator']['dataset_with_features_path'])


def load_delay():
    return config['web_clicker']['load_delay']


def updating_frequency():
    return config['web_clicker']['updating_frequency']