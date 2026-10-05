from my_trip import trips

# transportation cost.

distances = {
    ("Cairo", "Giza"): 20,
    ("Cairo", "Alexandria"): 220,
    ("Cairo", "Faiyum"): 100,
    ("Cairo", "Luxor"): 650,
    ("Cairo", "Aswan"): 900,
    ("Cairo", "New Valley"): 600,
    ("Cairo", "South Sinai"): 500,
    ("Cairo", "Red Sea"): 450,

    ("Giza", "Alexandria"): 230,
    ("Giza", "Faiyum"): 110,
    ("Giza", "Luxor"): 640,
    ("Giza", "Aswan"): 890,

    ("Alexandria", "Faiyum"): 250,
    ("Alexandria", "Luxor"): 870,

    ("Luxor", "Aswan"): 240,

    ("South Sinai", "Red Sea"): 300
}

def get_distance(governorate1, governorate2):
    if governorate1 == governorate2:
        return 0

    if (governorate1, governorate2) in distances:
        return distances[(governorate1, governorate2)]

    if (governorate2, governorate1) in distances:
        return distances[(governorate2, governorate1)]

    return 0

def calculate_ticket_cost(email):
    if email not in trips:
        return 0

    total = 0
    for attraction in trips[email]:
        total += attraction["ticket_price"]

    return total

def calculate_transportation_cost(email):
    if email not in trips or len(trips[email]) < 2:
        return 0

    total_distance = 0
    for i in range(len(trips[email]) - 1):
        current_place = trips[email][i]["governorate"]
        next_place = trips[email][i + 1]["governorate"]

        total_distance += get_distance(
            current_place,
            next_place
        )

    cost_per_km = 5
    return total_distance * cost_per_km

def calculate_total_cost(email):
    ticket_cost = calculate_ticket_cost(email)
    transportation_cost = calculate_transportation_cost(email)
    return ticket_cost + transportation_cost

def final_summary(email):
    print("\n================================")
    print("         FINAL TRIP SUMMARY")
    print("================================")

    if email not in trips or len(trips[email]) == 0:
        print("Your trip is empty.")
        return

    print("\nSelected Attractions:")
    for attraction in trips[email]:
        print(
            "-",
            attraction["name"],
            "(",
            attraction["governorate"],
            ")"
        )

    ticket_cost = calculate_ticket_cost(email)
    transportation_cost = calculate_transportation_cost(email)
    total_cost = calculate_total_cost(email)

    print("\nTicket Cost:", ticket_cost, "EGP")
    print("Transportation Cost:", transportation_cost, "EGP")
    print("--------------------------------")
    print("Total Trip Cost:", total_cost, "EGP")