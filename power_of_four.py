'''
Checking whether a number is a power of four
'''

def poweroffour(number):
    if number ==0:
        return False
    while number !=1:
        if number % 4 !=0:
            return False
        number= number // 4
    return True

#invoke function

print(poweroffour(16))