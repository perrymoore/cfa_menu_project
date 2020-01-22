from menuclass import Food

name = {
    "1": "Chicken Sandwich", "2": "Chicken Sandwich Deluxe", "3": "Spicy Chicken Sandwich", "4":
        "Spicy Chicken Sandwich Deluxe", "5": "Grilled Chicken Sandwich"}
price = [3.75, 4.45, 3.99, 4.69, 5.15]
cals = [440, 500, 450, 540, 330]

menu = [Food("1", price[0], cals[0]), Food("2", price[1], cals[1]), Food("3", price[2], cals[2]),
        Food("4", price[3], cals[3]), Food("5", price[4], cals[4])]

def place_order(menu):
    total_cals = 0
    total_price = 0
    total_name = 0
    for meal in range(0,num_meals):
        order = int(input("Awesome, how can we help you?\n(order numbers 1-5): "))
        if order == 1:
            total_cals += menu[0][2]
        else:
            pass
    return total_cals



num_meals = int(input("How many sandwiches will you be ordering?"))
place_order(menu)
