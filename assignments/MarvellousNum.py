


def checkPrime(number) :
 
    for i in range(2, number) :   
        if number % i == 0 :
            return 0
    else :    
        return number


def addlist(a,b):
    return a+b