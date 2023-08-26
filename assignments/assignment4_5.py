from functools import reduce



def checkPrime(number) :
 
    for i in range(2, number) :   
        if number % i == 0 :
            return 0
    else :    
        return number

def Mult(numb):
    return numb*2

def addlist(a,b):
    if(a>=b):
        return a
    else:
        return b      

def main():
    #arr=[2,70,11,10,17,23,31,77]
    arr=[]
    print("Enter no of element")
    size=int(input())

    print("Enter the elements")
    for i in range(size):
        value=int(input())
        arr.append(value)

    result= list(map(checkPrime,arr))
    print(result)

    result1= list(map(Mult,result))
    print(result1)  

    result2=reduce(addlist,result1)
    print(result2)  

        
if __name__=="__main__":
    main()        