import math

from internal.dataset_generator import page_info


def get_input(title1, title2):
    result = []

    # Retrieving data from the pages
    page_info1 = page_info.get(title1)
    page_info2 = page_info.get(title2)

    # Adding to the result
    for word in page_info1:
        result.append(word)
    for word in page_info2:
        result.append(word)

    return result


# Namely, it is a modificated sigmoid: 2*sigmoid(x)-1
def sigmoid(x):
    return (1 - math.exp(-x)) / (1 + math.exp(-x))


# Interpolates two inputs according to the following rule:
# 1 and 1 give 1
# 1 and 0 or 0 and 1 give -1
# 0 and 0 give 0
def interpolate(x, y):
    return (sigmoid(x)*sigmoid(y)) - math.fabs(sigmoid(x) - sigmoid(y))

