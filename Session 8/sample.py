# write a python program to add two numbers 
num1 = 1.5
num2 = 6.3
sum = num1 + num2
print(f'Sum: {sum}')


# write a python function to add two user provided numbers and return the sum
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum


# write a program to find and print the largest among three numbers
num1 = 10
num2 = 12
num3 = 14
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print(f'largest:{largest}')


# write a program to print sum of first 6 numbers, starting from 1
i = 1
total = 0
while i <= 6:
    total += i
    i += 1
print(total)


# write a program to print sum of first 6 numbers, starting from 1
total = 0
for i in range(6):
	total += i+1
print(total)


# write a program to print sum of first 6 numbers, starting from 1
total = 0
for i in range(1,7):
	total += i
print(total)


# write a program to print sum of first 'n' numbers, starting from 1
n = 10
total = 0
for i in range(1, n+1):
	total += i
print(total)


# write a function that returns the sum of first 'n' numbers, starting from 1
def sum(n):
	total = 0
	for i in range(n):
		total += i+1
	return total


# write a function which returns the sum of first 'n' numbers, starting from 1
def sum(n):
	total = 0
	for i in range(1, n+1):
		total += i
	return total


