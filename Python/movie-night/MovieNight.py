"""
*******************************
Movie Night
*******************************
This file is used to allow users to book movie tickets and order concessions.
It must calculate the total cost based on input types and quantities,
terminating the program when done making selections. The subtotal, tax,
online booking fee, and total are then printed.
"""

# Importing random module and setting up constant values.
import random

REGULAR_TICKET = 14.99
THREE_D_TICKET = 17.99
IMAX_TICKET = 19.99
CHILDREN_TICKET = 8.99
SENIOR_TICKET = 10.99
SMALL_POPCORN = 6.99
MEDIUM_POPCORN = 8.99
LARGE_POPCORN = 10.99
SMALL_DRINK = 4.99
MEDIUM_DRINK = 5.99
LARGE_DRINK = 6.99
CANDY = 4.50
NACHOS = 7.99
HOT_DOG = 6.99
MEMBER_DISCOUNT = 0.15
FAMILY_PACKAGE_DISCOUNT = 0.10
ONLINE_BOOKING_FEE = 1.50
TAX_RATE = 0.13

# Checking to see if inputted category and type are valid, returning a Boolean value.
def validate_input(category, type_value):
    categories = ["movie tickets", "concessions", "done"] # Lists to check if inputted values are one of the available options.
    ticket_type = ["regular", "3d", "imax", "children", "senior"]
    concession_type = ["popcorn", "drinks", "candy", "nachos", "hot dog", "daily special"]
    if category.strip().lower() not in categories: # Check if inputted category is one of the available options.
        return False
    elif category.strip().lower() in categories:
        if (category.strip().lower() == "movie tickets") and (type_value.strip().lower() in ticket_type): # If category is valid, check if inputted ticket type is one of the available options.
            return True
        elif (category.strip().lower() == "concessions") and (type_value.strip().lower() in concession_type):
            return True
        else:
            return False

# Calculating ticket cost based on inputted ticket type and quantity, returning a subtotal as a float value.
def calculate_ticket_cost(ticket_type, quantity):
    ticket_types = ["regular", "3d", "imax", "children", "senior"] # List to check if inputted ticket type is one of the available options.
    ticket_prices = [REGULAR_TICKET, THREE_D_TICKET, IMAX_TICKET, CHILDREN_TICKET, SENIOR_TICKET] # List of prices for each type of ticket.
    if ticket_type.lower().strip() in ticket_types:
        i = ticket_types.index(ticket_type.lower().strip()) # If ticket type is valid, find its index in the ticket types list.
        subtotal = (ticket_prices[i] * quantity) # Plug the same index into the ticket prices list and multiply by the quantity to get the subtotal.
        return float(subtotal)
    else:
        return -1

# Calculating concession cost based on inputted concession type, quantity, and size if applicable, returning a subtotal as a float value.
def calculate_concession_cost(concession_type, quantity, size=None):
    diff_sizes = ["popcorn", "drinks"] # Lists to check if inputted concession type has different sizes available or just one.
    one_size = ["candy", "nachos", "hot dog"]
    if concession_type.lower().strip() in diff_sizes:
        size_options = ["small", "medium", "large"] # If the concession type can have different sizes, check that the inputted size is one of the available options.
        if (concession_type.lower().strip() == "popcorn") and (size.lower().strip() in size_options):
            popcorn_size_prices = [SMALL_POPCORN, MEDIUM_POPCORN, LARGE_POPCORN]
            i = size_options.index(size.lower().strip()) # If the size is valid, find its index in the size options list.
            popcorn_subtotal = (popcorn_size_prices[i] * quantity) # Plug the same index into the popcorn size prices list and multiply by the quantity to get the subtotal.
            return float(popcorn_subtotal)
        if (concession_type.lower().strip() == "drinks") and (size.lower().strip() in size_options):
            drink_size_prices = [SMALL_DRINK, MEDIUM_DRINK, LARGE_DRINK]
            i = size_options.index(size.lower().strip()) # If the size is valid, find its index in the size options list.
            drink_subtotal = (drink_size_prices[i] * quantity) # Plug the same index into the drink size prices list and multiply by the quantity to get the subtotal.
            return float(drink_subtotal)
        else:
            return -1
    elif concession_type.lower().strip() in one_size:
        one_size_prices = [CANDY, NACHOS, HOT_DOG]
        i = one_size.index(concession_type.lower().strip()) # If the concession type is valid, find its index in the one size list.
        one_size_subtotal = (one_size_prices[i] * quantity) # Plug the same index into the one size prices list and multiply by the quantity to get the subtotal.
        return float(one_size_subtotal)
    else:
        return -1

