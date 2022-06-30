import csv
import pandas

import requests.exceptions

from internal.dataset_generator import pair
from internal.config import config


def generate_dataset_saved(offset):
    with open(config.dataset_path(), 'r') as dataset:
        # Initialize csv reader
        dataset_reader = csv.reader(dataset)
        # Omit the header
        next(dataset_reader)
        # Put all dataset rows into an array
        dataset_rows = list(dataset_reader)
        with open(config.dataset_with_features_path(), 'a', encoding='UTF8') as dataset_with_features:
            # If offset is 0, we have to truncate the file
            if offset == 0:
                dataset_with_features.truncate(0)
            # Initialize dataset_with_features writer
            writer = csv.writer(dataset_with_features)
            # Iterate over dataset rows and append relevant information
            for i in range(offset, len(dataset_rows)):
                row = dataset_rows[i]
                row_pair = pair.Pair(row[0], row[1], int(row[2]))
                # Load csv data
                try:
                    csv_data = row_pair.csv_data()
                except requests.exceptions.ConnectionError:
                    print('Connection error. Retrying...')
                    generate_dataset_saved(i)
                # If there is no data in the pair, omit it
                if csv_data == pair.NO_DATA:
                    print('Cannot retrieve data for pair {}'.format(i))
                    continue

                writer.writerow(csv_data)
                print('added features to the row {}'.format(i))


def read_row(row_number):
    with open(config.dataset_with_features_path(), 'r') as dataset_with_features:
        # Define the reader
        reader = csv.reader(dataset_with_features)
        # Read rows as a list
        rows = list(reader)
        return rows[row_number]


def get_number_of_features():
    with open(config.dataset_with_features_path(), 'r') as dataset:
        reader = csv.reader(dataset)
        rows = list(reader)[0]
        return int((len(rows) - 3)/2)


# Find two sums of all most frequent words appearances
def read_row_sum(row_number):
    with open(config.dataset_with_features_path(), 'r') as dataset_with_features:
        # Define the reader
        reader = csv.reader(dataset_with_features)
        # Read rows as a list
        rows = list(reader)
        # Define sums
        sum1 = 0
        sum2 = 0
        for i in range(1, 1 + get_number_of_features()):
            sum1 += int(rows[row_number][i])
        for i in range(2 + get_number_of_features(), 2 + 2*get_number_of_features()):
            sum2 += int(rows[row_number][i])

        return sum1, sum2


def get_feature_header():
    # Retrieve most frequent words
    most_frequents = config.most_frequent_words()

    # First page info
    header = ['title_1']
    for word in most_frequents:
        header.append(word + '_1')

    # Second page info
    header.append('title_2')
    for word in most_frequents:
        header.append(word + '_2')

    header.append('distance')
    return header


def print_info():
    with open(config.dataset_with_features_path(), 'r') as dataset:
        # Define the reader
        reader = csv.reader(dataset)
        # Read rows as a list
        rows = list(reader)
        print("Number of rows:{}".format(len(rows)))
        print("Number of features:{}".format(len(rows[0])))

