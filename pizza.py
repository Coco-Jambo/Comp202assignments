#Réda Alidrissi-Omari
#261068776

import math

PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED = 4.0
PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED = 3.0
SPECIAL_INGREDIENT = "guacamole"
SPECIAL_INGREDIENT_COST = 19.99
FAIR = True

def get_pizza_area(diameter):
    """(float)->float 
    Returns the area of the pizza using a positive diameter
    
    >>> get_pizza_area(6)
    28.274333882308138
    >>> get_pizza_area(2)
    3.141592653589793
    >>> get_pizza_area(3.5)
    9.62112750161874
    """
    
    area = (diameter/2)**2*math.pi
    return area

def get_fair_quantity(diameter1, diameter2):
    """(float,float)->int
    Returns the minimum number of pizzas with the smaller area
    that must be ordered to get at least the same area of the
    bigger pizza, the big and small pizzas could have either
    diameter1 or diameter2, which are both positive floating point numbers

    >>> get_fair_quantity(14,3)
    22
    >>> get_fair_quantity(5,3)
    3
    >>> get_fair_quantity(5,5)
    1
    """
        
    if(get_pizza_area(diameter1) >= get_pizza_area(diameter2)):
        bigger_pizza = get_pizza_area(diameter1)
        smaller_pizza = get_pizza_area(diameter2)
    else:
        bigger_pizza = get_pizza_area(diameter2)
        smaller_pizza = get_pizza_area(diameter1)
    
    x=0
    quantity = smaller_pizza
    while quantity < bigger_pizza:
        quantity = x * smaller_pizza
        x += 1
    x-=1
    
    if FAIR == False:
        return round(1.5*x, 2)
    else:
        return x
          
def pizza_formula(d_large, d_small, c_large, c_small, n_small):
    """(float,float,float,float)->float
    Returns the one missing value rounded to two decimal places
    which could be d_large, d_small, c_large, c_small or n_small
    that is of value -1, using the other inputs to find it, which
    are positive floating point numbers
    
    >>> pizza_formula(12.0, 6.0, 10.0, -1, 2)
    5.0
    >>>pizza_formula(29.93, 8.0, 7.0, 2, -1)
    4
    >>> pizza_formula(-1,6,10,5,2)
    12.0
    """
    
    area_large = get_pizza_area(d_large)
    area_small = get_pizza_area(d_small)
    
    if d_large == -1:
        area_large = (c_large*n_small*area_small)/c_small
        missing_value = math.sqrt(area_large*4/math.pi) 
    
    elif d_small == -1:
        area_small = (c_small*area_large)/(n_small*c_large)
        missing_value = math.sqrt(area_small*4/math.pi) 
    
    elif c_large == -1:
        missing_value = (area_large*c_small)/(n_small*area_small)
    
    elif c_small == -1:
        missing_value = (area_small*c_large*n_small)/(area_large)
    
    elif n_small == -1:
        missing_value = get_fair_quantity(d_large, d_small)
        
    return round(missing_value,2)
    

def get_pizza_cake_cost(base_diameter, height_per_level):
    """(int,float)->float
    Returns the cost of a multi-layered pizza cake, rounded to two
    decimal figures, where the cost of one layer of pizza is
    calculated using the base_diameter and the height_per_level, which
    are both positive floating point numbers
    
    >>> get_pizza_cake_cost(2, 1)
    15.71
    >>> get_pizza_cake_cost(5, 2)
    345.58
    >>> get_pizza_cake_cost(12, 1)
    2042.04
    """
    
    previous_pizza_cost=0
    total_pizza_cake_cost=0
    
    while base_diameter >= 1:
        pizza_area = get_pizza_area(base_diameter)
        pizza_cost = pizza_area*height_per_level*PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED
        
        total_pizza_cake_cost = previous_pizza_cost+ pizza_cost
        
        previous_pizza_cost = total_pizza_cake_cost
        base_diameter -= 1
    
    if FAIR == False:
        return round(1.5*total_pizza_cake_cost, 2)
        
    return round(total_pizza_cake_cost, 2) 