# Checking if discount needs to be applied, using the subtotal and number of tickets to find the best possible discount that can be offered, returning a subtotal as an integer or a float.
def apply_discount(subtotal, number_of_tickets):
    membership = input("Are you a member? (y/n): ")
    if (membership.lower().strip() == "y") and (number_of_tickets >= 4): # If user has membership and purchases 4 or more tickets.
        subtotal -= (subtotal * MEMBER_DISCOUNT)
        if subtotal.is_integer():
            return int(subtotal)
        return subtotal
    elif membership.lower().strip() == "y": # If user has membership, but has not purchased 4 or more tickets.
        subtotal -= (subtotal * MEMBER_DISCOUNT)
        if subtotal.is_integer():
            return int(subtotal)
        return subtotal
    elif (membership.lower().strip() != "y") and (number_of_tickets >= 4): # If user does not have membership, but purchases 4 or more tickets.
        subtotal -= (subtotal * FAMILY_PACKAGE_DISCOUNT)
        if subtotal.is_integer():
            return int(subtotal)
        return subtotal
    elif membership.lower().strip() != "y": # If user does not have membership and has not purchased 4 or more tickets.
        if subtotal.is_integer():
            return int(subtotal)
        return subtotal

# Randomly picking a daily special from the list of daily special options, returning a string value for the chosen daily special.
def get_daily_special():
    daily_special_options = ["candy", "nachos", "hot dog"]
    daily_special = random.choice(daily_special_options) # Randomly choose an option from the daily special options list.
    return daily_special

# Calculating tax on the subtotal, returning a float value.
def calculate_tax(subtotal):
    tax_amount = subtotal * TAX_RATE # Multiply the subtotal by the tax rate to find out what the tax amount is.
    return tax_amount

# Checking if inputted ticket type is valid, how many tickets are purchased if so, returning ticket type as a string and quantity as an integer value.
def ticket_option():
    ticket_type = input("Select a ticket type (regular, 3D, IMAX, children, senior): ").lower().strip()
    while not validate_input("movie tickets", ticket_type): # Check if ticket type inputted is valid, and ask for input again if not.
        print("Invalid Movie Ticket type. Please try again.")
        ticket_type = input("Select a ticket type (regular, 3D, IMAX, children, senior): ")
    quantity = input("Enter quantity (greater than 0): ") # Check if quantity inputted is valid.
    while not quantity.isdigit() or int(quantity) <= 0:
        if quantity.startswith('-') and quantity[1:].isdigit(): # Check if quantity inputted is negative and ask for input again is so.
            print("Please enter a valid integer.")
        elif quantity.isdigit() and int(quantity) == 0: # Check if quantity inputted is zero and ask for input again if so.
            print("Quantity must be greater than zero.")
        else:
            print("Please enter a valid integer.") # If input is still invalid ask for input again.
        quantity = input("Enter quantity (greater than 0): ")
    return ticket_type.lower().strip(), int(quantity)

