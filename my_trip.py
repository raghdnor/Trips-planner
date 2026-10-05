from attractions import attractions

trips = {}

def find_attraction(name):
    for attraction in attractions:
        if attraction["name"].lower() == name.lower():
            return attraction
    return None

def add_to_trip(email, name):
    attraction = find_attraction(name)

    if attraction is None:
        print("Attraction not found.")
        return False

    if email not in trips:
        trips[email] = []

    for item in trips[email]:
        if item["name"].lower() == name.lower():
            print("Attraction is already in your trip.")
            return False

    trips[email].append(attraction)
    print("Attraction added to your trip.")
    return True

def remove_from_trip(email, name):
    if email not in trips:
        print("Your trip is empty.")
        return False

    for attraction in trips[email]:
        if attraction["name"].lower() == name.lower():
            trips[email].remove(attraction)
            print("Attraction removed from your trip.")
            return True

    print("Attraction is not in your trip.")
    return False

def show_my_trip(email):
    if email not in trips or len(trips[email]) == 0:
        print("\nYour trip is empty.")
        return

    print("\n========== MY TRIP ==========")
    for i, attraction in enumerate(trips[email], start=1):
        print(f"\n{i}. {attraction['name']}")
        print(f"Governorate: {attraction['governorate']}")
        print(f"Ticket Price: {attraction['ticket_price']} EGP")
        print(f"Rating: {attraction['rating']}")
        print(f"Visit Time: {attraction['visit_time']} hours")
        print(f"Category: {attraction['category']}")

def my_trip_page(email):
    while True:
        print("\n========== MY TRIP ==========")
        print("1. Show My Trip")
        print("2. Add Attraction")
        print("3. Remove Attraction")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            show_my_trip(email)
        elif choice == "2":
            name = input("Enter attraction name: ")
            add_to_trip(email, name)
        elif choice == "3":
            name = input("Enter attraction name: ")
            remove_from_trip(email, name)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")