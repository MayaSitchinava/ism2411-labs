# Reflections:
#1:Something I found interesting about Python lists is how easy it is to find information without knowing exactly where everything is located.
# I learned that using negative indexing lets you start from the last item instead of the first. This is helpful because it gives you more 
# options when working with different sets of data
#2. I remember working on an assignment where I had to keep track of different products and their sales information. It was difficult to 
# organize everything and make calculations because there was so much data. Now that I understand how Python lists work, I realize I could 
# have used them to store the information, organize it and complete calculations with less effort.


# Exercise 1

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2

print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])

# Exercise 3

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5

coords = (40.7128, -74.0060) #NYC coordinates

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuple protect coodinates from being changed by accident")

# Exercise 6

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sale: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for sale in sales:
    if sale > best:
        best = sale
    if sale < worst:
        worst = sale

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}") 

# Exercise 7

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

# Exercise 8

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales)}")


