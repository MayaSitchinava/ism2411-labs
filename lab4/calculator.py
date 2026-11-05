#Self-Assesment: 1. Forgetting to divide the discount percentage by 100 would result in an error.
#python would not crash because the code is syntactically valid. However, instead of applying 10% 
# discount the code would multiple by 10. This results in a negative revenue that produces incorrect 
# business output.
# 2. A common business sencario is employee shift planning or staffing distribution. Integer division 
# (//) determines how many full 8 hour shifts can be scheduledd, while the module operator calculates 
# how many remaining hours are left over for the short-shift. Another example is physical fleet delivery 
# loading where // calculates full truckloads and % identifies the leftover pallet volume needing a smaller van.
# 3.The concept I feel least confident about is managing operator precedence and complex numeric formatting 
# inside f-strings. To strengthen it , I can practice breaking calculations down into separate variable 
# assignments first before formatting them and consistently use explicit parentheses in arithmetic expressions 
# to avoid unexpected order of operation results.




# Exercise 1:
price = 50
quantity = 12
revenue = price * quantity

print(f"Revenue: ${revenue:,.2f}")

# Exercise 2:

cost = 32
price = 50
margin = (price -cost) / price
print(f"Margin: {margin:.1%}")

# Exercise 3: Boolean logic
# Product A wins if margin_a > margin_b
# Product A margin 60%, Product B margin (80-60)/80 = 25%
margin_a = 0.60
margin_b = 0.25
product_a_wins = margin_a > margin_b
print(f"Product A wins: {product_a_wins}")

# Exercise 4: Logic Combo

is_premium = price > 100 and margin > 0.3

price = 150
marginn = 0.35
is_premium = price > 100 and margin > 0.3

# Exercise 5: Division + Mod

print(17/5) # use float division
print(17//5) # use floor division
print(17%5) # use modulus operator to get remainder


# Exercise 6:

#inputs names, retail_price, cost, quantity_sold, discount_pct

product = input("Enter product name: ")
retail_price = float(input("Enter retail price: "))
quantity_sold = int(input("Enter quantity sold: "))
discount_pct = int(input("Enter discount percentage: "))
cost = float(input("Enter cost: "))
print("="*50)
revenue = retail_price * quantity_sold
discounted_revenue = revenue * (1-discount_pct / 100)
gross_margin = (retail_price - cost) / retail_price
net_profit = discounted_revenue - (cost * quantity_sold)

# Output
print(f"Product: {product}")
print(f"Revenue: ${revenue:,.2f}")
print(f"Discounted Revenue: ${discounted_revenue:,.2f}")
print(f"Gross Margin: {gross_margin:.1%}")
print(f"Net Profit: ${net_profit:,.2f}")


# Exercise 7: 

BOX_SIZE = 24
items_ordered = int(input("Enter number of items ordered: "))
full_boxes = items_ordered // BOX_SIZE
loose_items = items_ordered % BOX_SIZE
exact_fit = loose_items == 0
print(f"Full boxes: {full_boxes}")
print(f"Loose items: {loose_items}")
print(f"Exact fit: {exact_fit}")