def get_pizza_poutine_cost(diameter, height):
    """(int, float)-> float
    Returns the cost of a pizza poutine, rounded to 2 decimal
    figures, using diameter, a positive integer, and height, a positive
    floating point number
    
    >>> get_pizza_poutine_cost(2,1)
    9.42
    >>> get_pizza_poutine_cost(3,1)
    21.21
    >>> get_pizza_poutine_cost(5,2)
    117.81
    """
 
    poutine_volume = get_pizza_area(diameter) * height
    poutine_cost = poutine_volume * PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED
    
    if FAIR == False:
        return round(1.5*poutine_cost, 2)
    
    return round(poutine_cost,2)

def display_welcome_menu():
    """()->None
    Prints a welcome message and the menu
    
    >>> display_welcome_menu()
    Welcome to ★Magic Pizza★! The place where the ★Magic★ begins!
    What would you like to do?

    A. Get a ★special★ order
    B. ★Magic★ missing value finder (using a ★Magical★ formula)
    C. How many small ★Magic★ pizzas should I get to match a big one?
    """
    
    print("Welcome to ★Magic Pizza★! The place where the ★Magic★ begins!")
    print("What would you like to do?")
    print("\nA. Get a ★special★ order")
    print("B. ★Magic★ missing value finder (using a ★Magical★ formula)")
    print("C. How many small ★Magic★ pizzas should I get to match a big one?")

def special_orders():
    """()->None
    Asks the user to choose between a cake or a poutine by typing
    cake or by typing poutine, asks him to enter the diameter as a positive
    integer, asks him to enter the height as a positive floating point
    number, asks him to enter yes/y or no to add a special ingredient
    and finally prints the cost of the pizza cake or pizza poutine
    
    >>> special_orders()
    Would you like a ★Magic★ cake or a ★Magic★ poutine? cake
    Enter the diameter: 12
    Enter the height: 1
    Do you want guacamole? yes
    
    The cost is: 2062.03 $
    
    >>> special_orders()
    Would you like a ★Magic★ cake or a ★Magic★ poutine? cake
    Enter the diameter: 5
    Enter the height: 2
    Do you want guacamole? y
    
    The cost is: 365.57 $
    
    >>> special_orders()
    Would you like a ★Magic★ cake or a ★Magic★ poutine? poutine
    Enter the diameter: 2
    Enter the height: 1
    Do you want guacamole? no
    
    The cost is: 9.42 $
    """
    
    order = input("Would you like a ★Magic★ cake or a ★Magic★ poutine? ")
    diameter = int(input("Enter the diameter: "))
    height = float(input("Enter the height: "))
    wants_special = input("Do you want "+SPECIAL_INGREDIENT+"? ")
    
    if order == "cake":
        total_cost = get_pizza_cake_cost(diameter, height)
    elif order == "poutine":
        total_cost = get_pizza_poutine_cost(diameter, height)

    if wants_special == "yes" or wants_special == "y":
        total_cost += SPECIAL_INGREDIENT_COST
        print("\nThe cost is:", round(total_cost,2), "$")
    else:
        print("\nThe cost is:", total_cost, "$")  
    
def quantity_mode():
    """()->None
    Asks the user to enter 2 positive floating point numbers
    and prints the number of small pizzas that must be ordered
    to get at least the same quantity of the bigger pizza

    >>> quantity_mode()
    Enter the first ★Magic★ pizza's diameter: 12
    Enter the second ★Magic★ pizza's diameter: 10

    You should get 2 ★Magic★ pizzas.
    
    >>> quantity_mode()
    Enter the first ★Magic★ pizza's diameter: 2
    Enter the second ★Magic★ pizza's diameter: 1

    You should get 4 ★Magic★ pizzas.
    
    >>> quantity_mode()
    Enter the first ★Magic★ pizza's diameter: 5
    Enter the second ★Magic★ pizza's diameter: 3

    You should get 3 ★Magic★ pizzas.
    """
    
    diameter1 = float(input("Enter the first ★Magic★ pizza's diameter: "))
    diameter2 = float(input("Enter the second ★Magic★ pizza's diameter: "))
    
    quantity = get_fair_quantity(diameter1, diameter2)
    print("\nYou should get", quantity, "★Magic★ pizzas.")

