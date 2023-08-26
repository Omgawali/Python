
from functools import reduce

def addlist(no1,no2):
    if(no1<no2):
        return no1
    else:
        return no2    

def main():
    print("Enter number of elements :")
    length=int(input())
    
    arr=list()
    print("Enter element ")
    for i in range(length):
        value=int(input())
        arr.append(value)

    result=reduce(addlist,arr)  
    print(result)  


if __name__=="__main__":
    main()