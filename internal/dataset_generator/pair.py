from internal.dataset_generator import page_info
NO_DATA = 'No Data'


class Pair:
    def __init__(self, title1, title2, distance):
        self.title1 = title1
        self.title2 = title2
        self.distance = distance

    def as_array(self):
        return [self.title1, self.title2, self.distance]

    def csv_data(self):
        # Get page contents
        page_info1 = page_info.get(self.title1)
        page_info2 = page_info.get(self.title2)

        # If one of the page infos is empty, omit them
        if page_info1 == page_info.NO_CONTENT or page_info2 == page_info.NO_CONTENT:
            return NO_DATA

        # First page info
        csv_data = [self.title1]
        for number in page_info1:
            csv_data.append(number)

        # Second page info
        csv_data.append(self.title2)
        for number in page_info2:
            csv_data.append(number)

        csv_data.append(self.distance)
        return csv_data
