import matplotlib.pyplot as plt
from internal.dataset_generator import csv_interactor


def show_chart():
    distribution = csv_interactor.get_distance_distribution()
    print(distribution)

    # X-coordinates of left sides of bars
    left = []
    for key in distribution:
        left.append(key)

    # Heights of bars
    max_height = 500
    height = []

    for key in distribution:
        height.append(distribution[key] * max_height)

    # Labels for bars
    tick_label = []
    for key in distribution:
        tick_label.append(str(key))

    # Plotting a bar chart
    plt.bar(left, height, tick_label=tick_label,
            width=0.8, color=['red', 'green'])

    # Naming the x-axis
    plt.xlabel('Distance')
    # Naming the y-axis
    plt.ylabel('Number of pairs')
    # Plot title
    plt.title('Distances distribution')

    # Function to show the plot
    plt.show()
