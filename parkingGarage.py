class Tickets: # Classes are blueprints for creating objects. For example, the tickets_obj below.
    def __init__ (self, tickets, price): # This method initializes the properties of your class. All new objects will have these properties.
        self.tickets = list(range(1, tickets + 1))
        self.price = price
        self.taken_tickets = []
        self.currentTicket = {'paid': 'False'} # Cyrus added a dictionary
    def take_ticket(self): # This is a method (a function inside of a class) for taking tickets. It uses two list datastructures.
        popped_ticket = self.tickets.pop(0)
        self.taken_tickets.append(popped_ticket)
        print(f"Your ticket number is {popped_ticket}.")
        # available ticket and space are decresed by 1
    def pay_4_parking(self): # This method takes user inputs and determines whether they would like to pay.
        while True: # Cyrus added "while True" to remove the nested fuction
            tick_num = input('What is your ticket number? ') # Cyrus added numeric check for ticket input
            if (not tick_num.isnumeric()):
                print("Ticket number invalid. Please try again.")
            else:
                tick_num = int(tick_num)
                if tick_num in self.tickets: # Cyrus added if input equals invalid ticket.
                    print("Ticket number has not been taken. Please try again.")
                elif tick_num in self.taken_tickets:
                    paying = input(f'The ticket price today is ${self.price}. Would you like to pay for your ticket now? (y/n) ')
                    if paying.lower() == 'y':
                        self.tickets.append(tick_num)
                        self.taken_tickets.remove(tick_num)
                        self.currentTicket["paid"] = 'True' # Cyrus implemented  dictionary check
                        if self.currentTicket.get("paid") == 'True':
                            print('Thank you for parking with us today! You have 15 minutes to leave.')
                            print(f'Ticket paid: {self.currentTicket.get("paid")}')
                            break
                    elif paying.lower() == 'n':
                        print('Don\'t forget to pay for your ticket. ')
                    else:
                        print('Please enter a valid reponse. ') # Cyrus removed the fuction within a function
                else:
                    print('Invalid Ticket Number. Enter another ticket.')

# In your run function, make it possible for users to see the number of available spaces by printing the length of the self.tickets list.

tickets_obj = Tickets(20, 5)

# Below are test runs.

# print(tickets_obj.tickets) # This prints self.tickets for the tickets_obj object.
# print(tickets_obj.price) # This prints self.price for the tickets_obj object.
# tickets_obj.take_ticket() # This runs self.take_ticket() for the tickets_obj object.
tickets_obj.take_ticket()
tickets_obj.pay_4_parking()
# print(f'Ticket paid: {tickets_obj.currentTicket.get("paid")}') # Checks if ticket has been paid.
# This runs self.pay_4_parking for the tickets_obj object.
# print(f'Available ticket numbers: {tickets_obj.tickets} ') # This is a print statement for you to test the results of running your methods above.
# print(f'Taken tickets numbers: {tickets_obj.taken_tickets} ')

        # Spare Code
            # try:
            #     int(tick_num)
            #     it_is = True
            # except ValueError:
            #     it_is = False           
            # if tick_num == False:
            #     print("Ticket number invalid. Please try again.")
            # if tick_num == True:
            #     tick_num = int(tick_num)
            #     continue
