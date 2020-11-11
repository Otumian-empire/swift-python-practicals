# mathsmodule

Swyft-python-practical, ex21.

## Developer

- alias: otumian-empire
- email: popecan@gmail.com
- github: otumian-empire@github.com

## What the module is about

This is a simple arithmatic scripts that performs addition, subtraction, multiplication and divsion.

## How to use the module

Import the MathsModule from mathsmodule script. Create an instance of MathsModule. MathsModule accepts int and float types. Call a method and pass the respected arg.

```python
from mathsmodule import MathsModule

module = MathsModule()

res = module.add(2,3,4,5)
print(res)
```

## How the methods work

- add: Takes at least 0 args and returns the total of the args. Total is initialized to 0 . Looping through args and adding the elements to total. If element is not an int or float, loop breaks and total is returned.

- subtr: Takes a and b as args and returns diff, initialized to zero. If a and b is an int or a float, diff is assigned the different between a and b.

- mult: Takes at least 0 args and returns the product total of the args. Total is initialized to 1 . Looping through args and then multiplying the elements by the total. If the element is not an int or float, loop breaks and total is returned.

- div: Takes a and b as args and returns a / b when a and b are int or float and b is not 0, else returns None.

- floor_div: Takes at least 0 args. It returns None if the first element is not int or float. Initialize the total to the first arg. Looping through the args from the second element. return None if the element is not an int or a float or element is 0 . Total becomes, total =// element. return total when no error is encountered.

- pow: Takes a and b as args. returns None if a or b is not an int or a float or when a = 0 . returns a exponent b when there is no error.

- mod: Takes a and b as args. returns None if a or b is not an int or a float or when a = 0 . returns a modulo b when there is no error.
