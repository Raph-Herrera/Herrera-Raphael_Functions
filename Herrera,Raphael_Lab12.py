def display_menu():
    menu = {
        1: ("Sandwich", 69.99),
        2: ("Fries", 59.99),
        3: ("Nuggets", 94.99),
        4: ("Burger", 109.99),
        5: ("Hotdog", 89.99),
    }
    print("\nMenu:")
    for key, value in menu.items():
        print(f"{key}. {value[0]} - ₱{value[1]:.2f}")
    return menu

def order_selection(menu):
    while True:
        try:
            choice = int(input("\nEnter the number of your order: "))
            if choice in menu:
                print(f"You selected {menu[choice][0]} for ₱{menu[choice][1]:.2f}")
                return menu[choice]
            else:
                print("Invalid choice. Please select a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def process_payment(total_cost):
    while True:
        try:
            payment = float(input(f"\nTotal is ₱{total_cost:.2f}. Payment please!: "))
            if payment >= total_cost:
                change = payment - total_cost
                print(f"Thankyou! Here's your change, ₱{change:.2f}")
                break
            else:
                print(f"Please provide sufficient amount, you are ₱{total_cost - payment:.2f}", " short.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    print("Welcome to Raph's smol isnack store! What can I get ya?")
    menu = display_menu()
    selected = order_selection(menu)
    total_cost = selected[1]
    process_payment(total_cost)
    print("\nThank you and come again! Enjoy your isnack!")

if __name__ == "__main__":
    main()