def formula_mode():
    """()->None
    Asks the user to enter 4 positive float values and one that
    is equal to -1 and prints the missing value which has a value of -1
    
    >>> formula_mode()
    Enter the large ★Magic★ pizza's diameter: 12
    Enter the small ★Magic★ pizza's diameter: 6
    Enter the large ★Magic★ pizza's cost: 10
    Enter the small ★Magic★ pizza's cost: -1
    Enter the number of small ★Magic★ pizzas: 2

    The ★Magic★ missing value is: 5.0
    
    >>> formula_mode()
    Enter the large ★Magic★ pizza's diameter: 29.93
    Enter the small ★Magic★ pizza's diameter: 8
    Enter the large ★Magic★ pizza's cost: 7
    Enter the small ★Magic★ pizza's cost: 2
    Enter the number of small ★Magic★ pizzas: -1

    The ★Magic★ missing value is: 4
    
    >>> formula_mode()
    Enter the large ★Magic★ pizza's diameter: -1
    Enter the small ★Magic★ pizza's diameter: 8
    Enter the large ★Magic★ pizza's cost: 9.55
    Enter the small ★Magic★ pizza's cost: 12.47
    Enter the number of small ★Magic★ pizzas: 4

    The ★Magic★ missing value is: 14.0
    
    """
    
    d_large = float(input("Enter the large ★Magic★ pizza's diameter: "))
    d_small = float(input("Enter the small ★Magic★ pizza's diameter: "))
    c_large = float(input("Enter the large ★Magic★ pizza's cost: "))
    c_small = float(input("Enter the small ★Magic★ pizza's cost: "))
    n_small = float(input("Enter the number of small ★Magic★ pizzas: "))
    
    missing_value = pizza_formula(d_large, d_small, c_large, c_small, n_small)
    print("\nThe ★Magic★ missing value is:", missing_value)

def run_pizza_calculator():
    """()->None
    Displays the welcome message, the options to choose from, asks
    the user to choose one, and calls the appropriate function for
    the task
    
    >>> run_pizza_calculator()
    Welcome to ★Magic Pizza★! The place where the ★Magic★ begins!
    What would you like to do?

    A. Get a ★special★ order
    B. ★Magic★ missing value finder (using a ★Magical★ formula)
    C. How many small ★Magic★ pizzas should I get to match a big one?

    What will you choose? A
     
    Would you like a ★Magic★ cake or a ★Magic★ poutine? cake
    Enter the diameter: 2
    Enter the height: 1
    Do you want guacamole? yes

    The cost is: 35.7 $
    
    >>> run_pizza_calculator()
    Welcome to ★Magic Pizza★! The place where the ★Magic★ begins!
    What would you like to do?

    A. Get a ★special★ order
    B. ★Magic★ missing value finder (using a ★Magical★ formula)
    C. How many small ★Magic★ pizzas should I get to match a big one?

    What will you choose? B
     
    Enter the large ★Magic★ pizza's diameter: 29.93
    Enter the small ★Magic★ pizza's diameter: 8
    Enter the large ★Magic★ pizza's cost: 7
    Enter the small ★Magic★ pizza's cost: 2
    Enter the number of small ★Magic★ pizzas: -1

    The ★Magic★ missing value is: 4
    
    >>> run_pizza_calculator()
    Welcome to ★Magic Pizza★! The place where the ★Magic★ begins!
    What would you like to do?

    A. Get a ★special★ order
    B. ★Magic★ missing value finder (using a ★Magical★ formula)
    C. How many small ★Magic★ pizzas should I get to match a big one?

    What will you choose? C
     
    Enter the first ★Magic★ pizza's diameter: 5
    Enter the second ★Magic★ pizza's diameter: 3

    You should get 3 ★Magic★ pizzas.
    
    >>> run_pizza_calculator()
    Welcome to ★Magic Pizza★! The place where the ★Magic★ begins!
    What would you like to do?

    A. Get a ★special★ order
    B. ★Magic★ missing value finder (using a ★Magical★ formula)
    C. How many small ★Magic★ pizzas should I get to match a big one?

    What will you choose? E
     
    Invalid Mode.
    """
    
    display_welcome_menu()
    choice = input("\nWhat will you choose? ")
    
    print(" ")
    if choice == "A":
        special_orders()
    elif choice == "B":
        formula_mode()
    elif choice == "C":
        quantity_mode()
    else:
        print("Invalid Mode.")



