import yaml
import os
from pathlib import Path

script_path = Path(__file__).parent.parent.parent
config_path = os.path.join(script_path, 'config.yaml')

with open(config_path, 'r') as stream:
    config = yaml.safe_load(stream)


def driver_path():
    return os.path.join(script_path, config['web_clicker']['driver_path'])


def website_link():
    return config['web_clicker']['website_link']


def api_random_page():
    return config['web_clicker']['api_random_page']


def text_fields_class():
    return config['web_clicker']['text_fields_class']


def button_class():
    return config['web_clicker']['button_class']


def blocks_class():
    return config['web_clicker']['blocks_class']


def most_frequent_words():
    return open(os.path.join(script_path, config['dataset_generator']['most_frequent_words']), "r").read().splitlines()


def dataset_path():
    return os.path.join(script_path, config['dataset_generator']['dataset_path'])