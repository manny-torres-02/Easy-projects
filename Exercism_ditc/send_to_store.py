def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    # cycle through each key in the shopping cart
    store ={}
    
    for food, items in cart.items(): 
      if food in aisle_mapping: 
        store[food] = [cart[food]] + aisle_mapping[food]
        
    # cart.update(aisle_mapping)
    print(store)
    return store
cart = {'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2}
aisle_mapping = {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False],
                  'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}

send_to_store(cart, aisle_mapping)