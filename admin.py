from attractions import attractions
from my_trip import find_attraction, trips

def add_attraction():
    print("\n========== ADD ATTRACTION ==========")

    name = input("Name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    if find_attraction(name) is not None:
        print("This attraction already exists.")
        return

    governorate = input("Governorate: ").strip()
    category = input("Category: ").strip()

    try:
        ticket_price = float(input("Ticket price: "))

        if ticket_price < 0:
            print("Ticket price cannot be negative.")
            return

        rating = float(input("Rating (0 - 5): "))

        if rating < 0 or rating > 5:
            print("Rating must be between 0 and 5.")
            return

        visit_time = float(input("Visit time in hours: "))

        if visit_time <= 0:
            print("Visit time must be greater than 0.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    new_attraction = {
        "name": name,
        "governorate": governorate,
        "ticket_price": ticket_price,
        "rating": rating,
        "visit_time": visit_time,
        "category": category
    }

    attractions.append(new_attraction)
    print("Attraction added successfully.")

def update_attraction():
    print("\n========== UPDATE ATTRACTION ==========")

    name = input("Enter attraction name: ").strip()

    attraction = find_attraction(name)

    if attraction is None:
        print("Attraction not found.")
        return

    print("\nLeave a field empty to keep the current value.")

    new_name = input(
        f"Name [{attraction['name']}]: "
    ).strip()

    new_governorate = input(
        f"Governorate [{attraction['governorate']}]: "
    ).strip()

    new_category = input(
        f"Category [{attraction['category']}]: "
    ).strip()

    new_price = input(
        f"Ticket price [{attraction['ticket_price']}]: "
    ).strip()

    new_rating = input(
        f"Rating [{attraction['rating']}]: "
    ).strip()

    new_visit_time = input(
        f"Visit time [{attraction['visit_time']}]: "
    ).strip()

    if new_name != "":
        existing = find_attraction(new_name)

        if existing is not None and existing is not attraction:
            print("Another attraction already has this name.")
            return

        attraction["name"] = new_name

    if new_governorate != "":
        attraction["governorate"] = new_governorate

    if new_category != "":
        attraction["category"] = new_category

    if new_price != "":
        try:
            new_price = float(new_price)

            if new_price < 0:
                print("Ticket price cannot be negative.")
                return

            attraction["ticket_price"] = new_price

        except ValueError:
            print("Invalid ticket price.")
            return

    if new_rating != "":
        try:
            new_rating = float(new_rating)

            if new_rating < 0 or new_rating > 5:
                print("Rating must be between 0 and 5.")
                return

            attraction["rating"] = new_rating

        except ValueError:
            print("Invalid rating.")
            return

    if new_visit_time != "":
        try:
            new_visit_time = float(new_visit_time)

            if new_visit_time <= 0:
                print("Visit time must be greater than 0.")
                return

            attraction["visit_time"] = new_visit_time

        except ValueError:
            print("Invalid visit time.")
            return

    print("Attraction updated successfully.")

def delete_attraction():
    print("\n========== DELETE ATTRACTION ==========")

    name = input("Enter attraction name: ").strip()

    attraction = find_attraction(name)

    if attraction is None:
        print("Attraction not found.")
        return

    attractions.remove(attraction)

    # Remove it from users' trips
    for email in trips:
        if attraction in trips[email]:
            trips[email].remove(attraction)

    print("Attraction deleted successfully.")

def admin_page():
    while True:
        print("\n========== ADMIN ==========")
        print("1. Add Attraction")
        print("2. Update Attraction")
        print("3. Delete Attraction")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            add_attraction()
        elif choice == "2":
            update_attraction()
        elif choice == "3":
            delete_attraction()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")