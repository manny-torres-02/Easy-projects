def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    #cycle by key in the cart
    for food, items in fulfillment_cart.items():
      if food in store_inventory and store_inventory[food][0] > 0:
        store_inventory[food][0] -= fulfillment_cart[food][0]
        if store_inventory[food][0] == 0:
          store_inventory[food][0] = "out of stock"

    print(store_inventory)

fullfillment_cart = {'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True],
                  'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]}

store_inventory =  {'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False],
                  'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}

update_store_inventory(fullfillment_cart, store_inventory)