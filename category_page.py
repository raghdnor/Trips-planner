from categories import get_attractions_by_category
from details import show_category_list, show_attraction_details
from sorting import sort_attractions
from search import search_by_name

def category_page(category_name):
    current_list = get_attractions_by_category(category_name)

    while True:
        print("\n=== " + category_name + " ===")
        show_category_list(current_list)
        print("1. Default order")
        print("2. Sort by price (low to high)")
        print("3. Sort by price (high to low)")
        print("4. Sort by rating (high to low)  ")
        print("5. Sort by rating (low to high)  ")
        print("6. Search by name")
        print("7. View details of an attraction")
        print("0. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            current_list = get_attractions_by_category(category_name)
        elif choice == "2":
            current_list = sort_attractions(current_list, "ticket_price")
        elif choice == "3":
            current_list = sort_attractions(
                current_list, "ticket_price", ascending=False
            )
        elif choice == "4":

            current_list = sort_attractions(
                current_list, "rating", ascending=False
            )
        elif choice == "5":

            current_list = sort_attractions(current_list, "rating")
        elif choice == "6":
            name = input("Enter attraction name: ")
            att = search_by_name(current_list, name)
            if att is not None:
                show_attraction_details(att)
            else:
                print("Not found.")
        elif choice == "7":
            try:
                number = int(input("Enter attraction number: ").strip())
                if number <= 0 or number > len(current_list):
                    print("Invalid number.")
                else:
                    show_attraction_details(current_list[number - 1])
            except ValueError:
                print("Invalid number.")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    category_page("Museums")