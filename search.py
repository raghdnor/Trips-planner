from sorting import quick_sort

def binary_search(sorted_list, target):
    target = target.lower()
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        name = sorted_list[mid]["name"].lower()

        if name == target:
            return sorted_list[mid]
        elif name > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

def search_by_name(attractions_list, name):
    sorted_by_name = quick_sort(attractions_list, "name")
    return binary_search(sorted_by_name, name)