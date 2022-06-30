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

