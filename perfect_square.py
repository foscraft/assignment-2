import math
'''
Function that checks if  a number is a perfect square
'''
def number_perfect_square(number):
 
    if (number >= 0):
        #to convert it into integer
        sqroot = int(math.sqrt(number))
        return sqroot**2 == number
    return False

#invoke function
print(number_perfect_square(64))
 