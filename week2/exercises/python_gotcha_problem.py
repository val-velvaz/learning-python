# what is the output of the following code
def update_order(new_item, current_order=[]): # definimos una funcion que acepta un nuevo item y guarda la orden actual
    current_order.append(new_item) # en la lista "current_order" se le añade el nuevo item
    return current_order # regresa la lista con el nuevo item

# First order, burger
order1 = update_order({'item': 'burger', 'cost': '3.50'})
# output: burger, 3.50

print(order1)

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})
# output: burger, 3.50, soda, 1.50

# What's in that second order again?
print(order2)