def add(fridge, product, quantity):
    if product in fridge:
        fridge[product] += quantity
    else:
        fridge[product] = quantity

def remove(fridge, product, quantity):
    if product in fridge:
        fridge[product] -= quantity
    else:
        print('Poduct not in fridge')

def check_quantity(fridge, product):
    if product in fridge:
        quantity = fridge[product]
        print(quantity)
    else:
        print("Product not in fridge")
def check_recipe(fridge, recipe):
    missing_ingredients = {}
    for product_needed, quantity_needed in recipe.items():
        if product_needed in fridge:
            missing_quantity = quantity_needed - fridge[product_needed]
            if missing_quantity > 0:
                missing_ingredients[product_needed] = missing_quantity
        else:
            missing_ingredients[product_needed] = quantity_needed

    if missing_ingredients:
        print('Missing products: ')
        for product, quantity in missing_ingredients.items():
            print(f'{product}: {quantity}')
    else:
        print("You have the ingredients for the recipe")
    
fridge = {}
recipe = {"Cheese": 1, "Tomato": 2, "Olive": 20}
while True:
    print("Fridge\n1)Add\n2)Remove\n3)Check quantity\n4)Check recipe\n5)Display fridge\n0)Exit")
    choice = input("Pick a number: ")
    if choice not in range(0,6):
        print("Incorrect input")
    elif choice == 0:
        break
    elif choice == 1:
        product = input("Product: ")
        quantity = int(input("Quantity: "))
        add(fridge, product, quantity)
    elif choice == 2:
        product = input("Product: ")
        quantity = int(input("Quantity: "))
        remove(fridge, product, quantity)
    elif choice == 3:
        product = input("Product: ")
        check_quantity(fridge, product)
    elif choice == 4:
        check_recipe(fridge, recipe)
    elif choice == 5:
        for key, value in fridge.items():
            if value > 0:
                print(f"{key}: {value}")
            else:
                del key
   
 