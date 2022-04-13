import math

def perfectSquare(number):
    '''
    Function that checks if  a number is a perfect square
    '''
 
    if (number >= 0):
        #to convert it into integer
        sqroot = int(math.sqrt(number))
        return sqroot**2 == number
    return False

#invoke function
print(perfectSquare(64))
 