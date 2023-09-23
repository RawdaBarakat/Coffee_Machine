class CoffeeMaker :
    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def report(self):
        """Prints a report of all resources."""
        print(f"the water : {self.resources['water']}")
        print(f"the milk : {self.resources['milk']}")
        print(f"the coffee : {self.resources['coffee']}")
    def is_resource_sufficient(self , drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self , order):
        for i in order.ingredients:
            self.resources[i] -= order.ingredients[i]
        print(f"here is your order : {order.name}")

class MoneyMachine :
    currency = "$"
    coins_value = {"quarters": 0.25,"dimes": 0.10,"nickles": 0.05,"pennies": 0.01}
    def __init__(self):
        self.profit = 0
        self.money_received  = 0

    def report(self):
        print(f"current profit : {self.currency}{self.profit}")

    #"""Returns the total calculated from coins inserted."""
    def coin_process(self):
        print('''\033[33m
                We accept the following coins:
                Quarters ($0.25), dimes ($0.10)
                nickles ($0.05), pennies ($0.01)\033[m
                ''')
        for i in self.coins_value:
            self.money_received += int(input(f"How many {i}? Please: ")) * self.coins_value[i]
        print(f"you have provided : {self.currency}{self.money_received}")
        return self.money_received

    #"""Returns True when payment is accepted, or False if insufficient."""
    def make_payment(self , cost):
        self.coin_process()
        if self.money_received >= cost :
            change = round(self.money_received - cost , 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else :
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False

class MenuItem:
    def __init__(self , name , water , milk,coffee , cost ):
        self.name = name
        self.cost = cost
        self.ingredients = {"water":water , "milk":milk , "coffee":coffee}

class Menu :
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    #"""Returns all the names of the available menu items"""
    def get_items(self):
        options = ""
        for i in self.menu:
            options += i.name
        return options

    def find_drink(self , order_name):
        for i in self.menu:
            if i.name == order_name:
                return order_name
            print("Sorry that item is not available.")

