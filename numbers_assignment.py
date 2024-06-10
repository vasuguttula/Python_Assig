"""
WAP to assign 75 and 3.14 values to the variable and constant.
Check the values and type of those after the assignment.
"""
var1 = 75
var2 = 3.14
NUM1 = 74
NUM2 = 3.14
print(var1, type(var1))
print(var2, type(var2))
print(NUM1, type(NUM1))
print(NUM2, type(NUM2))
'''
WAP to define one complex number with lower case 'j' and
another one with the upper case 'J'.
Check the values and type of the variables after the assignment.
'''
a = 1+2j
print(a, type(a))
b = 1+2J
print(b, type(b))

'''
WAP to assign 99 digits integer number to a variable.
Check the value, size and type of the variable after the assignment.
'''
import sys
num = 123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
print(num)
print(sys.getsizeof(num))
print(type(num))