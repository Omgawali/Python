
from functools import reduce

def morethn(no):
    if(no>=70)and(no<=90):
        return no

def Increase(no):
    return no+10

def add(a,b):
    return a+b    

def main():
    #arr=[4,34,36,76,68,24,89,23,86,90,45,70]

    arr=[]
    print("Enter no of element")
    size=int(input())

    print("Enter the elements")
    for i in range(size):
        value=int(input())
        arr.append(value)

    output=list(filter(morethn,arr))
    print(output)

    output1=list(map(Increase,output))
    print(output1)

    output2=reduce(add,output1)
    print(output2)

if __name__=="__main__":
    main()