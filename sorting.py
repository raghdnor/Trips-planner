def quick_sort(items, key):
    if len(items) <= 1:
        return items

    pivot = items[0]
    less = []
    greater = []
    equal = []

    for item in items:
        if item[key] < pivot[key]:
            less.append(item)
        elif item[key] == pivot[key]:
            equal.append(item)
        else:
            greater.append(item)
    return quick_sort(less, key) + equal + quick_sort(greater, key)

def reverse_list(items):
    result = []
    for i in range(len(items), 0, -1):
        result.append(items[i - 1])
    return result

def sort_attractions(attractions_list, key, ascending=True):
    sorted_list = quick_sort(attractions_list, key)
    if not ascending:
        sorted_list = reverse_list(sorted_list)
    return sorted_list