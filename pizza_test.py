pizza_type = ['napoletana', 'margherita', 'capricciosa']
pizza_toppings = ['mushrooms', 'olives', 'pineapple']
pizza_crust = ['thin', 'fluffy', 'classic']


pizza = {'pizza_type': 'none', 'pizza_toppings': 'none', 'pizza_crust': 'none'}

def pizza_type_program():
    requested_pizza_type = input(f"Hello! Please select from the available pizza types:\n{pizza_type[0].title()}\n{pizza_type[1].title()}\n{pizza_type[2].title()}\n:")
    if requested_pizza_type.lower() in pizza_type:
        pizza['pizza_type'] = requested_pizza_type
    else:
        print(f"Sorry, {requested_pizza_type.title()} is not available!")

while True:
    pizza_type_program()
    if pizza['pizza_type'].lower() not in pizza_type:
        print(pizza_type_program)
    elif pizza['pizza_type'].lower() in pizza_type:
        if input(f"Are you sure? (Y/N)\n:").strip().upper() == "Y":
            break

        
def toppings_program():
        requested_toppings = input(f"Please select from the available toppings:\n{pizza_toppings[0].title()}\n{pizza_toppings[1].title()}\n{pizza_toppings[2].title()}\nOR select 'none' if you don't want any\n:")
        if requested_toppings.lower() in pizza_toppings:
            pizza['pizza_toppings'] = requested_toppings
        elif requested_toppings.lower() == 'none':
            pizza['pizza_toppings'] = 'none'
        elif requested_toppings not in pizza_toppings:
            print(f"Sorry, {requested_toppings.title()} is not available!")
        

while True:
    toppings_program()
    if input(f"Are you sure? (Y/N)\n:").strip().upper() == "Y":
        break

    
print(f"Here's your {pizza['pizza_type']}")