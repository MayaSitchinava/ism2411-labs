#Self Assessment:
#1. The missing colon (SyntaxError) was the easiest bug to find because Python showed the error. I found the logic bug (total = sale) by using print() to check the values. The IndexError was found using the traceback. I am getting better at finding syntax errors, but logic errors still take more time to figure out.
#2. apply_discount (price, tier) takes a starting price and membership level ("gold", "silver", "bronze" or another value). It calculates and returns the price after the discount. A colleague can uuse it easily because the inputs and outputs are clear.
#3. AI: Disclosure: AI was used to help explain Python errors


# Exercise 1 

#Defining a function
def calculate_tax(price, rate):
    return price * rate 

#calling the function 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")

# Exercise 2 

#Defining a function with multiple parameters
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price 


# Calling the functiion with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")


# Exercuse 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

#Calling the final_price function
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

orders = [(200, 'gold'), (150, 'silver'), (8, 'bronze'), (500, 'none')]

rate = 0.07

for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}" )


# Exercise 6

x = 100 # global x 

def double_it():
    x = 999 # local x
    return x * 2

print(x)
print(double_it())
print(x)