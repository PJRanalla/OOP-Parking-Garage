class ParkingGarage:
    def __init__(self, num_of_spaces):
        self.tickets = [i for i in range(1, num_of_spaces + 1)]
        self.parkingSpaces = [i for i in range(1, num_of_spaces + 1)]
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            self.parkingSpaces.pop(0)
            self.currentTicket[ticket] = {'paid': False}
            print(f"Yout ticket number is: {ticket}. Available spaces: {len(self.parkingSpaces)}")
        else:
            print("\nSorry, THE LOT IS FULL.")

    def payForParking(self):
        ticket_num = int(input("Enter your ticket number: "))
        if ticket_num in self.currentTicket:
            payment = input("Enter the payment amount: ")
            if payment:
                self.currentTicket[ticket_num]['paid'] = True
                print("Your ticket has been paid. You have 15 minutes to leave.")
                print(f"Available spaces: {len(self.parkingSpaces)}")
            else:
                print("Payment amount cannot be empty.")
        else:
            print("Invalid ticket number.")

    def leaveGarage(self):
        ticket_num = int(input("Enter your ticket number: "))
        if ticket_num in self.currentTicket:
            if self.currentTicket[ticket_num]['paid']:
                print(f"Thank you, have a nice day! Available spaces: {len(self.parkingSpaces)}")
                self.parkingSpaces.append(ticket_num)
                self.tickets.append(ticket_num)
                del self.currentTicket[ticket_num]
            else:
                payment = input("Payment is required. Enter payment amount: ")
                if payment:
                    self.currentTicket[ticket_num]['paid'] = True
                    print(f"Thank you, have a nice day! Available spaces: {len(self.parkingSpaces)}")
                    self.parkingSpaces.append(ticket_num)
                    self.tickets.append(ticket_num)
                else:
                    print("Payment amount cannot be empty.")
        else:
            print("The ticket number is invalid.")


garage = ParkingGarage(5)


def garage_Sim():
    while True:
        response = input("Welcome to The Parking Garage on 5th & Main\n" + "\nWould you like to: Park | Exit | Quit? ")
        if response.lower() == 'park':
            garage.takeTicket()
        elif response.lower() == 'exit':
            garage.payForParking()
            garage.leaveGarage()
        elif response.lower() == 'quit':
            print("\nThank you for trying this Python simulation of a parking garage.")
            break
        else:
            print("Please try a different command")

garage_Sim()
