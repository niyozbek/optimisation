import array
import random
import numpy

print('2.1 Tasks')
# 1. Write a function that takes an integer and returns True if it is even. A way to figure out if
# an integer is even or odd is to divide the number by 2 and compute the remainder. If there
# is a remainder then it is an odd number, otherwise it is even. Use the following numbers to
# test your code: 5 and 122.
def isEven(number: int) -> bool: 
    return number % 2 == 0
print(isEven(5))
print(isEven(122))

# 2. In a module, there is a coursework and a quiz. The contribution from each element is configurable as a percentage, e.g. x% contribution from coursework and y% contribution from
# the quiz, where x + y = 100. With x and y, we create an array p = (x, y). Consider that
# someone achieves c marks for the coursework, and q marks for the quiz; all these marks are
# out of 100. So, the marks array is: m = (c, q). Write a function that takes the arrays p and
# m, and returns the overall percentage of marks achieved for a student.
def getMark(p: array, m: array) -> float:
    if len(p) != len(m):
        raise Exception("Sorry, array size do not match")
    mark: float = 0
    for index, element in enumerate(p):
        mark += element * m[index]
    return mark
print(getMark([0.5, 0.4, 0.1], [49, 40, 100]))

# 3. Write a function that can return the maximum number in a list of integers using only
# for loop and comparison operators. Use the following numpy array to test your function:
# (1, 19, 2, 3, 4, 100); your program should return 100
def getMaximum(numbers: array) -> int:
    maxNumber: int = float('-inf')
    for number in numbers:
        if number > maxNumber:
            maxNumber = number
    return maxNumber
print(getMaximum([1, 19, 2, 3, 4, 100]))

# 4. Write a function that can produce an m × n dimensional random integer uniformly. Here m
# and n should be user defined. [Hint: you may find the random.uniform function useful]
def getRandom(m: int, n: int): 
    return numpy.random.uniform(0, 1, (m, n))
print(getRandom(20, 30))

# 5. The Fibbonacci numbers, commonly denoted as Fn for a sequence, called the Fibbonacci
# sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1
def nThFibonacci(n: int) -> int: 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a = 0
    b = 1
    c = 0
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return c
print(nThFibonacci(0))
print(nThFibonacci(1))
print(nThFibonacci(2))
print(nThFibonacci(100))

import matplotlib .pyplot as plt # im p o r t l i b r a r y
plt.ion () # t h i s e n a b l e s i n t e r a c t i v e p l o t t i n g
# x = [1, 2, 3, 5, 6] # h o r i z o n t a l a x i s v a l u e
# y = [2, 4, 5, 6, 6] # v e r t i c a l a x i s v a l u e s
# plt.plot(x, y) # p l o t a l i n e g r a p 
# input()

# 3.1 Task.
# Using the solutions for exercises in 2.1 (5), generate a plot of the function response when n varies
# from 0 to 100.
fibonacciX = range(0, 101)
fibonacciY = []
for n in fibonacciX:
    fibonacciY.append(nThFibonacci(n))
plt.plot(fibonacciX, fibonacciY)
input()