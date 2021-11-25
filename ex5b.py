""" Analyse and design a solution for the following problems.

1. Given that a quadratic equation is of the form, Ax^2 + Bx + C = 0 , where A , B , C are real parameters such that A , B is not zero. A and B are the co-efficient of x , of second and first degrees respectively and c a constant. Find and output the roots of the quadratic equation.

2. Find the Area of a circle of radius, r , given that PI is 3.143 .

3. A shop keeper sold an item of cost, $340.00 at $372.99 including a tax of $2.99 .find the
    a. selling price
    b. profit made
    c. profit percentage
    d. tax percentage
"""

"""
problem 1
Analysis:
    input: A, B and C
    output: x
    process: x = (-B + or - squareroot(B square - 4*A*C)) / 4*A
Design:
    A = input: Enter a value for A
    B = input: Enter a value for B
    C = input: Enter a value for C
    x1 = (-B + squareroot(B square - 4*A*C)) / 4*A
    x2 = (-B - squareroot(B square - 4*A*C)) / 4*A

    output: A and B
"""

"""
problem 2
Analysis:
    input: radius, PI
    output: Area
    process: Area = radius * radius * PI
Design:
    PI = 3.143
    radius = input: Enter a value for radius
    Area = radius * radius * PI

    output: Area
"""

"""
problem 3
Analysis:
    input: selling_price_taxed, cost_price, tax
    output: selling_price, profit, profit_percentage, tax_percentage
    process:
        selling = selling_price_taxed - tax
        profit = selling_price - cost_price
        profit_percentage = profit * 100 / cost_price
        tax_percentage = tax * 100 / cost_price
Design:
    selling_price_taxed = 372.99
    cost_price = 340.00
    tax = 2.99

    selling = selling_price_taxed - tax
    profit = selling_price - cost_price
    profit_percentage = profit * 100 / cost_price
    tax_percentage = tax * 100 / cost_price

    output: selling_price, profit, profit_percentage, tax_percentage
"""
