from internal.dataset_generator import csv_interactor
from internal.dataset_generator import pair

csv_interactor.push_pair(pair.Pair("Hollow_Knight", "Albert_Einstein", 2))
csv_interactor.write()
print(csv_interactor.read()[0])