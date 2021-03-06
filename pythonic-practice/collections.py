#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the example module. This module does stuff.
"""
__author__ = ["[Davis Hong](https://github.com/davislf2)"]
__copyright__ = "Copyright 2018, The Boundary of Knowledge Project"
__credits__ = "Davis Hong"
__license__ = "MIT License"
__version__ = "0.1.0"
__maintainer__ = "Davis Hong"
__email__ = "davislf2.net@gmail.com"
__status__ = "Prototype"
__date__ = '13/11/2018'



"""
01 - Adding Iteration
"""

def adding_iteration():
    class ShoppingCart:
        def __init__(self):
            self.items = []

        def add_item(self, it):
            self.items.append(it)

        def __iter__(self):
            sorted_items = sorted(self.items, key=lambda i: -i.price)
            return sorted_items.__iter__()
            # for i in sorted_items:
            #     yield i


    class CartItem:
        def __init__(self, name, price):
            self.price = price
            self.name = name


    cart = ShoppingCart()
    cart.add_item(CartItem("guitar", 799))
    cart.add_item(CartItem("cd", 19))
    cart.add_item(CartItem("iPhone", 699))

    # Can we for-in the cart?
    # what if it was to be sorted?

    print("Items in your cart.")
    for item in cart:
        print(" * {} ${}".format(item.name, item.price))

