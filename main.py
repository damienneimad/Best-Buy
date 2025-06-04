from products import LimitedProduct, NonStockedProduct, Product
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree
from store import Store


# Set up products
mac = Product("MacBook Air M2", price=1450, quantity=100)
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
pixel = Product("Google Pixel 7", price=500, quantity=250)
usb_cable = NonStockedProduct("USB-C Charging Cable", price=10)
paper = LimitedProduct("Printer Paper", price=5, quantity=200, maximum=5)

store = Store([mac, bose, pixel, usb_cable, paper])

# Promotions
second_half_price = SecondHalfPrice("Second half price")
third_one_free = ThirdOneFree("Buy 2 Get 1")
thirty_percent = PercentDiscount("30% off", percent=30)

mac.set_promotion(second_half_price)
bose.set_promotion(third_one_free)
paper.set_promotion(thirty_percent)


def list_products():
    for idx, product in enumerate(store.get_all_products(), start=1):
        print(f"{idx}. {product}")


def make_order():
    cart = []
    while True:
        list_products()
        choice = input("Enter product number to buy (or press Enter to finish): ")
        if not choice:
            break
        idx = int(choice) - 1
        quantity = int(input("Quantity: "))
        product = store.get_all_products()[idx]
        cart.append((product, quantity))
    if cart:
        total = store.order(cart)
        print(f"Order made! Total paid: ${total:.2f}")


def main():
    actions = {
        "1": list_products,
        "2": lambda: print(f"Total quantity in store: {store.get_total_quantity()}") ,
        "3": make_order,
    }
    while True:
        print("\n== Best Buy Store ==")
        print("1. List all products")
        print("2. Show total quantity")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Choose an action: ")
        if choice == "4":
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
