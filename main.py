# Importing the necessary classes from the products and store modules
from products import Product
from store import Store

# Setting up the initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = Store(product_list)


def start(store: Store):
    while True:
        print("\nWelcome to Best Buy!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please enter your choice (1-4): ")

        if choice == '1':
            products = store.get_all_products()
            print("\nList of all products in store:")
            for product in products:
                print(product.show())
        elif choice == '2':
            total_quantity = store.get_total_quantity()
            print(f"\nTotal amount in store: {total_quantity}")
        elif choice == '3':
            make_order(store)
        elif choice == '4':
            print("Thank you for visiting Best Buy!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def make_order(store: Store):
    print("\nMake an Order")
    products = store.get_all_products()
    shopping_list = []

    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.show()}")

    while True:
        try:
            product_choice = int(input("\nEnter the product number you want to buy (0 to finish): "))
            if product_choice == 0:
                break
            elif 1 <= product_choice <= len(products):
                quantity = int(input(f"Enter the quantity for {products[product_choice - 1].name}: "))
                shopping_list.append((products[product_choice - 1], quantity))
            else:
                print("Invalid product number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if shopping_list:
        try:
            total_cost = store.order(shopping_list)
            print(f"\nTotal cost of your order: {total_cost} dollars.")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("No products selected for the order.")


if __name__ == "__main__":
    start(best_buy)
