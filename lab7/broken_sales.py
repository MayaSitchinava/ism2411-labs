# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale #logic error: replace '=' with '+=' so total accumulates instead of overwriting 
print(f"Total: ${total}")

count = 0
for sale in sales:    #Suntax error: add missing colon ':' at the end of the for loop definition
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):    #Runtime error: change '<=' to '< so index 'i' stays within the range 
    print(sales[i])
    i += 1
