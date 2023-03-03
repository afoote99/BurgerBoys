#Grant Alston
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

#These lines were to make sure it worked
#print(oCust.order.burger_count)
#oCust.randomName()
#print(oCust.customer_name)
