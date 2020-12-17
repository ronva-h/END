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


# create a string "Hello World"
string = "Hello World"


# write a function that returns the string "Hello World"
def hello_world():
	return "Hello World"


# create a list of integers from 1 to 10
list_of_ints = [1,2,3,4,5,6,7,8,9,10]


# create a list of integers from 1 to 10
list_of_ints = list(range(1,11))


# write a function that returns the sum of first 'n' numbers, starting from 1
def sum(n):
	total = 0
	for i in range(n):
		total += i+1
	return total


# write a function which returns the sum of first 'n' numbers, starting from 1
def sum_n(n):
	total = 0
	for i in range(1, n+1):
		total += i
	return total


# write a program to demonstrate string slicing
b = "Hello, World!"
print(b[2:5])
print(b[:5])


# write a function which accepts a string and checks if it is empty
def check_empty(string):
	return string == ''


# Write a program that counts up the number of vowels contained in the string s.
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_counter = 0
for vowel in vowels:
    for eachchar in s:
        if vowel == eachchar:     
            vowel_counter += 1
print("Number of vowels : {}".format(vowel_counter))


# Write a program that prints the number of times the string 'bob' occurs in s.
s = "abcbobobjhdfkj"
bob_counter = 0
for i in range(len(s) - 2):
    if s[i:i+3] == 'bob':
        bob_counter += 1
print("Number of times bob occurs is: ",bob_counter)


# Write a program that prints the number of times the string 'bob' occurs in 's'.
print('Number of times bob occurs is:', s.replace('b', 'bb').count('bob'))


# Write a program that prints the longest substring of lowercase string 's' in which the letters occur in alphabetical order.
s = 'zzabccb'
s+="#"
longest_sofar = ''
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if ord(s[j]) < ord(s[j-1]):
            if (j-i) > len(longest_sofar):
                longest_sofar = s[i:j]
            break
print("Longest substring in alphabetical order is: {}".format(longest_sofar))


# Write a program that prints the longest substring of lowercase string 's' in which the letters occur in alphabetical order.
s = 'zzabccb'
cur = lng = s[0]
for c in s[1:] + ' ':
    if c < cur[-1]:
        if len(cur) > len(lng):
            lng = cur
        cur = ''
    cur += c
    print(cur,lng)
print('Longest substring in alphabetical order is: ', lng)


# Write a function which computes the sum of elements in a list
def sumList(aList):
	total = 0
	for element in aList:
		total += element
	return total


# Write a function which computes the sum of elements in a list
def sumList(aList):
	total = 0
	for i in range(len(aList)):
		total += aList[i]
	return total


# Write a function which computes the sum of elements in a list
def sumList(aList):
	return sum(aList)


# Write a function which computes the sum of elements in a list
def sumList(aList):
    if len(aList) == 0:
        return 0 
    else:
        return aList[0] + sumList(aList[1:])


# Write a function which computes the sum of elements in a list
def sumList(aList, sum=0):
    if len(aList) == 0:
        return sum 
    else:
        sum = sum + aList[0]
        return sumList(aList[1:], sum)


# Write a function which computes the sum of elements in a list
sum = 0
def sumList(aList):
    global sum
    if len(aList) == 0:
        return sum 
    else:
        sum = sum + aList[0]
        return sumList(aList[1:])


# write a function to check if a string is a palindrome
def palin(mystr):
    strlen = len(mystr) 
    if strlen <= 1:
        return True
    elif strlen == 2:
        return mystr[0] == mystr[-1]
    else:
        return palin(mystr[0]+mystr[-1]) and palin(mystr[1:-1])


# write a function to check if a string is a palindrome
def palin(mystr):
    strlen = len(mystr) 
    if strlen <= 1:
        return True
    else:
        return (mystr[0] == mystr[-1]) and palin(mystr[1:-1])


# write a python function which swaps the first and last elements of a list passed
def swapList(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp 
    return newList 


# write a python function which swaps the first and last elements of the list passed
def swapList(newList): 
    newList[0], newList[-1] = newList[-1], newList[0] 
    return newList 


# write a function to swap first and last element of a list
def swapList(list): 
    get = list[-1], list[0] 
    list[0], list[-1] = get 
    return list


# write a function to swap first and last element of a list
def swapList(list): 
    start, *middle, end = list
    list = [end, *middle, start] 
    return list

# Write a python function which swaps the first and last elements of the list passed
def swapList(list):   
    first = list.pop(0)    
    last = list.pop(-1) 
    list.insert(0, last)   
    list.append(first)    
    return list


# write a python program to print odd numbers in a list
list1 = [10, 21, 4, 45, 66, 93] 
for num in list1: 
    if num % 2 != 0: 
       print(num, end = " ")


# write a python program to print odd numbers in a list
list1 = [10, 21, 4, 45, 66, 93] 
i = 0
while(i < len(list1)): 
    if list1[i] % 2 != 0: 
        print(list1[i], end = " ") 
    i += 1


# write a python program to print odd numbers in a list
list1 = [10, 21, 4, 45, 66, 93]   
only_odd = [num for num in list1 if num % 2 == 1]   
print(only_odd) 


# write a python program to print odd numbers in a list
list1 = [10, 21, 4, 45, 66, 93, 11]  
odd_nos = list(filter(lambda x: (x % 2 != 0), list1)) 
print("Odd numbers in the list: ", odd_nos)


