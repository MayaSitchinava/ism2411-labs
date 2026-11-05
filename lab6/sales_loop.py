# Self-Assessment:
#1. It is like saving money in a piggy bank. You initialize a total variable to 0 to Python has starting point, loop and update it by 
# adding each item one by one, and use the result after the loop finishes to get your final answer instead of incomplete middle steps
#2. The while loop is longer because you must manually write code to set up an index (i = 0), check the limit (i < len(sales))and step 
# forward (i +=1). A for loop handles all of that automatically making it shorter and safer for lists, whereas while loops are better 
# when you don't know the exact number of iterations in advance.
#3. In a summer retail job a list of daily revenue numbers like [150.00, 200.50, 89,99]can be passed through a loop to accumulate each 
# sale into a total_revenue variable starting at 0. Once finished it prints the single final total earned for that point.


# Exercise 1 - A running total
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0 
for sale in sales:
    total += sale 
print(f"Total: ${total}")

# Exercise 2 - Total, count, and average
total = 0
count = 0
for sale in sales:
    total += sale
    count += 1

average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

# Exercise 3 - The largest value so far
current_max = 0 
for sale in sales:
    if sale > current_max:
        current_max = sale

print(f"Largest sale: ${current_max}")

# Exercise 4 
count_over_100 = 0
total_over_100 = 0
for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale

print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")

# Exercise 5 
for sale in sales: 
    if sale > 400:
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")

# Exercise 6 
total = 0
i = 0
while i < len(sales):
    total += sales [i]
    i += 1

print(f"Total (while loop): ${total}")

# Exercise 7 
for sale in sales: 
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0
    discounted_price = sale * (1 - discount)
    print(
        f"${sale} {discount * 100:.0f}% discount"
        f"${discounted_price:.2f}"
    )