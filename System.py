# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {}

# Function to add an item to the inventory
def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

# Function to view all items in the inventory
def view_inventory():
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
    else:
        print(f"Item '{item}' not found in the inventory.")

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        # Process the user's choice
        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
            print(f"{quantity} {item}(s) added to the inventory.")
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            item = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            update_item(item, quantity)
        elif choice == '4':
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()
