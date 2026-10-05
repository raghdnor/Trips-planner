ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASSWORD = "admin123"

CATEGORIES = [
    "Museums",
    "Historical Sites",
    "Nature",
    "Adventure",
    "Cultural Attractions"
]

users = {
    ADMIN_EMAIL: {
        "name": "Administrator",
        "phone": "",
        "email": ADMIN_EMAIL,
        "gender": "",
        "governorate": "",
        "password": ADMIN_PASSWORD,
        "age": 0,
        "national_id": "",
        "role": "admin"
    }
}


def register_user():
    print("\n========== REGISTER ==========")

    name = input("Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip().lower()
    gender = input("Gender: ").strip()
    governorate = input("Governorate: ").strip()
    password = input("Password: ").strip()
    age = input("Age: ").strip()
    national_id = input("National ID: ").strip()

    if not name or not phone or not email or not gender or not governorate or not password or not age or not national_id:
        print("All fields are required.")
        return

    if email in users:
        print("This email is already registered.")
        return

    if not age.isdigit():
        print("Age must be a number.")
        return

    if int(age) <= 0:
        print("Age must be greater than 0.")
        return

    users[email] = {
        "name": name,
        "phone": phone,
        "email": email,
        "gender": gender,
        "governorate": governorate,
        "password": password,
        "age": int(age),
        "national_id": national_id,
        "role": "user"
    }

    print("Registration completed successfully.")


def login_user():
    print("\n========== LOGIN ==========")

    email = input("Email: ").strip().lower()
    password = input("Password: ").strip()

    if email not in users:
        print("Invalid email or password.")
        return None

    if users[email]["password"] != password:
        print("Invalid email or password.")
        return None

    print(f"\nWelcome, {users[email]['name']}!")
    return users[email]


def show_profile(user):
    print("\n========== MY PROFILE ==========")

    print("Name:", user["name"])
    print("Phone Number:", user["phone"])
    print("Email:", user["email"])
    print("Gender:", user["gender"])
    print("Governorate:", user["governorate"])
    print("Age:", user["age"])
    print("National ID:", user["national_id"])
    print("Role:", user["role"])


def show_categories(navigation):
    print("\n========== CATEGORIES ==========")

    for i in range(len(CATEGORIES)):
        print(f"{i + 1}. {CATEGORIES[i]}")

    print("0. Back")

    choice = input("Choose a category: ").strip()

    if choice == "0":
        return

    if not choice.isdigit():
        print("Invalid choice.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(CATEGORIES):
        print("Invalid choice.")
        return

    category = CATEGORIES[choice - 1]

    navigation.append(category)

    print(f"\nOpening category: {category}")
    print("Attractions module will be connected here.")

    input("\nPress Enter to return...")

    navigation.pop()


def home_page(user):
    navigation = ["Home"]

    while True:
        print("\n========== EGYPT EXPLORER ==========")
        print(f"Welcome, {user['name']}")

        print("\n1. Browse Categories")
        print("2. My Profile")
        print("3. Back")
        print("4. Logout")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            show_categories(navigation)

        elif choice == "2":
            navigation.append("Profile")

            show_profile(user)

            input("\nPress Enter to return...")

            navigation.pop()

        elif choice == "3":
            if len(navigation) > 1:
                navigation.pop()
                print(f"Back to: {navigation[-1]}")
            else:
                print("You are already on Home.")

        elif choice == "4":
            print("Logged out successfully.")
            return

        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n========== EGYPT EXPLORER ==========")

        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            user = login_user()

            if user is not None:
                home_page(user)

        elif choice == "2":
            register_user()

        elif choice == "3":
            print("Thank you for using Egypt Explorer.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()