# Checking if inputted concession type is valid, if inputted size is applicable and valid, how many concessions are purchased if valid, returning concession type and size as a string, and returning quantity as an integer value.
def concessions_option():
    concession_sizes = ["popcorn", "drinks"]
    concession_regular = ["candy", "nachos", "hot dog", "daily special"]
    sizes = ["small", "medium", "large"]
    size = None
    concession_type = input("Select concession type (popcorn, drinks, candy, nachos, hot dog, daily special): ").lower().strip()
    while not validate_input("concessions", concession_type): # Check if inputted concession type is valid and ask for input again if not.
        print("Invalid Concession type. Please try again.")
        concession_type = input("Select concession type (popcorn, drinks, candy, nachos, hot dog, daily special): ").lower().strip()
    if concession_type.lower().strip() in concession_sizes:
        size = input("Select size (small, medium, large): ").lower().strip()
        while size.lower().strip() not in sizes: # Check if inputted size is in the sizes list and ask for input again if not.
            print("Invalid size. Please select 'small', 'medium', 'large'.")
            size = input("Select size (small, medium, large): ").lower().strip()
    elif (concession_type.lower().strip() == "daily special") and (concession_type.lower().strip() in concession_regular):
        size = None
        concession_type = get_daily_special()
        print(f"You have selected the daily special: {concession_type.capitalize()}.")
    elif (concession_type.lower().strip() != "daily special") and (concession_type.lower().strip() in concession_regular):
        size = None
    quantity = input("Enter quantity (greater than 0): ")
    while not quantity.isdigit() or int(quantity) <= 0: # Check if quantity inputted is valid.
        if quantity.startswith('-') and quantity[1:].isdigit(): # Check if quantity inputted is negative and ask for input again is so.
            print("Please enter a valid integer.")
        elif quantity.isdigit() and int(quantity) == 0: # Check if quantity inputted is zero and ask for input again if so.
            print("Quantity must be greater than zero.")
        else:
            print("Please enter a valid integer.") # If input is still invalid ask for input again.
        quantity = input("Enter quantity (greater than 0): ")
    return concession_type.lower().strip(), int(quantity), size

# Obtains user input and calculates total cost by calling the functions defined above, printing float values for subtotal, tax, and total.
def main():
    order = input("Would you like to order Movie Tickets, Concessions, or type done to finish? ").strip().lower()
    ticket_cost = 0 # Set these values to zero, so that costs and quantities can be added according to inputs.
    ticket_quantity = 0
    concession_cost = 0
    concession_quantity = 0
    total_cost = 0
    total_quantity = 0
    while order != "done":
        if order == "movie tickets": # Calculate ticket cost based on ticket type and quantity, and keep asking user for more inputs.
            ticket_type, quantity = ticket_option()
            ticket_cost += calculate_ticket_cost(ticket_type, quantity)
            ticket_quantity += quantity
            total_quantity += ticket_quantity
            order = input("Would you like to order Movie Tickets, Concessions, or type done to finish? ").strip().lower()
        elif order == "concessions": # Calculate concession cost based on concession type and quantity, and keep asking user for more inputs
            concession_info = concessions_option()
            if concession_info is not None:
                concession_type, quantity, size = concession_info
                concession_cost += calculate_concession_cost(concession_type, quantity, size)
                concession_quantity += quantity
                total_quantity += concession_quantity
                order = input("Would you like to order Movie Tickets, Concessions, or type done to finish? ").strip().lower()
        else:
            print("Invalid category type. Please try again.") # If input is not valid, ask for input again.
            order = input("Would you like to order Movie Tickets, Concessions, or type done to finish? ").strip().lower()
    if total_quantity == 0:
        print("You don't seem to have ordered anything")
    else:
        total_cost += apply_discount(ticket_cost + concession_cost, ticket_quantity)
        print(f"Subtotal: ${total_cost:.2f}")
        print(f"Tax: ${calculate_tax(total_cost):.2f}")
        print(f"Online Booking Fee: ${ONLINE_BOOKING_FEE:.2f}")
        total = total_cost + calculate_tax(total_cost) + ONLINE_BOOKING_FEE
        print(f"Total: ${total:.2f}")

# Use for testing different cases and calling the main function.
if __name__ == "__main__":
    main()