from attractions import attractions

categories = ["Museums", "Historical Sites", "Nature", "Adventure", "Cultural Attractions"]

def get_attractions_by_category(category_name):
    result = []
    for attraction in attractions:
        if attraction["category"] == category_name:
            result.append(attraction)
    return result