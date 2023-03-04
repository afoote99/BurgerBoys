# IS 303-003
# Team 8
# Ian Purnell, Allan Foote, Grant Alston, Keller Elison, Michael Spotts
# 3/4/23
# Hamburger Order Tracker (Group Project)

#Creates all the objects needed for the Hamburger Door Dash assignment
import random
class Order :
    def __init__(self) :
        self.burger_count = self.randomBurgers()

    def randomBurgers(self) :
        return random.randint(1, 20) 
    
class Person :
    def __init__(self) :
        self.list_of_names = list(["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"])
        self.customer_name = self.randomName()

    def randomName(self) :
        return self.list_of_names[random.randint(0, len(self.list_of_names)-1)]
    
class Customer(Person) :
    def __init__(self):
        super().__init__()
        self.order = Order()
        
# Creating the variable for the queue of 100 customers
queueCustomers = []
for iCount in range(0, 100) :
    oCust = Customer()
    queueCustomers.append([oCust.customer_name, oCust.order.burger_count])
    iCount += 1

# Create the Customer Dictionary
dctCustomer = {}

# Get name and # of eaten burgers for every customer from nested list [customer_name, burger_count]
for iCount in range (len(queueCustomers)) :
    name = queueCustomers[iCount][0]
    burgers_eaten = queueCustomers[iCount][1]
    # If the name has already been added to the dictionary add burgers eaten to exisiting amount, otherwise set burger amount
    if name in dctCustomer :
        dctCustomer[name] += burgers_eaten
    else :
        dctCustomer[name]= burgers_eaten

# Sorts the customers by how many burgers they've eaten (High-Low)
lstSortedCustomers = sorted(dctCustomer.items(), key= lambda x: x[1], reverse=True)

# Prints customer names and burgers eaten in order
print ("\n")
for iCount in range (len(lstSortedCustomers)) :
    DisplayName = (lstSortedCustomers[iCount][0]).ljust(19)
    DisplayBurger = (lstSortedCustomers[iCount][1])
    print (DisplayName, DisplayBurger)
print ("\n")
