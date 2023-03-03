#Grant Alston
#Creates a queue of 100 customers all with the attributes from the Customer Class found on a different page

from hamburgerObjectsFinal import Customer

#Creating the variable for the queue of 100 customers
iCount = 0
queueCustomers = []
for iCount in range(0, 99) :
    oCust = Customer()
    queueCustomers.append(oCust.customer_name)
    iCount += 1

#Checker to see if it worked:
#print(queueCustomers)