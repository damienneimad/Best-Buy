# Importing the necessary classes from the products and store modules
from products import Product, NonStockedProduct, LimitedProduct
from store import Store
import promotions

# Setting up the initial stock of inventory
mac = Product("MacBook Air M2", price=1450, quantity=100)
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
pixel = Product("Google Pixel 7", price=500, quantity=250)

best_buy = Store([mac, bose])

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
mac.set_promotion(second_half_price)
bose.set_promotion(third_one_free)

# Test magic methods and properties
try:
    mac.price = -100  # Should give error
except ValueError as e:
    print(e)

print(mac)  # Should print `MacBook Air M2, Price: $1450 Quantity:100`
print(mac > bose)  # Should print True
print(mac in best_buy)  # Should print True
print(pixel in best_buy)  # Should print False

# Combine two stores
new_store = best_buy + Store([pixel])
print(pixel in new_store)  # Should print True
