# Exercise #1: Variables and Types

from itertools import product
from math import prod


Product = "Notebook"
unit_price = 4.99
quantity = 12
in_stock = True

# print(type(prod)); #<class 'str'>
# print(type(unit_price)); #<class 'float'>
# print(type(quantity)); #<class 'int'>
# print(type(in_stock)); #<class 'bool'>

# Exercise #2: String Formatting

print(f"{quantity} units of {Product} at ${unit_price:.2f} each. Total: ${unit_price * quantity:.2f}. In stock: {in_stock}")

# Exercise #3: Input functions

# product_in = input("Product Name: ")
# price_in = float(input("Unit Price: ")) # Converts string to float
# quantity_in = int(input("Quantity: ")) # Converts string to int

#print(f"{quantity_in} units of {product_in} at ${price_in:.2f} each. Total: ${price_in * quantity_in:.2f}.") 

# Exercise #4: Product Card

unit_cost = 3.29
revenue = unit_price * quantity
margin = (unit_price - unit_cost) / unit_price * 100

# print(f"Product: {product} ")
# print(f"Revenue: ${revenue:.2f}")
# print(f"Cost: ${unit_cost:.2f}")
# print(f"Margin: {margin:.2f}%")

# Exercise #5 Type Investigations
print ("5" + "3")
print (5 + 3)