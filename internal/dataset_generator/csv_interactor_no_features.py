import csv
import collections

# Internal imports
from internal.config import config
from internal.dataset_generator import pair

# Rows to be pushed into dataset
rows = []


def push_pair(pair):
    # Print that the pair was appended
    print('appended pair {} and {}'.format(pair.title1, pair.title2))
    rows.append(pair.as_array())


def write():
    global rows
    with open(config.dataset_path(), 'a', encoding='UTF8') as dataset:
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
        # Iterate over all experiments
        for experiment in csvreader:
            experiments.append(experiment)

    return experiments


def get_distance_distribution():
    distribution = {}
    elements_number = 0

    with open(config.dataset_path(), 'r') as dataset:
        # Initialize csv reader
        csvreader = csv.reader(dataset)
        # Omit the header
        next(csvreader)

        for experiment in csvreader:
            elements_number += 1
            distance = experiment[2]
            if distance in distribution.keys():
                distribution[distance] += 1
            else:
                distribution[distance] = 1

        for key in distribution:
            distribution[key] = distribution[key] / elements_number

        return collections.OrderedDict(sorted(distribution.items()))
