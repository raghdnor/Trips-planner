from categories import *

def show_attraction_details(attraction):
    print("-" * 30)
    print("Name:", attraction["name"])
    print("Governorate:", attraction["governorate"])
    print("Ticket Price:", attraction["ticket_price"])
    print("Rating:", attraction["rating"])
    print("Visit Time:", attraction["visit_time"])
    print("Category:", attraction["category"])
    print("-" * 30)

def show_category_list(att):
    print("-" * 30)
    count = 1
    for a in att:
        print(count, a["name"], "-", a["ticket_price"], "EGP")
        count += 1
    print("-" * 30)