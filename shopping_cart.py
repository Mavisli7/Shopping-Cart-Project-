products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]
from time import strftime

def start_scanner():
    product_ids=[]
    while True:
        input_id=input("Please input a product identifier, or 'DONE' if there are no more items: ")

        if str(input_id).upper() != 'DONE':
            if not any(p for p in products if p["id"] == int(input_id)):
                print("Hey, are you sure that product identifier is correct? Please try again!")
                continue
            else:
                product_ids.append(int(input_id))
        else:
            break
    return(product_ids)

def name_prices(products_selected):
    return [product['name']+" ("+ "$" + '{0:.2f}'.format(product['price']) + ")" for product in products_selected]

def prices(products_selected):
    return [ product['price'] for product in products_selected]

product_ids=start_scanner()
products_selected = [next((p for p in products if p["id"] == product_id)) for product_id in product_ids]
c_items=name_prices(products_selected)
Subtotal=sum(prices(products_selected))
Tax=Subtotal*(8.875/100)
Total=Subtotal+Tax

print("--------------------------------")
print("MAVIS GROCERY STORE")
print("--------------------------------")
print("Web:www.mavis_store.com")
print("Phone: 1.123.445.7788")
print("Checkout Time: " + strftime("%Y-%m-%d %X"))
print("--------------------------------")
print("Shopping Cart Items: ")
[print("+ " +item) for item in c_items]
print("--------------------------------")
print("Subtotal: " + "$" +'%.2f' % Subtotal)
print("Plus NYC Sales Tax (8.875%): " + "$" + '%.2f' % Tax)
print("Total: " + "$"+ '%.2f' % Total)
print("--------------------------------")
print("Thanks for your business! Please come again.")
