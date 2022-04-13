def powerOfFour(number):
    '''
    Check if a number is a power of four'''
    
    if number ==0:
        return False
    while number !=1:
        if number % 4 !=0:
            return False
        number= number // 4
    return True

#invoke function

print(powerOfFour(16))