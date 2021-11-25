"""
1. write a program that finds the sum then the average of five numbers,
	by asking the user to enter then as floats. Display all the inputs, the sum
	and then the average. [Use descriptive outputs]
2. Write a simple program to simulate an interview for Python developers.
	Display the answers in an essay form, with heading, `Your responds` .
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

num1 = float(input('Enter first number as float: '))
num2 = float(input('Enter second number as float: '))
num3 = float(input('Enter third number as float: '))
num4 = float(input('Enter fourth number as float: '))
num5 = float(input('Enter fifth number as float: '))

sumN = num1 + num2 + num3 + num4 + num5
averageN = sumN / 5

print(f'Sum of numbers: {sumN}')
print(f'Average of numbers: {averageN}')
print(end="\n\n")

"""
Problem 2
---------
Analysis:
	input:
		first name: first_name
		last name: last_name
		date of birth: date_of_birth
		marital status: marital_status
		education: education[]
		experience: experience[]
		expectation: expectation
		hobby: hobby
    job: current or recent job
	process:

	output:
		bio:
			full name: first_name last_name
			date of birth: date_of_birth
			married: marital_status
			hobby: hobby
		job: recent_job
			education:
				education1
				education2
				educationN
			experience:
				experience1
				experience2
				experienceN
			expectation:
				expectation1
				expectation2
				expectationN

Design:
	first_name: Enter first name
	last_name: Enter last name
	date_of_birth: Enter date of birth
	marital_status: Enter marital status(Y/N)
	education[]: Enter all education attained
	experience[]: Enter all necessary experience
	hobby: Enter hobby
  recent_job: Enter most recent job

	bio:
		full name: first_name last_name
		date of birth: date_of_birth
		married: marital_status
		hobby: hobby
	job: recent_job
		education:
			education1
			education2
			educationN
		experience:
			experience1
			experience2
			experienceN
		expectation:
			expectation1
			expectation2
			expectationN

"""

first_name = input('Enter first name: ').lower()
last_name = input('Enter last name: ').lower()

date_of_birth = input(
    'Enter date of birth[2nd April, 2020 or 2-4-2020]: ')
date_of_birth = date_of_birth.lower()

marital_status = input(
    '\nEnter marital status[married, single, divorced, other]: ')
marital_status = marital_status.lower()

educations = []

print('\nEnter all education attained in the format')
print('Bsc, Computer Science, University of Ghana - Legon, 2000-2004')

education = input('Enter education: ')
while(education):
    educations.append(education)
    education = input('Enter education: ')


experiences = []

print('\nEnter all necessary experience in the format')
print('Android Back-end Engineer, EstateFairy App, Axionteq LLC,', end=' ')
print('Developed the Back-end')

experience = input('Enter experience: ')
while(experience):
    experiences.append(experience)
    experience = input('Enter experience: ')


expectations = []

print('\nEnter your expectations: ')

expectation = input('Enter expectation: ')
while(expectation):
    expectations.append(expectation)
    expectation = input('Enter expectation: ')


hobby = input('\nEnter hobby: ')

recent_job = input('\nEnter recent job: ')

print('\nBio:')
print(f'\tfull name: {first_name} {last_name}')
print(f'\tdate of birth: {date_of_birth}')
print(f'\tmarried: {marital_status}')
print(f'\thobby:  {hobby}')

print(f'\njob: {recent_job}')

print('\neducation(s):')
for education in educations:
    print(f'\t{education}')


print('\nexperience(s):')
for experience in experiences:
    print(f'\t{experience}')

print('\nexpectation:')
for expectation in expectations:
    print(f'\t{expectation}')
