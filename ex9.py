# ex9.py
'''
Find the Truth Value of the following:
  - True and not False
  - not True and not False
  - True and False and True or False
  - True or False and True or False
  
Write a simple program that makes use of all the relational and logical operators.
'''


'''
The truth values for:
  - True and not False => True and True => True
  - not True and not False => False and True => False
  - True and False and True or False => False or False => False
  - True or False and True or False => True or False or False => True
'''
# Code test for the above solution using print statements
# format: problem == my_solution, if True, I was right

print((True and not False) == True)
print((not True and not False) == False)
print((True and False and True or False) == False)
print((True or False and True or False) == True)


# A program that make use of all the relational and logical operators
# logical operators: and, or, not
# relational operators: <, >, <=, >=, ==, !=
# In this case, all these operators must appear in my code in someway

image_name = input("Enter image name: ").lower()
image_extension = input('Enter image extension: ').lower()
image_size = int(input('Enter image size: '))
image_is_free = input('Is image free to use(Y/N or YES/NO): ').lower()

# stab data to test manually
# image_name = 'design'
# image_extension = 'jpeg'
# image_size = 70
# image_is_free = 'n'

IS_TRUE = True
IS_FALSE = False


TEN_MG = 10
TWO_CHARS = 2
TWENTY_CHARS = 20
RECOMMENDED_IMAGE_SIZE = 120
RECOMMENDED_IMAGE_EXTENSION = 'jpeg'


if image_size <= TEN_MG:
    print(f"Please select an image with a more bigger size than {TEN_MG}")
elif image_size > RECOMMENDED_IMAGE_SIZE:
    print(
        f'Please do not upload an with size more than {RECOMMENDED_IMAGE_SIZE}')
else:
    chars_in_image_name = len(image_name)

    if not chars_in_image_name < TWO_CHARS and not chars_in_image_name >= TWENTY_CHARS:

        if image_extension != RECOMMENDED_IMAGE_EXTENSION:
            print(
                f"Recommend image extension is {RECOMMENDED_IMAGE_EXTENSION}")
        else:

            is_free_image = IS_TRUE if image_is_free == 'y' or image_is_free == 'yes' else IS_FALSE

            print()
            print(f"Image summary")
            print(f"Name: {image_name}")
            print(f"Extension: {image_extension}")
            print(f"Size: {image_size}")
            print(f"Free: {is_free_image}")

    else:
        print(
            f'please, image name should be between {TWO_CHARS} and {TWENTY_CHARS}')
