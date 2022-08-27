# Start Your Code here

#Cyrus
# from operator import truediv


class Ticket:
    def __init__(self, tickets, space):
        self.tickets = tickets
        self.space = space

    def takeTicket(self):
        self.tickets -= 1
        self.space -= 1

currentTicket = {False}

t = Ticket(5, 5)

def payForParking():
        while True:
            ticket = input("Hello! Welcome to Coding Temple Garage. A ticket is $1, would you like to purchase a ticket (y,n)?: ")
            if ticket.lower() == 'y':
                price = input("How much would you like to pay?: ")
                print(f"You've paid this much: ")
                print(price)
                t.takeTicket()
                print(f"Tickets Left: ")
                print(t.tickets)
                print(f"Spaces left: ")
                print(t.space)
            if ticket.lower() == 'n':
                print("Have a nice day!")
                break

#     input: (waits for amount and store in a variable)
#     if not empty:
#         display message that ticket has been paid and they have 15 mins to leave.
#     updates "current ticket dict": key "paid" to truediv

# def leaveGarage():
#     if ticket paid,
#         display "Thank You, have a nice day"
#     if ticket not paid,
#         input(please pay)

#     once paid:
#         display "Thank You, have a nice day"
#             {increase ticket count by 1}
#             {increase space count by 1}


payForParking()

"""  """

# Your parking gargage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# class Ticket:
#     def __init__(self, tickets, space):
#         self.tickets = 5
#         self.space = 5

#     def 

# dict_paid= {
#     "currentTicket": "true",
# }

# print(dict_a)

# def takeTicket():



    
#         while True:
#             print("Hello! Welcome to Coding Temple Garage.")
#             ticket = input("A ticket is $1, would you like to purchase a ticket or exit?: ")

#             if ticket == "yes" or "":
#                 print("Thank you, have a nice day!")
            
#             if ticket.lower == 'n' or "no" or "exit" or "quit":
#                 print("Have a nice day!")
#                 break


# def print_receipt(self):
#         print("=~ *15")
#         print("Your Receipt: ")


# parking_garage = Ticket("1")
# parking_garage.takeTicket()


# class Items:
#     def __init__(self, fish, drink, vegetable):
#         self.fish = fish
#         self.drink = drink
#         self.vegetable = vegetable
# class Shopping_cart:
#     def __init__(self, fish, drink, vegetable, cart=[]):
#         self.fish = fish
#         self.drink = drink
#         self.vegetable = vegetable
#         self.cart = cart
#     def add_cart(self, fish, drink, vegetable):
#         new_items = Items(fish, drink, vegetable)
#         self.cart.append(new_items)
#     def print_receipt(self):
#         print("=~ *15")
#         print("Your Receipt: ")
#         for item in self.cart:
#             print(item.fish, item.drink, item.vegetable)
#         print("=~ *15")
#     def run(self):
#         while True:
#             fish = input("What kind of fish do you want for tonight?: ")
#             drink = input("What kind of drink do you want?: ")
#             vegetable = input("What kind of vegetable do you want to buy?: ")
#             self.add_cart (fish, drink, vegetable)
#             cont = input("Do you need anything else (y/n)? ")
#             if cont == 'n':
#                 break
#         self.print_receipt()
# your_cart = Shopping_cart('salmon', 'beer', 'tomato')
# your_cart.run()





# def storeInfo():
#     list = [] 
    
#     while True:
#         cart = input("Do you want to : Show/Add/Delete or Quit?: ")
#         if cart.lower() == "show":
#             print(f"This is your cart: ")
#             for x in list:
#                 print(x)
#         if cart.lower() == "add":
#             item = input("What would you like to add?: ")
#             list.append(item)
#             print(f"This is your cart: ")
#             for x in list:
#                 print(x)
#         if cart.lower() == "delete":
#             item = input("What would you like to delete?: ")
#             list.remove(item)
#             print(f"This is your cart: ")
#             for x in list:
#                 print(x)
#         if cart.lower() == "quit":
#             print(f"This is your cart: ")
#             for x in list:
#                 print(x)
#             break

# storeInfo()









