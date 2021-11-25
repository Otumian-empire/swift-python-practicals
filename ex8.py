""" Using the new concept in this exercise and the white space character, newline - `\n` , write a program that accepts from the user, inputs, name, age, sex and hobby. Output a descriptive essay of the values taken. """

name = input('Enter name: ')
age = input('Enter age: ')
sex = input('Enter sex: ')
hobby = input('Enter hobby: ')

print()
print(f"My name is {name.lower()} and I am {age.lower()}.")
print(f"I am a {sex.lower()} and I love {hobby.lower()}")
