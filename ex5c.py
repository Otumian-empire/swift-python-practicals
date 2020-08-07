"""
Implement the design from the practicals in `exercise 5 b (Design of a solution)` 
"""


"""
problem 1
A = input: Enter a value for A
B = input: Enter a value for B
C = input: Enter a value for C
x1 = (-B + squareroot(B square - 4*A*C)) / 4*A
x2 = (-B - squareroot(B square - 4*A*C)) / 4*A
"""


from math import sqrt
A = int(input("Enter a value for A: "))
B = int(input("Enter a value for B: "))
C = int(input("Enter a value for C: "))

if (B ** 2) >= (4*A*C):
    x1 = (-(B) + sqrt((B ** 2) - (4*A*C))) / (4*A)
    x2 = (-(B) - sqrt((B ** 2) - (4*A*C))) / (4*A)

    print(x1, x2)
else:
    print("There is some dumb error - actually there is not but some complex numbers")


"""
problem 2
PI = 3.143
radius = input: Enter a value for radius
Area = radius * radius * PI

output: Area
"""

PI = 3.143
radius = float(input("Enter a value for radius: "))
Area = radius * radius * PI

print(Area)


"""
problem 3
selling_price_taxed = 372.99
cost_price = 340.00
tax = 2.99

selling_price = selling_price_taxed - tax
profit = selling_price - cost_price
profit_percentage = profit * 100 / cost_price
tax_percentage = tax * 100 / cost_price

output: selling_price, profit, profit_percentage, tax_percentage
"""

selling_price_taxed = 372.99
cost_price = 340.00
tax = 2.99

selling_price = selling_price_taxed - tax
profit = selling_price - cost_price
profit_percentage = (profit * 100) / cost_price
tax_percentage = (tax * 100) / cost_price

print(f"selling price:  {selling_price}, profit: {profit}, profit percentage: {profit_percentage}, tax percentage: {tax_percentage}")
