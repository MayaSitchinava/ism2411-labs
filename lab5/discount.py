#Self-Assesment: 
#1. The program first checks if 350 is 500 ore more. Next it checks if 350 is 200 or more. And then 
# it applies a 10% discount and brings the final total to 315
#2. No they don't give the same results. The combined and statemtn only runs if a number is inside the 
# 100-500 range. Two separate if statements check both rules independentyl so a number like 50 would 
# still accidentally trigger the second rule (50 < 500)
#3. We see this everywhere like tax brackets, shipping rates or credit card cash back. Knowing Python
#  conditionals helps you see these everyday systems as simple step-by-step rules and makes it easy to
#  spot exact cutoff points.



# starter code for lab 5

total = float(input("Enter cart total: $"))

# Exercise 1 
# add your if/elif/else here
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.1
elif total >= 100:
    discount = 0.05
else: 
    discount = 0

# discount = 0 # replacce with correct logic
final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")


# Exercise 2
if final > 1000: #strictly greater than.
    status = "manager_approval_required"
else:
    status = "auto_approved"

# print(status)

# Exercise 3

region = "North" #S is capitalized.


if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")
else:
    extra_discount = 0

final = total * (1 - (discount + extra_discount))
print(final)

# Exercise 4 


customer_type = "wholesale" 
if region == "South" and total > 100 and customer_type == "whosesale":
    extra_discount = 0.03

# Exercise 5
amount = 10

if amount <= 0:
    print("SUSPICIOUS")
elif amount < 10000:
    print("NORMAL")
else: 
    print("LARGE -- REVIEW REQUIRED")


# Exercise 6

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False #bool

vip_upgrade = True
if total_spent_this_year > 2000 or orders_this_year > 10:
    vip_upgrade = True
else:
    vip_upgrade = False 


