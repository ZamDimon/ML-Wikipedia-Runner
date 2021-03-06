import numpy
import matplotlib.pyplot as plt
import math
from internal.dataset_generator import csv_interactor_no_features
import collections

# Six degrees of Wikipedia data
NUMBER_OF_SAMPLES = 373017
SIX_DEGREES_DATA = numpy.array([524, 10216, 90068, 183172, 67754, 16317, 3738, 1228])

# Normalized array to be displayed on the chart
SIX_DEGREES_DATA_NORMALIZED = {}
for key, value in enumerate(SIX_DEGREES_DATA):
    SIX_DEGREES_DATA_NORMALIZED[str(key)] = value / NUMBER_OF_SAMPLES


def normal_distribution_function(val):
    sigma = 0.81
    return (1/(sigma*math.sqrt(2*math.pi))) * math.exp((-(val - 3)**2)/(2*(sigma**2)))


# Possible values: six_degrees, generator
def draw_chart(mode='six_degrees'):
    data_to_display = {}

    # Set data to display
    if mode == 'generator':
        data_to_display = csv_interactor_no_features.get_distance_distribution()
    elif mode == 'six_degrees':
        data_to_display = SIX_DEGREES_DATA_NORMALIZED

    # Add 0 if not present
    if '0' not in data_to_display:
        data_to_display['0'] = 0
    data_to_display = collections.OrderedDict(sorted(data_to_display.items()))

    # Plot the bar
    plt.grid(True, color='gray', linewidth='0.5', linestyle='--')
    plt.bar(data_to_display.keys(), data_to_display.values(), width=0.8, color=['#c5c9cb', '#979ea2', '#646f75'])

    # Plot the normal distribution
    first_key = int(list(data_to_display)[0])
    last_key = int(list(data_to_display)[-1])

    x_points = numpy.arange(first_key, last_key, 0.1)
    normal_distribution = numpy.frompyfunc(normal_distribution_function, 1, 1)
    y_points = normal_distribution(x_points)

    plt.plot(x_points, y_points, 'r--')

    title = "Dataset and normal distribution"
    plt.title(title)

    plt.show()