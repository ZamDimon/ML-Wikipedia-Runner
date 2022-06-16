import csv
from internal.config import config

# Rows to be pushed into dataset
rows = []


def push_pair(pair):
    rows.append(pair.csv_data())


def get_header():
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
    with open(config.dataset_path(), 'w', encoding='UTF8') as dataset:
        writer = csv.writer(dataset)
        writer.writerow(get_header())
        writer.writerows(rows)


def read():
    experiments = []
    with open(config.dataset_path(), 'r') as dataset:
        csvreader = csv.reader(dataset)
        next(csvreader)
        for experiment in csvreader:
            print(experiment)
            experiments.append(experiment)

    return experiments
