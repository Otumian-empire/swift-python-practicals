""" 
1. write a program that finds the sum then the average of five numbers, by asking the user to enter then as floats. Display all the inputs, the sum and then the average. [Use descriptive outputs]
2. Write a simple program to simulate an interview for Python developers. Display the anwsers in an essay form, with heading, `Your responds` .
"""

"""
Problem 1
---------
Analysis:
    inputs: five number: num1, num2, num3, num4, num5
    process:
        sumN = num1 + num2 + num3 + num4 + num5
        averageN = sumN / 5
    outputs: sumN, averageN
Design:
    input num1, num2, num3, num4 and num5 as float
    sumN = num1 + num2 + num3 + num4 + num5
    averageN = sumN / 5
    
    display sumN and averageN
"""
num1 = float(input('Enter number as float: '))
num2 = float(input('Enter number as float: '))
num3 = float(input('Enter number as float: '))
num4 = float(input('Enter number as float: '))
num5 = float(input('Enter number as float: '))

sumN = num1 + num2 + num3 + num4 + num5
averageN = sumN / 5

print(f'Sum of numbers: {sumN}')
print(f'Average of numbers: {averageN}')


display sum and average
