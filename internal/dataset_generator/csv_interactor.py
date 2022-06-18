import csv
from internal.config import config

# Rows to be pushed into dataset
rows = []


def push_pair(pair):
    # Print that the pair was appended
    print('appended pair {} and {}'.format(pair.title1, pair.title2))
    rows.append(pair.csv_data())


def get_header():
    # Retrieve most frequent words
    most_frequents = config.most_frequent_words()

    # First page info
    header = ['name 1']
    for word in most_frequents:
        header.append(word + ' 1')

    # Second page info
    header.append('name 2')
    for word in most_frequents:
        header.append(word + ' 2')

    header.append('distance')
    return header


def write():
    global rows
    with open(config.dataset_path(), 'w', encoding='UTF8') as dataset:
        # Initialize writer
        writer = csv.writer(dataset)
        # Write all rows
        writer.writerows(rows)
    # Remove current rows
    rows = []


def read():
    # Initialize output array
    experiments = []
    with open(config.dataset_path(), 'r') as dataset:
        # Initialize csv reader
        csvreader = csv.reader(dataset)
        # Omit the header
        next(csvreader)
        for experiment in csvreader:
            experiments.append(experiment)

    return experiments
